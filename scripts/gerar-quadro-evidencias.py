"""Gera o quadro de evidências da PopKore em SVG.

Uso: python scripts/gerar-quadro-evidencias.py

Os espaços do quadro estão em CARTOES e as ligações em FIOS. Para preencher um espaço,
troque o texto de "pergunta" por um texto curto da evidência e mude "preenchido" para True.
A lista de evidências, com fontes, vive em docs/02-conteudo/marca/04_quadro-de-evidencias.md.
"""
import pathlib
import base64
import math
import re
from xml.sax.saxutils import escape

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "docs/02-conteudo/marca/assets"
SAIDA = ASSETS / "popkore-quadro-evidencias.svg"

COR = {
    "contorno": "#170003",
    "vermelho": "#D40000",
    "pop": "#FF0000",
    "creme": "#E3E0CC",
    "branco": "#ECECEC",
    "pessego": "#EAA993",
    "rosa": "#F2C8BA",
    "malva": "#CB788D",
    "lilas": "#C79FBC",
}

# id, tipo, x, y, largura, altura, rotação, cor, grupo, título, pergunta, preenchido
CARTOES = [
    ("foto", "polaroid", 70, 145, 190, 265, -4, "branco", "Quem sou eu", "Foto minha", "a fundadora da PopKore", True),
    ("cerebro", "postit", 300, 130, 190, 170, 3, "pessego", "Quem sou eu", "Meu cérebro", "mil abas abertas, hiperfoco, aprendo em profundidade e preciso ver para lembrar", True),
    ("trajetoria", "folha", 80, 455, 220, 240, 2, "branco", "Quem sou eu", "Trajetória", "Head of Marketing & Context Engineering", True),
    ("irrita", "postit", 330, 470, 190, 170, -3, "rosa", "Quem sou eu", "O que me irrita", "rotina rígida, culpa, sistemas complexos e coisas sem graça", True),
    ("espm", "nota", 560, 560, 200, 150, 4, "creme", "Quem sou eu", "ESPM", "uma LLM wiki estruturada; antes eu fazia wikis sozinha", True),
    ("tese", "postit", 550, 150, 245, 190, -2, "pop", "PopKore", "Caos criativo organizado", "ferramentas leves para cabeças inquietas darem forma às ideias", True),
    ("nome", "polaroid", 830, 130, 190, 255, 5, "branco", "PopKore", "Por que PopKore", "pipoca + cérebro", True),
    ("publico", "nota", 815, 385, 215, 160, -4, "lilas", "PopKore", "Pessoas descoladas", "builders, makers, criativas, ND, marketing e quem quer IA na rotina", True),
    ("produto", "polaroid", 1070, 140, 190, 270, -3, "branco", "PopKore", "Primeiro produto", "print do primeiro template ou curso", False),
    ("catalogo", "folha", 1070, 465, 200, 230, 3, "branco", "PopKore", "Catálogo", "planejado: Notion, cursos, infoprodutos, skills, plugins e IA", True),
    ("provas", "envelope", 795, 570, 255, 175, -2, "creme", "PopKore", "Provas", "depoimentos e resultados (com permissão)", False),
]

# fotos embutidas nas polaroides (caminho relativo a ASSETS)
IMAGENS = {
    "foto": "quadro/fundadora-foto-quadro.jpg",
}

FIOS = [
    ("foto", "cerebro"), ("cerebro", "tese"), ("cerebro", "irrita"), ("irrita", "tese"),
    ("trajetoria", "espm"), ("espm", "tese"), ("tese", "nome"), ("tese", "publico"),
    ("publico", "produto"), ("produto", "catalogo"), ("publico", "provas"), ("catalogo", "provas"),
    ("trajetoria", "foto"),
]

W, H = 1360, 800

# largura média de um caractere, em frações do corpo da fonte, com folga para
# Fraunces/Atkinson e para as fontes de reserva (Georgia/Arial)
LARG_TITULO = 0.62
LARG_TEXTO = 0.56


def nome_paths():
    svg = (ASSETS / "popkore-nome-vermelho.svg").read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    paths = "\n".join(re.findall(r"<path[^>]*/>", svg))
    return vb, paths


def quebra(texto, n):
    linhas, atual = [], ""
    for p in texto.split():
        if len(atual) + len(p) + 1 > n and atual:
            linhas.append(atual)
            atual = p
        else:
            atual = (atual + " " + p).strip()
    if atual:
        linhas.append(atual)
    return linhas


def pino(x, y):
    return (f'<g class="pino"><circle cx="{x + 3}" cy="{y + 4}" r="11" fill="{COR["contorno"]}" opacity=".35"/>'
            f'<circle cx="{x}" cy="{y}" r="11" fill="{COR["pop"]}" stroke="{COR["contorno"]}" stroke-width="3"/>'
            f'<circle cx="{x - 3}" cy="{y - 3}" r="3.5" fill="#fff" opacity=".8"/></g>')


def cartao(c):
    cid, tipo, x, y, w, h, rot, cor, grupo, titulo, pergunta, cheio = c
    cx, cy = x + w / 2, y + h / 2
    fill = COR[cor]
    tinta = "#FFFFFF" if cor == "pop" else COR["contorno"]
    out = [f'<g id="{cid}" transform="rotate({rot} {cx} {cy})">',
           f'<rect x="{x + 7}" y="{y + 9}" width="{w}" height="{h}" rx="4" fill="{COR["contorno"]}" opacity=".35"/>']
    texto_y = y + 46
    if tipo == "polaroid":
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#FFFFFF" stroke="{COR["contorno"]}" stroke-width="4"/>')
        ph = h - 104
        if cid == "nome":
            out.append(f'<rect x="{x + 14}" y="{y + 14}" width="{w - 28}" height="{ph - 14}" fill="#FFFFFF" stroke="{COR["contorno"]}" stroke-width="2"/>')
            lvb, lcorpo = logo_svg()
            out.append(f'<svg x="{x + 18}" y="{y + 18}" width="{w - 36}" height="{ph - 22}" viewBox="{lvb}" preserveAspectRatio="xMidYMid meet">{lcorpo}</svg>')
        elif cid in IMAGENS:
            dados = base64.b64encode((ASSETS / IMAGENS[cid]).read_bytes()).decode("ascii")
            out.append(f'<image x="{x + 14}" y="{y + 14}" width="{w - 28}" height="{ph - 14}" preserveAspectRatio="xMidYMid slice" href="data:image/jpeg;base64,{dados}"/>')
            out.append(f'<rect x="{x + 14}" y="{y + 14}" width="{w - 28}" height="{ph - 14}" fill="none" stroke="{COR["contorno"]}" stroke-width="2"/>')
        else:
            out.append(f'<rect x="{x + 14}" y="{y + 14}" width="{w - 28}" height="{ph - 14}" fill="{COR["contorno"]}"/>')
        if not cheio:
            out.append(f'<text x="{cx}" y="{y + 14 + (ph - 14) / 2 + 14}" text-anchor="middle" font-size="44" fill="{COR["malva"]}" font-family="Atkinson Hyperlegible Next, Arial, sans-serif">+</text>')
        texto_y = y + ph + 24
        tinta = COR["contorno"]
    elif tipo == "folha":
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#FFFFFF" stroke="{COR["contorno"]}" stroke-width="4"/>')
        for gy in range(y + 24, y + h - 6, 18):
            out.append(f'<line x1="{x + 4}" y1="{gy}" x2="{x + w - 4}" y2="{gy}" stroke="{COR["lilas"]}" stroke-width="1.2" opacity=".6"/>')
        out.append(f'<line x1="{x + 30}" y1="{y + 3}" x2="{x + 30}" y2="{y + h - 3}" stroke="{COR["pop"]}" stroke-width="1.5" opacity=".6"/>')
        for ry in range(y + 18, y + h - 10, 22):
            out.append(f'<circle cx="{x + 14}" cy="{ry}" r="4" fill="{COR["creme"]}" stroke="{COR["contorno"]}" stroke-width="2"/>')
    elif tipo == "envelope":
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{COR["contorno"]}" stroke-width="4"/>')
        out.append(f'<path d="M{x} {y} L{cx} {y + h * .4} L{x + w} {y}" fill="none" stroke="{COR["contorno"]}" stroke-width="3"/>')
        texto_y = y + h * .4 + 26
    else:  # postit / nota
        dobra = 26
        out.append(f'<path d="M{x} {y} H{x + w} V{y + h - dobra} L{x + w - dobra} {y + h} H{x} Z" fill="{fill}" stroke="{COR["contorno"]}" stroke-width="4" stroke-linejoin="round"/>')
        out.append(f'<path d="M{x + w} {y + h - dobra} H{x + w - dobra} V{y + h} Z" fill="{COR["contorno"]}" opacity=".25" stroke="{COR["contorno"]}" stroke-width="3" stroke-linejoin="round"/>')
        if tipo == "nota":
            out.append(f'<rect x="{cx - 34}" y="{y - 12}" width="68" height="24" fill="{COR["branco"]}" opacity=".85" stroke="{COR["contorno"]}" stroke-width="2" transform="rotate(-6 {cx} {y})"/>')
    tx = x + (40 if tipo == "folha" else 16)
    largura = w - (tx - x) - 16  # área útil para texto, com margem dos dois lados
    base = y + h - 12
    vazio_marcado = not cheio and tipo != "polaroid"

    # título: reduz o corpo até caber numa linha; se não couber, quebra
    tam_t = 19
    larg_t = largura - (34 if vazio_marcado else 0)  # o quadradinho fica à direita do título
    while tam_t > 15 and len(titulo) * LARG_TITULO * tam_t > larg_t:
        tam_t -= 1
    linhas_t = quebra(titulo, int(larg_t / (LARG_TITULO * tam_t)))
    for i, linha in enumerate(linhas_t):
        out.append(f'<text x="{tx}" y="{texto_y + i * tam_t * 1.15}" font-family="Fraunces, Georgia, serif" font-weight="700" font-size="{tam_t}" fill="{tinta}">{escape(linha)}</text>')
    topo = texto_y + (len(linhas_t) - 1) * tam_t * 1.15

    # texto: reduz o corpo até todas as linhas caberem na altura do cartão
    estilo = 'font-style="normal"' if cheio else 'font-style="italic" opacity=".75"'
    for tam in (14.5, 13.5, 12.5):
        passo = tam * 1.3
        linhas = quebra(pergunta, int(largura / (LARG_TEXTO * tam)))
        if topo + 6 + len(linhas) * passo <= base:
            break
    else:
        raise SystemExit(f"texto de '{cid}' não cabe no cartão. Encurte o texto ou aumente o cartão.")
    for i, linha in enumerate(linhas):
        out.append(f'<text x="{tx}" y="{topo + 6 + (i + 1) * passo:.1f}" font-family="Atkinson Hyperlegible Next, Arial, sans-serif" font-size="{tam}" {estilo} fill="{tinta}">{escape(linha)}</text>')
    if vazio_marcado:
        out.append(f'<rect x="{x + w - 40}" y="{texto_y - 19}" width="24" height="24" rx="6" fill="none" stroke="{tinta}" stroke-width="2" stroke-dasharray="4 3" opacity=".6"/>')
    out.append("</g>")
    return "\n".join(out)


def ancora(c):
    _, tipo, x, y, w, h, rot, *_ = c
    cx, cy = x + w / 2, y + h / 2
    px, py = cx, y + 6
    a = math.radians(rot)
    dx, dy = px - cx, py - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def logo_svg():
    svg = (ASSETS / "popkore-logo.svg").read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    corpo = svg[svg.index(">", svg.index("<svg")) + 1:svg.rindex("</svg>")]
    corpo = re.sub(r"<title>.*?</title>", "", corpo, flags=re.S).replace('id="sombra"', 'id="sombra-quadro"').replace("url(#sombra)", "url(#sombra-quadro)")
    return vb, corpo


def gerar():
    por_id = {c[0]: c for c in CARTOES}
    vb, paths = nome_paths()
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
              "<title>PopKore — quadro de evidências</title>",
              "<defs>",
              f'<pattern id="listras" width="56" height="56" patternUnits="userSpaceOnUse" patternTransform="rotate(-8)">'
              f'<rect width="28" height="56" fill="{COR["vermelho"]}"/><rect x="28" width="28" height="56" fill="{COR["branco"]}"/></pattern>',
              f'<pattern id="pontos" width="22" height="22" patternUnits="userSpaceOnUse">'
              f'<circle cx="4" cy="4" r="1.6" fill="{COR["contorno"]}" opacity=".08"/><circle cx="15" cy="13" r="1.2" fill="{COR["malva"]}" opacity=".12"/></pattern>',
              "</defs>",
              # moldura listrada como o balde de pipoca
              f'<rect x="0" y="0" width="{W}" height="{H}" rx="28" fill="url(#listras)"/>',
              f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" rx="26" fill="none" stroke="{COR["contorno"]}" stroke-width="8"/>',
              f'<rect x="34" y="34" width="{W - 68}" height="{H - 68}" rx="14" fill="{COR["creme"]}" stroke="{COR["contorno"]}" stroke-width="6"/>',
              f'<rect x="34" y="34" width="{W - 68}" height="{H - 68}" rx="14" fill="url(#pontos)"/>',
              ]
    # etiqueta com o nome
    partes.append(f'<g transform="rotate(-2 {W / 2} 64)"><rect x="{W / 2 - 170}" y="26" width="340" height="78" rx="18" fill="{COR["creme"]}" stroke="{COR["contorno"]}" stroke-width="5"/>'
                  f'<svg x="{W / 2 - 140}" y="36" width="280" height="58" viewBox="{vb}" preserveAspectRatio="xMidYMid meet">{paths}</svg></g>')
    partes.append(f'<text x="{W / 2}" y="132" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="20" fill="{COR["contorno"]}">quadro de evidências</text>')
    # rótulos dos grupos
    partes.append(f'<text x="70" y="118" font-family="Fraunces, Georgia, serif" font-weight="800" font-size="26" fill="{COR["vermelho"]}">Quem sou eu</text>')
    partes.append(f'<text x="{W - 70}" y="118" text-anchor="end" font-family="Fraunces, Georgia, serif" font-weight="800" font-size="26" fill="{COR["vermelho"]}">PopKore</text>')
    # fios por baixo dos cartões para não cobrir os textos; os pinos ficam por cima
    for a, b in FIOS:
        (x1, y1), (x2, y2) = ancora(por_id[a]), ancora(por_id[b])
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 18
        partes.append(f'<path d="M{x1} {y1} Q{mx} {my} {x2} {y2}" fill="none" stroke="{COR["vermelho"]}" stroke-width="3.2" stroke-linecap="round" opacity=".9"/>')
    for c in CARTOES:
        partes.append(cartao(c))
    for c in CARTOES:
        partes.append(pino(*ancora(c)))
    # cérebro caído, assinatura da logo
    partes.append(f'<g transform="translate({W - 120} {H - 92}) rotate(-12)"><ellipse cx="0" cy="0" rx="40" ry="28" fill="{COR["pessego"]}" stroke="{COR["contorno"]}" stroke-width="5"/>'
                  f'<path d="M-24 -6 q8 -14 18 -2 q8 -14 20 0 M-18 10 q10 -8 20 2 q8 -8 18 0" fill="none" stroke="{COR["contorno"]}" stroke-width="3" stroke-linecap="round"/>'
                  f'<path d="M14 18 q16 -2 24 -14 q4 14 -10 20 z" fill="{COR["malva"]}" stroke="{COR["contorno"]}" stroke-width="3"/></g>')
    partes.append("</svg>")
    SAIDA.write_text("\n".join(partes) + "\n", encoding="utf-8")
    cheios = sum(1 for c in CARTOES if c[-1])
    print(f"{SAIDA.relative_to(RAIZ)}: {cheios}/{len(CARTOES)} espaços preenchidos")


if __name__ == "__main__":
    gerar()
