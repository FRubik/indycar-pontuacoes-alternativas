# -*- coding: utf-8 -*-
"""Confere os .txt (pontos oficiais) contra as posições extraídas da Wikipédia.

O alinhamento entre as colunas do .txt e as corridas da Wikipédia não pode ser posicional:
ao copiar a tabela perdem-se os `colspan` dos fins de semana de prova dupla, e alguns
arquivos estão na ordem cronológica original, não na ordem em que a Wikipédia lista as
provas remarcadas. Cada coluna é, portanto, casada com a corrida que ela mais explica.
"""
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
print("(cada coluna do .txt é casada com a corrida da Wikipédia que ela mais explica;")
print(" uma coluna sem posição nenhuma é um fim de semana de prova dupla somado numa célula só)\n")

total_ok = total_falha = 0
alertas = []
for f in sorted(glob.glob(os.path.join(DIR, "Indy*.txt"))):
    ano = re.search(r"\d{4}", f).group()
    txt = parse_txt(f)
    wk = W[ano]
    drop = set(DESCARTAR.get(ano, []))
    corridas = [c for i, c in enumerate(wk["corridas"]) if i not in drop]
    wpos = {sobrenome_wiki(n): [v for i, v in enumerate(r) if i not in drop]
            for n, r in wk["pilotos"].items()}

    pares = [(x, wpos[sobrenome_txt(x["driver"])]) for x in txt
             if sobrenome_txt(x["driver"]) in wpos]
    sem_par = [x["driver"] for x in txt if sobrenome_txt(x["driver"]) not in wpos]
    ncols = max(len(x["races"]) for x in txt)

    def confronto(c, i):
        """Quantas posições batem e quantas divergem entre a coluna c e a corrida i."""
        ok = falha = 0
        for x, wr in pares:
            p = x["races"][c][1] if c < len(x["races"]) else None
            if p is None: continue
            if wr[i] == p: ok += 1
            else: falha += 1
        return ok, falha

    # cada coluna com posições vai para a corrida que ela melhor explica; sem posição
    # nenhuma, a coluna é uma prova dupla somada (se tem pontos) ou está vazia
    mapa, duplas, vazias = {}, [], []
    for c in range(ncols):
        tem = lambda k: any(c < len(x["races"]) and x["races"][c][k] is not None for x, _ in pares)
        if not tem(1):
            (duplas if tem(0) else vazias).append(c); continue
        mapa[c] = max(range(len(corridas)), key=lambda i: confronto(c, i)[0])

    ok = falha = 0
    problemas = []
    for c, i in sorted(mapa.items()):
        for x, wr in pares:
            p = x["races"][c][1] if c < len(x["races"]) else None
            if p is None: continue
            if wr[i] == p: ok += 1
            else:
                falha += 1
                problemas.append(f"    {x['driver']} col{c+1} ({corridas[i]}): "
                                 f".txt P{p} vs Wikipédia P{wr[i]}")
    total_ok += ok; total_falha += falha

    # estrutura: colunas duplas, corridas ausentes e soma dos pontos
    cobertas = set(mapa.values())
    livres = [i for i in range(len(corridas)) if i not in cobertas]
    # cada coluna dupla cobre duas corridas; o que sobrar não veio no arquivo
    corrida_vazia = lambda i: all(wr[i] is None for _, wr in pares)   # ainda não disputada
    ausentes = [i for i in livres[2*len(duplas):] if not corrida_vazia(i)]
    soma_ruim = sum(1 for x in txt
                    if sum(p for p, _ in x["races"] if p is not None) != x["total"])

    est = []
    if duplas:   est.append(f"colunas duplas: {[c+1 for c in duplas]}")
    if vazias:   est.append(f"colunas vazias: {[c+1 for c in vazias]}")
    if ausentes: est.append("AUSENTES no .txt: " + ", ".join(corridas[i] for i in ausentes))
    if soma_ruim: est.append(f"soma ≠ total em {soma_ruim} de {len(txt)} pilotos")
    if sem_par:  est.append(f"sem par na Wikipédia: {sem_par}")
    fora_de_ordem = sorted(mapa) != [c for c, _ in sorted(mapa.items(), key=lambda kv: kv[1])]
    if fora_de_ordem: est.append("colunas fora da ordem da Wikipédia")

    print(f"  {ano}: {ok} conferem, {falha} divergem" + ("  ✓" if falha == 0 else "  ✗")
          + ("".join("\n         · " + e for e in est)))
    for pr in problemas[:5]:
        print(pr)
    if ausentes or soma_ruim:
        alertas.append(ano)

print(f"\n  TOTAL: {total_ok} posições conferem, {total_falha} divergem "
      f"({total_ok/(total_ok+total_falha)*100:.2f}% de acordo)")
print("\n  As divergências conhecidas são casos de não-largada em que o .txt atribui uma")
print("  posição e a Wikipédia deixa a célula vazia. A Wikipédia é a fonte usada na página,")
print("  então nada disso afeta os cálculos: do .txt vêm só o total e a classificação oficial.")
if alertas:
    print(f"\n  ATENÇÃO — arquivo incompleto em: {', '.join(alertas)}. Os totais oficiais continuam")
    print("  corretos (é o que a página usa do .txt), mas a soma das colunas não fecha com eles.")
