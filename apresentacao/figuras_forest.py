"""Gráficos de floresta redesenhados para o slide (fontes legíveis do fundo da sala).

Mesmo modelo do manuscrito: logito, τ² por Paule-Mandel, IC da estimativa combinada por Hartung-Knapp (t, k − 1 gl),
intervalo de predição com t (k − 2 gl), IC95% de cada estudo pelo método de Wilson, I² pelo Q de efeitos fixos.
O script confere os números contra o manuscrito antes de salvar (37,6% [21,9–56,5], IP 7–83%, I² 93%;
41,7% [30,4–53,9], IP 15–74%, I² 91%).

Uso: python3 figuras_forest.py   → assets/figuras/fig2_forest_ocular_slide.png e fig3_forest_resp_slide.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from scipy import optimize, stats  # noqa: E402

OUT = Path(__file__).resolve().parent / "assets" / "figuras"
NAVY, RED, INK, GRAY, GRID = "#002060", "#8B0000", "#1F2937", "#5A6270", "#C9CFDA"

for f in ("LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf"):
    p = Path("/usr/share/fonts/truetype/liberation") / f
    if p.exists():
        font_manager.fontManager.addfont(str(p))
plt.rcParams.update({"font.family": ["Liberation Sans", "Arial", "DejaVu Sans"], "svg.fonttype": "none"})

OCULAR = [("İlçe et al., 2017", 33, 81), ("Cinar; Sanlier, 2022", 46, 82), ("Usta et al., 2019", 57, 105),
          ("Mohd Fikri Rosely, 2022", 38, 196), ("Mohd Fikri Rosely; Titi Rahmawati, 2019", 28, 137),
          ("Bieniek et al., 2022", 67, 155)]
RESP = [("İlçe et al., 2017", 32, 81), ("Cinar; Sanlier, 2022", 17, 82), ("Usta et al., 2019", 43, 105),
        ("Mohd Fikri Rosely, 2022", 72, 196), ("Mohd Fikri Rosely; Titi Rahmawati, 2019", 55, 137),
        ("Van Giersbergen et al., 2019", 385, 672), ("Bieniek et al., 2022", 86, 155)]


def inv(x):
    return 1 / (1 + np.exp(-x))


def wilson(e, n, z=1.959964):
    p = e / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def meta(ev, n):
    ev, n = np.asarray(ev, float), np.asarray(n, float)
    y = np.log(ev / (n - ev))
    v = 1 / ev + 1 / (n - ev)
    k = len(y)

    def q(t2):
        w = 1 / (v + t2)
        mu = np.sum(w * y) / np.sum(w)
        return np.sum(w * (y - mu) ** 2) - (k - 1)

    t2 = 0.0 if q(0) <= 0 else optimize.brentq(q, 0, 100)
    w = 1 / (v + t2)
    mu = np.sum(w * y) / np.sum(w)
    se = np.sqrt(np.sum(w * (y - mu) ** 2) / (k - 1) / np.sum(w))
    tc = stats.t.ppf(0.975, k - 1)
    wf = 1 / v
    Q = np.sum(wf * (y - np.sum(wf * y) / np.sum(wf)) ** 2)
    tp = stats.t.ppf(0.975, k - 2)
    sp = np.sqrt(t2 + se ** 2)
    return dict(est=inv(mu), lo=inv(mu - tc * se), hi=inv(mu + tc * se), plo=inv(mu - tp * sp), phi=inv(mu + tp * sp),
                I2=max(0.0, (Q - (k - 1)) / Q), w=w / w.sum())


def br(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def forest(rows, size, out, i2_expect, est_expect, label_pt=15, num_pt=14):
    names, ev, n = zip(*rows)
    m = meta(ev, n)
    assert br(m["est"] * 100) == est_expect, (br(m["est"] * 100), est_expect)
    assert round(m["I2"] * 100) == i2_expect
    W, H = size
    fig = plt.figure(figsize=(W, H), dpi=250)
    fig.patch.set_facecolor("white")
    from PIL import ImageFont
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", label_pt * 10)
    left_w = max(fnt.getlength(s) for s in names) / 10 / 72 + 0.3   # coluna dos nomes cabe o nome mais longo
    right_w = 2.55                                                   # coluna numérica (pol.)
    ax = fig.add_axes([left_w / W, 0.9 / H, (W - left_w - right_w - 0.15) / W, (H - 1.25) / H])
    k = len(rows)
    ys = np.arange(k, 0, -1) + 1.2        # estudos de cima para baixo; linha da combinada em y = 0.6
    yp = 0.55
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.1, k + 1.95)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRAY)
    ax.set_yticks([])
    ax.set_xticks(range(0, 101, 20))
    ax.tick_params(axis="x", labelsize=num_pt, colors=INK, length=5, color=GRAY)
    ax.set_xlabel(f"Prevalência (%)   |   I² = {round(m['I2'] * 100)}%", fontsize=num_pt, color=INK, labelpad=8)
    for gx in range(20, 101, 20):
        ax.axvline(gx, color=GRID, lw=0.6, zorder=0)
    ax.axvline(m["est"] * 100, color=RED, lw=1.4, ls=(0, (4, 3)), zorder=1)
    # cabeçalhos
    hy = k + 1.75
    fig.text((left_w - 0.15) / W, ax.transData.transform((0, hy))[1] / (H * fig.dpi), "Estudo", ha="right", va="center",
             fontsize=num_pt - 1, color=GRAY, fontweight="bold")
    xr = (W - right_w + 0.05) / W
    fig.text(xr, ax.transData.transform((0, hy))[1] / (H * fig.dpi), "eventos/n = %  (IC95%)", ha="left", va="center",
             fontsize=num_pt - 1, color=GRAY, fontweight="bold")
    wmax = m["w"].max()
    for nm, e, nn, y, wi in zip(names, ev, n, ys, m["w"]):
        p = e / nn
        lo, hi = wilson(e, nn)
        ax.plot([lo * 100, hi * 100], [y, y], color=INK, lw=1.8, solid_capstyle="butt", zorder=2)
        s = 0.07 + 0.13 * np.sqrt(wi / wmax)   # lado do quadrado (pol.), área ∝ peso
        ax.scatter([p * 100], [y], marker="s", s=(s * 72) ** 2, color=NAVY, zorder=3, linewidths=0)
        yf = ax.transData.transform((0, y))[1] / (H * fig.dpi)
        fig.text((left_w - 0.15) / W, yf, nm, ha="right", va="center", fontsize=label_pt, color=INK)
        fig.text(xr, yf, f"{e}/{nn} = {br(p * 100)}%  ({round(lo * 100)}–{round(hi * 100)})", ha="left", va="center",
                 fontsize=num_pt, color=INK)
    # estimativa combinada + intervalo de predição
    ax.plot([m["plo"] * 100, m["phi"] * 100], [yp, yp], color=RED, lw=2.4, zorder=2, solid_capstyle="butt")
    dx = [m["lo"] * 100, m["est"] * 100, m["hi"] * 100, m["est"] * 100]
    dy = [yp, yp + 0.38, yp, yp - 0.38]
    ax.fill(dx, dy, color=RED, zorder=3, linewidth=0)
    yf = ax.transData.transform((0, yp))[1] / (H * fig.dpi)
    fig.text((left_w - 0.15) / W, yf + 0.11 / H, "Estimativa combinada", ha="right", va="center", fontsize=label_pt,
             color=INK, fontweight="bold")
    fig.text((left_w - 0.15) / W, yf - 0.17 / H, "(efeitos aleatórios)", ha="right", va="center", fontsize=num_pt - 1,
             color=GRAY)
    fig.text(xr, yf + 0.11 / H, f"{br(m['est'] * 100)}%  ({br(m['lo'] * 100)}–{br(m['hi'] * 100)})", ha="left",
             va="center", fontsize=num_pt, color=INK, fontweight="bold")
    fig.text(xr, yf - 0.17 / H, f"IP {round(m['plo'] * 100)}–{round(m['phi'] * 100)}%", ha="left", va="center",
             fontsize=num_pt - 1, color=RED, fontweight="bold")
    fig.savefig(out, dpi=250, facecolor="white")
    plt.close(fig)
    print("OK", out.name, br(m["est"] * 100), br(m["lo"] * 100), br(m["hi"] * 100),
          round(m["plo"] * 100), round(m["phi"] * 100), round(m["I2"] * 100))


if __name__ == "__main__":
    forest(OCULAR, (12.3, 6.1), OUT / "fig2_forest_ocular_slide.png", 93, "37,6")
    forest(RESP, (10.2, 5.75), OUT / "fig3_forest_resp_slide.png", 91, "41,7", label_pt=14, num_pt=14)
