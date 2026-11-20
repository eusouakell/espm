---
id: "kb.conteudo.produtos.skill-quadro-de-evidencias"
type: reference
category: content
title: "Primeiro produto: skill Quadro de Evidências"
summary: A primeira porção da PopKore — uma skill gratuita para Claude e ChatGPT que transforma respostas em um quadro de fio vermelho no formato story do Instagram.
status: draft
authority: canonical
audience: [fundadora, agentes]
owner: fundadora
last_reviewed: 2026-11-19
order: 1
tags: [produtos, skill, ia, instagram, porta-de-entrada]
related:
  - 00_mapa.md
  - ../publico/01_personas.md
  - ../marca/01_posicionamento.md
  - ../marca/03_identidade-visual.md
  - ../marca/04_quadro-de-evidencias.md
---

# Primeiro produto: skill Quadro de Evidências

> Decisões da fundadora (2026-11-19): linha, função, plataformas, formato e modelo. O nome,
> o fluxo, o escopo e os critérios de sucesso são propostas do Claude: revise antes de mudar
> para `status: active`. **Preços e números de venda não entram aqui.**

## Em uma frase

Você responde algumas perguntas sobre você ou seu projeto e a IA monta um **quadro de
evidências** com fio vermelho, polaroides e post-its, pronto para postar no **story do
Instagram**.

## Decisões

| Decisão | Escolha |
| --- | --- |
| Linha de produto | skill / plugin de IA |
| O que faz | gera um quadro de evidências, como o [quadro da PopKore](../marca/04_quadro-de-evidencias.md) |
| Plataformas | Claude (skill) **e** ChatGPT (GPT personalizado) |
| Entregável | imagem no formato **story 9:16 (1080×1920)** |
| Modelo | **gratuito**, porta de entrada da marca |
| Critério da fundadora | simples e com impacto visual |

## Por que este produto

- **Persona principal** ([personas](../publico/01_personas.md)): resolve "não sei por onde
  começar" com um resultado bonito em minutos, sem curso e sem jargão.
- **Promessa** ("pipoca para o seu cérebro"): uma porção rápida e gostosa, com resultado
  visível na hora.
- **Diversão:** atende ao desejo de "fazer coisas divertidas para desestressar".
- **Distribuição:** cada story compartilhado leva a estética da PopKore para outras pessoas.
- **Prova de conceito:** a PopKore já fez o próprio quadro nesta base. O produto ensina o
  que a marca pratica.

## Nome (proposta)

**Quadro de Evidências PopKore**. Alternativas: "Fio Vermelho", "Caso Arquivado: Você".

## Como funciona (proposta de fluxo)

1. A pessoa abre a skill no Claude ou o GPT no ChatGPT e escolhe o tema: **sobre mim** ou
   **sobre meu projeto**.
2. A IA faz de 6 a 8 perguntas, **uma de cada vez**, com sugestões de resposta.
3. A IA resume cada resposta em uma frase curta e propõe as ligações (o "fio vermelho").
4. A pessoa confirma ou ajusta.
5. A IA gera o quadro em 1080×1920, no estilo PopKore: moldura listrada, post-its, polaroides,
   alfinetes vermelhos e o selo "feito com PopKore".
6. Encerra com uma dica de legenda e o convite para marcar a PopKore.

### Diferença entre as plataformas

| | Claude (skill) | ChatGPT (GPT) |
| --- | --- | --- |
| Como gera o quadro | código (SVG/HTML), com controle total de layout e cores | gerador de imagem, com menos controle |
| Fidelidade visual | alta: igual ao estilo da marca | média: precisa de prompt de estilo bem amarrado |
| Distribuição | arquivo da skill para instalar | link público do GPT |

## Escopo da primeira versão

- **Entra:** um tema por vez (sobre mim ou sobre meu projeto); 6 a 8 espaços; formato story;
  estilo PopKore fixo; selo da marca; textos que cabem nos cartões.
- **Fica para depois:** foto da pessoa dentro da polaroide, outros formatos (post, carrossel),
  outros estilos visuais e versão em inglês.

## Privacidade

- A PopKore **não coleta** as respostas: tudo acontece na conta de IA da própria pessoa.
- A skill avisa para não incluir dados sensíveis (saúde, documentos, endereço) nem dados de
  outras pessoas sem permissão.
- Depoimentos e prints de quem usar só entram na base com permissão por escrito (LGPD/GDPR),
  no espaço "Provas" do [quadro](../marca/04_quadro-de-evidencias.md).

## Como saber se deu certo (proposta)

- 10 pessoas da persona principal geram e postam o quadro sem ajuda.
- Pelo menos metade marca a PopKore ou comenta que vai usar de novo.
- Surgem os primeiros depoimentos com permissão para o espaço "Provas".

## Próximos passos

1. Revisar e aprovar esta nota.
2. Prototipar a versão Claude, reaproveitando o gerador do quadro desta base
   (`scripts/gerar-quadro-evidencias.py`) no formato 1080×1920.
3. Testar com 3 pessoas da persona principal.
4. Adaptar para GPT.
5. Planejar o lançamento em [conteúdo e canais](../conteudo-e-canais/00_mapa.md).
