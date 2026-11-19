# PopKore — LLM wiki

Base de conhecimento da **PopKore**, marca de *caos criativo organizado*: templates de Notion,
cursos rápidos e infoprodutos de uma neurodivergente para pessoas descoladas.

É uma Knowledge Base em Markdown versionada no Git, para ser lida pela fundadora **e** por
agentes de IA como contexto para criar com a voz da marca. Nasceu de uma
[semente de KB](https://github.com/wagnerlsmartins/knowledge-base-seed) durante um curso na
ESPM.

## Por onde começar

- Pessoas: [views/00_comece-por-aqui.md](views/00_comece-por-aqui.md)
- Agentes: [AGENTS.md](AGENTS.md)
- Estado atual: [STATE.md](STATE.md)
- Mapa da base: [docs/01-base/00_mapa.md](docs/01-base/00_mapa.md)

## Estrutura

```text
docs/
  01-base/          tese, léxico, entidades
  02-conteudo/      marca/, produtos/, publico/, conteudo-e-canais/
  09-operacao/      schema, camadas, ingestão, colaboração com modelos
views/              trilhas de leitura (fundadora, agentes)
type/               tipos de nota
projeto/            inbox → nota → decisão → backlog → log → handoff
scripts/            ingestão e auditoria da KB
STATE.md            estado atual, próximo gate e riscos
AGENTS.md           instruções para agentes de IA
```

## Regras rápidas

- Commit direto na `main`, depois de rodar `python scripts/audit-kb.py` e revisar o diff.
- **Nunca** entram no Git: segredos e senhas, dados financeiros e preços, dados de clientes,
  ou qualquer coisa que viole a LGPD ou a GDPR. Veja a [política de segurança](.github/SECURITY.md).
- Frontmatter rico em toda nota estrutural ([schema](docs/09-operacao/00_schema.md)).
