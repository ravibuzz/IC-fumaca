// Gera o resumo do SEMICA em Word a partir de RESUMO_SEMICA.md (mesmo texto, conferido com o manuscrito).
// Uso: node resumo/gerar_docx.js  →  resumo/Resumo_SEMICA_Baccaro.docx
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require('docx');

const here = __dirname;
const md = fs.readFileSync(path.join(here, 'RESUMO_SEMICA.md'), 'utf8').split('\n');
const pick = (re) => md.find((l) => re.test(l));

const titulo = pick(/^\*\*SINTOMAS/).replace(/\*\*/g, '').trim();
const autores = pick(/\(Professora orientadora\)/).trim();
const instituicoes = pick(/^Instituições:/).trim();
const corpo = pick(/^\*\*Introdução:\*\*/).trim();
// espaços inseparáveis só em 'n = …' e 'I² = …', para não quebrar a linha no meio do número
const corpoDoc = corpo.replace(/(n|I²) = (\S)/g, '$1\u00a0=\u00a0$2');
const chaves = pick(/^\*\*Palavras-chave:\*\*/).replace(/^\*\*Palavras-chave:\*\*\s*/, '').trim();

const FONT = 'Arial';
const SIZE = 24; // 12 pt
const run = (text, opts = {}) => new TextRun({ text, font: FONT, size: SIZE, ...opts });

// "**Rótulo:** texto **Rótulo:** texto" → runs com o rótulo em negrito
function boldRuns(s) {
  return s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((part) =>
    part.startsWith('**') ? run(part.slice(2, -2), { bold: true }) : run(part));
}

const [instTexto, email] = instituicoes.replace(/^Instituições:\s*/, '').split(/\s*E-mail do autor responsável:\s*/);
const sp = { line: 240, after: 0 }; // espaçamento simples

const doc = new Document({
  creator: 'Theo Augusto Lopes de Moraes Báccaro',
  title: 'Resumo — VIII SEMICA',
  styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1701, left: 1701, bottom: 1134, right: 1134 }, // 3 cm / 2 cm
      },
    },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { ...sp, after: 240 }, children: [run(titulo, { bold: true })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { ...sp, after: 120 }, children: [run(autores)] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { ...sp, after: 120 },
        children: [run(instTexto.trim(), { size: 20 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { ...sp, after: 360 },
        children: [run('E-mail do autor responsável: ', { size: 20 }), run(email.trim(), { size: 20 })] }),
      new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { ...sp, after: 240 }, children: boldRuns(corpoDoc) }),
      new Paragraph({ alignment: AlignmentType.LEFT, spacing: sp,
        children: [run('Palavras-chave: ', { bold: true }), run(chaves)] }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(here, 'Resumo_SEMICA_Baccaro.docx');
  fs.writeFileSync(out, buf);
  const palavras = corpo.replace(/\*\*/g, '').split(/\s+/).filter(Boolean).length;
  console.log(`OK: ${out} (título ${titulo.split(/\s+/).length} palavras; corpo ${palavras} palavras)`);
});
