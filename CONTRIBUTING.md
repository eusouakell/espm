# Como contribuir

Nesta base o fluxo é **commit direto na `main`** (decisão da fundadora). Se precisar do
básico de Git, veja o [manual de Git](./docs/09-operacao/01_manual-git.md).

## Fluxo

1. `git switch main && git pull --ff-only`
2. editar ou criar Markdown
3. manter o frontmatter rico (ver [schema](./docs/09-operacao/00_schema.md))
4. atualizar os links `related` afetados
5. executar `python scripts/audit-kb.py`
6. revisar o diff: nada de segredos, financeiro/preços, dados de clientes ou violação de
   LGPD/GDPR
7. `git commit` com mensagem clara e `git push`

Branch + PR continuam disponíveis para mudanças grandes ou arriscadas.

## Agentes de IA

Declare o modelo no commit (`Co-Authored-By:`). Veja
[colaboração com modelos](./docs/09-operacao/03_colaboracao-com-modelos.md) e
[AGENTS.md](./AGENTS.md).
