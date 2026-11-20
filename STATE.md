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

- **Fundação da marca**: [tese](docs/01-base/01_tese.md) e [léxico](docs/01-base/02_lexico.md)
  ativos; entidades em rascunho. Próximo gate: a fundadora revisa as
  [entidades](docs/01-base/03_entidades.md).
- **Conteúdo da marca**: [identidade visual](docs/02-conteudo/marca/03_identidade-visual.md)
  e [voz e tom](docs/02-conteudo/marca/02_voz-e-tom.md) ativas; [quadro de evidências](docs/02-conteudo/marca/04_quadro-de-evidencias.md) com 9 de 11 espaços.
  Próximo gate: posicionamento.

## Decisões vigentes

- Uma camada só, repositório **público** no GitHub e frontmatter rico. Foto e avatar da
  fundadora públicos por autorização dela.
- Commit direto na `main`; sem PR obrigatória.
- Nada de segredos, financeiro/preços, dados de clientes ou qualquer coisa contrária à
  LGPD/GDPR no Git.

## Riscos e bloqueios

- A PopKore ainda não tem primeiro produto: sem ele, o quadro não fecha a ponta "Provas".

- Commit direto sem revisão: o risco de vazar dado sensível aumenta. Mitigação: rodar
  `python scripts/audit-kb.py` e revisar o diff antes de cada push.
- Vários agentes (Claude, ChatGPT/Codex, Gemini, Jev, Cursor) escrevendo: risco de vozes
  divergentes. Mitigação: todos seguem a nota de voz e tom.

## Sem movimento

- Nenhuma frente parada ainda.

## Próxima revisão

- **Data ou gatilho:** quando a primeira nota de marca existir
- **Responsável:** fundadora
