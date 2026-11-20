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

A marca PopKore já tem tese, léxico, identidade visual, voz e tom e um quadro de evidências;
o posicionamento está em revisão e ainda não existe primeiro produto.

## Frentes ativas

- **Fundação da marca**: [tese](docs/01-base/01_tese.md) e [léxico](docs/01-base/02_lexico.md)
  ativos; [entidades](docs/01-base/03_entidades.md) em rascunho e desatualizadas. Próximo
  gate: atualizar e revisar as entidades.
- **Marca**: [identidade visual](docs/02-conteudo/marca/03_identidade-visual.md) e
  [voz e tom](docs/02-conteudo/marca/02_voz-e-tom.md) ativas;
  [posicionamento](docs/02-conteudo/marca/01_posicionamento.md) em rascunho;
  [quadro de evidências](docs/02-conteudo/marca/04_quadro-de-evidencias.md) com 9 de 11
  espaços. Próximo gate: a fundadora revisa o posicionamento.
- **Público, produtos e canais**: seções vazias. Próximo gate: personas em
  [publico/](docs/02-conteudo/publico/00_mapa.md) e definição do primeiro produto.

## Decisões vigentes

- Uma camada só, repositório **público** no GitHub e frontmatter rico. Foto e avatar da
  fundadora públicos por autorização dela.
- Commit direto na `main`; sem PR obrigatória.
- Nada de segredos, financeiro/preços, dados de clientes ou qualquer coisa contrária à
  LGPD/GDPR no Git.
- Promessa da marca: "Pipoca para o seu cérebro. Resultados em porções rápidas e gostosas."
- Problema central: IA confusa para pessoas criativas.

## Riscos e bloqueios

- A PopKore ainda não tem primeiro produto: sem ele, o quadro não fecha a ponta "Provas" e as
  seções de produtos e canais ficam sem assunto.
- A [tese](docs/01-base/01_tese.md) não menciona IA, mas o posicionamento põe IA no centro.
  Vale revisar se a tese deve citar IA.
- Repositório público com commit direto sem revisão: risco de vazar dado sensível.
  Mitigação: rodar `python scripts/audit-kb.py` e revisar o diff antes de cada push.
- Vários agentes (Claude, ChatGPT/Codex, Gemini, Jev, Cursor) escrevendo: risco de vozes
  divergentes. Mitigação: todos seguem a nota de voz e tom.

## Sem movimento

- Nenhuma frente parada ainda.

## Próxima revisão

- **Data ou gatilho:** quando o posicionamento for revisado
- **Responsável:** fundadora
