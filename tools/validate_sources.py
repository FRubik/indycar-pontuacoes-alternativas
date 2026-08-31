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

RES = {}
print("VALIDAÇÃO — posição do arquivo vs posição da Wikipédia\n")
for f in sorted(glob.glob(os.path.join(DIR, "Indy*.txt"))):
    ano = re.search(r"\d{4}", f).group()
    txt = parse_txt(f)
    wk = W[ano]
    drop = set(DESCARTAR.get(ano, []))
    corridas = [c for i, c in enumerate(wk["corridas"]) if i not in drop]
    wpos = {}
    for nome, r in wk["pilotos"].items():
        wpos[sobrenome_wiki(nome)] = [v for i, v in enumerate(r) if i not in drop]

    # mapear colunas do txt -> indices de corrida da wiki
    # colunas do txt sao 1:1 com corridas, exceto as combinadas (2 corridas numa coluna)
    ncols = max(len(x["races"]) for x in txt)
    ok = falha = 0; problemas = []
    for x in txt:
        sn = sobrenome_txt(x["driver"])
        if sn not in wpos: problemas.append(f"  {ano}: piloto sem par na Wikipédia: {x['driver']}"); continue
        wr = wpos[sn]
        # alinhamento: percorre colunas do txt consumindo corridas da wiki
        ci = 0
        for col in range(ncols):
            if col >= len(x["races"]): break
            pts, pos = x["races"][col]
            if pos is not None:
                if ci < len(wr) and wr[ci] == pos: ok += 1
                else:
                    falha += 1
                    problemas.append(f"  {ano} {x['driver']} col{col+1}: txt P{pos} vs wiki P{wr[ci] if ci<len(wr) else '—'}")
                ci += 1
            else:
                ci += 1
    print(f"{ano}: {ok} posições conferem, {falha} divergem" + (" ✓" if falha == 0 else " ✗"))
    for p in problemas[:6]: print(p)
