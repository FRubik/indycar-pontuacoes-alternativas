# -*- coding: utf-8 -*-
import os, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
# Os .txt com os pontos oficiais não são versionados (ver README).
# Aponte INDY_DATA para a pasta que os contém, ou deixe-os na raiz do repositório.
DIR = pathlib.Path(os.environ.get("INDY_DATA", RAIZ))
import re, json, glob, os, unicodedata
W = json.load(open(AQUI / "wiki_pos.json", encoding="utf-8"))

# 2024: a coluna THE (Thermal $1 Million Challenge) nao valeu pontos de campeonato
DESCARTAR = {"2024": [1]}
ALIAS = {"veekay": "van kalmthout"}   # Wikipedia usa o nome de corrida; o arquivo, o legal

def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower().strip()

def sobrenome_wiki(n):
    n = re.sub(r"\s*\(.*?\)", "", n).strip()
    p = norm(n).split()
    for i, t in enumerate(p):
        if t in ("van","de","der","da"): return " ".join(p[i:])
    s = p[-1]
    return ALIAS.get(s, s)

def cell(c):
    c = c.strip()
    if c in ("-", ""): return (None, None)
    if "/" in c:
        a, b = c.split("/"); return (int(a), int(b))
    return (int(c), None)

def parse_txt(path):
    L = [l.rstrip("\n") for l in open(path, encoding="utf-8")]
    out, i = [], 1
    while i < len(L):
        if re.fullmatch(r"\d+", L[i].strip()):
            cells = [c.strip() for c in L[i+2].split("\t") if c.strip() != ""]
            nm = L[i+1].strip()
            m = re.search(r"([A-Z]\.\s+(?:[a-z]+\s+)*[A-Z][A-Za-z'\-]+)", nm)
            drv = re.sub(r"\s+", " ", m.group(1)) if m else nm
            eq = nm[m.end():].strip() if m else ""
            out.append(dict(pos=int(L[i].strip()), driver=drv, equipe=eq,
                            total=int(cells[0]), races=[cell(c) for c in cells[1:]]))
            i += 3
        else: i += 1
    return out

def sobrenome_txt(d):
    return norm(re.sub(r"^[A-Z]\.\s+", "", d))

print("VALIDAÇÃO — posições do .txt confrontadas com as da Wikipédia")
print("(uma coluna do .txt sem posição para nenhum piloto é um fim de semana de prova")
print(" dupla somado numa célula só, e cobre duas corridas da Wikipédia)\n")

total_ok = total_falha = 0
for f in sorted(glob.glob(os.path.join(DIR, "Indy*.txt"))):
    ano = re.search(r"\d{4}", f).group()
    txt = parse_txt(f)
    wk = W[ano]
    drop = set(DESCARTAR.get(ano, []))
    corridas = [c for i, c in enumerate(wk["corridas"]) if i not in drop]
    wpos = {sobrenome_wiki(n): [v for i, v in enumerate(r) if i not in drop]
            for n, r in wk["pilotos"].items()}

    ncols = max(len(x["races"]) for x in txt)
    # quantas corridas cada coluna do .txt cobre: 2 quando ninguém tem posição nela
    largura = []
    for c in range(ncols):
        tem_pos = any(c < len(x["races"]) and x["races"][c][1] is not None for x in txt)
        tem_pts = any(c < len(x["races"]) and x["races"][c][0] is not None for x in txt)
        largura.append(1 if tem_pos else (2 if tem_pts else 1))
    # índice da corrida da Wikipédia em que cada coluna começa
    inicio, acc = [], 0
    for w in largura:
        inicio.append(acc); acc += w

    ok = falha = 0
    problemas = []
    for x in txt:
        sn = sobrenome_txt(x["driver"])
        if sn not in wpos:
            problemas.append(f"    {x['driver']}: sem par na Wikipédia")
            continue
        wr = wpos[sn]
        for c in range(min(ncols, len(x["races"]))):
            if largura[c] != 1:      # coluna combinada: não há posição para comparar
                continue
            pos = x["races"][c][1]
            if pos is None:
                continue
            i = inicio[c]
            esperado = wr[i] if i < len(wr) else None
            if esperado == pos:
                ok += 1
            else:
                falha += 1
                problemas.append(f"    {x['driver']} col{c+1} ({corridas[i]}): "
                                 f".txt P{pos} vs Wikipédia P{esperado}")
    total_ok += ok; total_falha += falha
    comb = [i+1 for i, w in enumerate(largura) if w == 2]
    print(f"  {ano}: {ok} conferem, {falha} divergem"
          + (f" · colunas duplas: {comb}" if comb else "")
          + ("  ✓" if falha == 0 else "  ✗"))
    for pr in problemas[:5]:
        print(pr)

print(f"\n  TOTAL: {total_ok} posições conferem, {total_falha} divergem "
      f"({total_ok/(total_ok+total_falha)*100:.2f}% de acordo)")
print("\n  As divergências conhecidas são casos de não-largada em que o .txt atribui uma")
print("  posição e a Wikipédia deixa a célula vazia. A Wikipédia é a fonte usada na página.")
