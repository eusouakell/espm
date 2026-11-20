---
id: "kb.base.mapa"
type: map
category: core
title: Mapa da PopKore
summary: Porta de entrada da base — estrutura, ordem de leitura e as decisões fundadoras.
status: active
authority: canonical
audience: [fundadora, agentes]
owner: fundadora
last_reviewed: 2026-11-19
order: 0
tags: [mapa, navegacao]
related:
  - 01_tese.md
  - 02_lexico.md
  - ../09-operacao/00_schema.md
  - ../../STATE.md
---

# Mapa da PopKore

> Comece por aqui. Este é o documento canônico de navegação da base: a LLM wiki da marca
> **PopKore**.

## As decisões fundadoras

- **Objeto:** a marca PopKore, de **caos criativo organizado**: conhecimento em porções
  rápidas (IA, ferramentas e métodos) para pessoas criativas. É um projeto antigo da
  fundadora que está ganhando forma no curso da ESPM, onde esta base nasceu a partir de uma
  semente de KB.
- **Públicos:** a fundadora, para pensar e decidir sobre a marca, e agentes de IA, que usam a
  base como contexto para criar com a voz da PopKore.
- **Camadas:** uma só. Tudo vive aqui.
- **Privacidade:** o repositório no GitHub é **público**: tudo o que entra aqui pode ser lido
  por qualquer pessoa. A foto e o avatar da fundadora são públicos por autorização dela, como
  parte do branding. Nunca entram no Git segredos e senhas, dados
  financeiros e preços, dados de clientes, nem nada que viole a LGPD ou a GDPR.
- **Manutenção:** commit direto na `main`, feito pela fundadora ou por agentes autorizados.
  Sem PR obrigatória.
- **Agentes:** Claude, ChatGPT/Codex, Gemini, Jev, Cursor e outros (ver
  [colaboração com modelos](../09-operacao/03_colaboracao-com-modelos.md)).
- **Frontmatter:** rico (ver [schema](../09-operacao/00_schema.md)).
- **Ingestão de calls:** sim. A pasta [`projeto/`](../../projeto/README.md) fica ativa para
  aulas da ESPM, conversas, briefings e brainstorms.

## Estrutura

- `01-base/`: fundação (tese, léxico, entidades)
- `02-conteudo/`: o conhecimento da marca, em [marca](../02-conteudo/marca/00_mapa.md),
  [produtos](../02-conteudo/produtos/00_mapa.md), [público](../02-conteudo/publico/00_mapa.md)
  e [conteúdo e canais](../02-conteudo/conteudo-e-canais/00_mapa.md)
- `09-operacao/`: governança da própria base (schema, camadas, ingestão)
- `views/`: trilhas de leitura por público
- `type/`: tipos de nota como lente
- `projeto/`: operação viva (inbox, decisões, backlog, logs, handoffs)

## Ordem de leitura sugerida

1. Este mapa
2. [Estado atual](../../STATE.md)
3. [Tese](01_tese.md)
4. [Léxico](02_lexico.md)
5. [Entidades](03_entidades.md)
6. [Mapa de conteúdo](../02-conteudo/00_mapa.md)
