---
id: "kb.state"
type: state
category: operations
title: Estado atual
summary: Leitura operacional curta da base PopKore — frentes, decisões vigentes, próximo gate e lacunas.
status: active
authority: reference
audience: [fundadora, agentes]
owner: fundadora
last_reviewed: 2026-11-19
timestamp: 2026-11-19
related:
  - docs/01-base/00_mapa.md
  - projeto/README.md
---

# Estado atual

## Em uma frase

A LLM wiki da PopKore está instanciada e a tese foi aprovada; o conteúdo da marca ainda está
vazio.

## Frentes ativas

- **Fundação da marca**: [tese](docs/01-base/01_tese.md) ativa; léxico e entidades em
  rascunho. Próximo gate: a fundadora revisa o [léxico](docs/01-base/02_lexico.md).
- **Conteúdo da marca**: quatro seções criadas e vazias. Próximo gate: primeira nota de
  posicionamento e voz em [marca/](docs/02-conteudo/marca/00_mapa.md).

## Decisões vigentes

- Uma camada só, repositório privado e frontmatter rico.
- Commit direto na `main`; sem PR obrigatória.
- Nada de segredos, financeiro/preços, dados de clientes ou qualquer coisa contrária à
  LGPD/GDPR no Git.

## Riscos e bloqueios

- Commit direto sem revisão: o risco de vazar dado sensível aumenta. Mitigação: rodar
  `python scripts/audit-kb.py` e revisar o diff antes de cada push.
- Vários agentes (Claude, ChatGPT/Codex, Gemini, Jev, Cursor) escrevendo: risco de vozes
  divergentes até a nota de voz e tom existir.

## Sem movimento

- Nenhuma frente parada ainda.

## Próxima revisão

- **Data ou gatilho:** quando a primeira nota de marca existir
- **Responsável:** fundadora
