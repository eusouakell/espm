---
id: "kb.conteudo.marca.identidade-visual"
type: reference
category: content
title: Identidade visual
summary: Logo, nome, paleta, tipografia e regras de uso da PopKore.
status: active
authority: canonical
audience: [fundadora, agentes]
owner: fundadora
last_reviewed: 2026-11-19
order: 3
tags: [marca, logo, identidade-visual]
related:
  - 00_mapa.md
  - ../../01-base/01_tese.md
  - ../../01-base/02_lexico.md
---

# Identidade visual

> Logo, cores, tipografia e regras de uso. A paleta foi medida nos pixels da logo.

## Logo

![Logo da PopKore](assets/popkore-logo.svg)

Um balde de pipoca listrado de vermelho e branco, cheio de **cérebros no lugar da pipoca**,
com um cérebro caído ao lado. No centro do balde, uma etiqueta creme com o nome "PopKore" em
vermelho.

## O que a logo comunica

- **Pop + Kore:** a pipoca (cultura pop, entretenimento, cinema) encontra o cérebro (o
  *core*, a mente). É a tese em imagem: cabeças criativas tratadas com leveza e diversão.
- **Cérebros transbordando:** o caos criativo, ideias demais para caber no balde.
- **O cérebro caído:** imperfeição assumida; nem tudo cabe na caixa, e tudo bem.
- **Traço de cartoon com contorno grosso:** tom informal, divertido, nada corporativo.

## Nome (versão só com o nome)

![PopKore só o nome](assets/popkore-nome-vermelho.svg)

O lettering da etiqueta, recortado e vetorizado. Use quando a logo completa não couber:
cabeçalhos, rodapés, assinaturas de e-mail, capas de template e espaços horizontais.

## Paleta

Cores medidas nos pixels da logo:

| Nome | Hex | Onde aparece | Papel |
| --- | --- | --- | --- |
| Vermelho pipoca | `#D40000` | listras do balde | cor principal |
| Vermelho pop | `#FF0000` | o nome "PopKore", listras laterais | destaque, CTA, nome |
| Creme etiqueta | `#E3E0CC` | etiqueta do nome | fundo de marca |
| Branco listra | `#ECECEC` | listras do balde | fundo neutro |
| Pêssego cérebro | `#EAA993` | cérebros (luz) | apoio |
| Rosa cérebro | `#F2C8BA` | cérebros (brilho) | apoio claro |
| Malva cérebro | `#CB788D` | cérebros (sombra) | apoio |
| Lilás | `#C79FBC` | reflexo na lateral | apoio |
| Contorno | `#170003` | traços e contornos | texto e linhas |

O vermelho `#FF0000` sobre creme `#E3E0CC` tem contraste baixo para texto corrido (3:1; sobre
branco, 4:1). Use essa dupla só no nome e em títulos grandes. Para texto corrido, prefira
`#170003` sobre creme ou sobre branco.

## Tipografia

Duas fontes **variáveis** do Google Fonts: um único arquivo cobre todos os pesos do
intervalo, e o desenho vetorial fica nítido em qualquer densidade de tela, de 1x a retina
(2x/3x).

| Uso | Fonte | Pesos | Por quê |
| --- | --- | --- | --- |
| Títulos | [Fraunces](https://fonts.google.com/specimen/Fraunces) | 100–900, tamanho óptico 9–144 | serifa com personalidade pop e um pouco "torta", como o caos criativo; o tamanho óptico redesenha as letras conforme o tamanho na tela |
| Texto | [Atkinson Hyperlegible Next](https://fonts.google.com/specimen/Atkinson+Hyperlegible+Next) | 200–800 | feita para máxima legibilidade, coerente com uma marca feita por e para pessoas neurodivergentes |

O nome "PopKore" **não** é escrito com fonte: use sempre o arquivo do nome.

### Escala tipográfica

Tamanhos em `rem` (1 rem = 16 px), que acompanham o zoom e o tamanho de fonte de quem lê:

| Nível | Fonte | Peso | Tamanho | Entrelinha |
| --- | --- | --- | --- | --- |
| Display | Fraunces | 800 | 3 rem (48 px) | 1,1 |
| H1 | Fraunces | 700 | 2.25 rem (36 px) | 1,15 |
| H2 | Fraunces | 600 | 1.75 rem (28 px) | 1,2 |
| H3 | Fraunces | 600 | 1.375 rem (22 px) | 1,25 |
| Texto | Atkinson Next | 400 | 1 rem (16 px) | 1,6 |
| Texto destacado | Atkinson Next | 700 | 1 rem (16 px) | 1,6 |
| Pequeno / legenda | Atkinson Next | 400 | 0.875 rem (14 px) | 1,5 |

Evite texto corrido abaixo de 14 px e pesos abaixo de 300 em textos pequenos.

### Como usar na web

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@200..800&family=Fraunces:opsz,wght@9..144,100..900&display=swap" rel="stylesheet">
```

```css
:root {
  --fonte-titulo: "Fraunces", Georgia, serif;
  --fonte-texto: "Atkinson Hyperlegible Next", system-ui, sans-serif;
}
body { font-family: var(--fonte-texto); font-size: 1rem; line-height: 1.6; }
h1, h2, h3 { font-family: var(--fonte-titulo); font-optical-sizing: auto; }
```

### Fora da web

- **Canva, Figma e apps de design:** as duas estão disponíveis ou podem ser instaladas a
  partir do Google Fonts.
- **Notion:** não aceita fontes personalizadas. Nos templates, use as fontes do próprio
  Notion e leve a identidade pela capa, pelos ícones, pelas cores e pelo arquivo do nome.

## Regras de uso

- **Área de proteção:** deixe em volta da logo e do nome um espaço livre igual à altura da
  letra "o" do nome.
- **Tamanho mínimo:** logo completa com 120 px (ou 25 mm) de largura; nome com 80 px (ou
  15 mm).
- **Fundos permitidos:**
  - logo completa: branco, creme `#E3E0CC` ou fotos claras e pouco poluídas;
  - nome vermelho: branco ou creme;
  - nome branco: contorno `#170003`, vermelho `#D40000` ou fotos escuras;
  - nome escuro: qualquer fundo claro em que o vermelho não funcione.
- **Não faça:** distorcer ou girar a logo, trocar as cores dos cérebros ou do balde, aplicar
  sombra ou contorno extras, colocar a logo completa sobre fundo vermelho ou estampado, ou
  reescrever o nome com outra fonte.

## Arquivos

| Arquivo | Uso |
| --- | --- |
| [`assets/popkore-logo.svg`](assets/popkore-logo.svg) | **padrão:** vetor, 200 KB, escala sem perder qualidade |
| [`assets/popkore-logo.png`](assets/popkore-logo.png) | raster com fundo transparente, 1753×1582 px |
| [`assets/popkore-logo.jpg`](assets/popkore-logo.jpg) | onde PNG não é aceito (fundo branco) |
| [`assets/popkore-nome-vermelho.svg`](assets/popkore-nome-vermelho.svg) | nome em `#FF0000`, para fundos claros |
| [`assets/popkore-nome-branco.svg`](assets/popkore-nome-branco.svg) | nome em branco, para fundos escuros |
| [`assets/popkore-nome-escuro.svg`](assets/popkore-nome-escuro.svg) | nome em `#170003`, monocromático |

Os SVGs foram gerados por vetorização automática (vtracer) a partir do PNG. São fiéis à
logo, mas não substituem um vetor desenhado à mão: os traços podem ter pequenas
irregularidades em tamanhos muito grandes, como banners e impressão.

O arquivo-fonte original `PopKore.svg` (Inkscape, 23 MB) **não está no Git**: ele guarda 32
imagens PNG embutidas. Guarde-o fora do repositório.

## Pendências

- [x] vetorizar a logo (SVG só com paths)
- [x] versão só com o nome, para cabeçalhos e espaços pequenos
- [x] medir a paleta exata
- [x] regras de uso: área de proteção, tamanho mínimo, fundos permitidos
- [x] tipografia confirmada pela fundadora (2026-11-19)
- [ ] para impressão grande: redesenhar a logo à mão em vetor (designer ou Inkscape)
