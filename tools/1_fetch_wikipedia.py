# -*- coding: utf-8 -*-
"""Extrai as posições de chegada por corrida da tabela 'Driver standings' da Wikipédia."""
import re, json, unicodedata, pathlib, urllib.request, sys
AQUI = pathlib.Path(__file__).resolve().parent
UA = "IndyPointsStudy/1.0 (https://github.com/; research)"

def baixa(ano):
    """Guarda o wikitext da temporada em cache local."""
    destino = AQUI / f"{ano}_IndyCar_Series.wiki"
    if destino.exists():
        return destino
    url = f"https://en.wikipedia.org/w/index.php?title={ano}_IndyCar_Series&action=raw"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        destino.write_bytes(r.read())
    print(f"  baixado: {destino.name}", file=sys.stderr)
    return destino

def sec_standings(txt):
    m = re.search(r"={2,4}\s*Driver standings\s*={2,4}", txt)
    i = m.start()
    m2 = re.search(r"={2,4}\s*(Entrant|Manufacturer|Engine|Team)[^=]*={2,4}", txt[i+10:])
    j = i + 10 + m2.start() if m2 else len(txt)
    return txt[i:j]

def strip_markup(s):
    s = re.sub(r"<sup>.*?</sup>", "", s)
    s = re.sub(r"\{\{.*?\}\}", "", s)
    s = re.sub(r"'{2,}", "", s)
    s = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("{{","").replace("}}","").replace("|","")
    return s.strip()

def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()

def parse(path):
    txt = open(path, encoding="utf-8").read()
    sec = sec_standings(txt)
    k = sec.index('class="wikitable')
    k = sec.rindex("{|", 0, k)
    end = sec.index("\n|}", k)
    tbl = sec[k:end]
    linhas = tbl.split("\n")

    # ---- cabecalho: corridas (entre "!Driver" e "!Pts") ----
    corridas, dentro = [], False
    for ln in linhas:
        t = ln.strip()
        if not t.startswith("!"): continue
        conteudo = t[1:].strip()
        if re.match(r"^Driver\b", conteudo): dentro = True; continue
        if not dentro: continue
        if re.match(r"^(Pts|Points)\b", conteudo): break
        mc = re.search(r'colspan\s*=\s*"?(\d+)"?', conteudo)
        n = int(mc.group(1)) if mc else 1
        nome = strip_markup(re.sub(r'^\s*colspan\s*=\s*"?\d+"?\s*\|', "", conteudo))
        for x in range(n):
            corridas.append(nome + ("" if n == 1 else " " + str(x+1)))

    # ---- blocos de piloto ----
    blocos = re.split(r"\n\|-", "\n" + tbl)
    pilotos = []
    for b in blocos:
        m = re.search(r"^\|[^\n]*?(?:align=\"left\"|align:\s*left)[^\n]*?\|([^\n]*)$", b, re.M)
        if not m: continue
        nome = strip_markup(m.group(1))
        if not nome or nome.lower().startswith("driver"): continue
        corpo = b[m.end():]
        cels = []
        for ln in corpo.split("\n"):
            t = ln.strip()
            if not t.startswith("|") or t.startswith("|-"): continue
            v = t[1:]
            if "|" in v and re.match(r'^\s*(style|align|colspan|rowspan|class|bgcolor)', v):
                v = v.split("|", 1)[1]
            cels.append(strip_markup(v))
        res = []
        for c in cels[:len(corridas)]:
            mm = re.match(r"^(\d+)", c)
            res.append(int(mm.group(1)) if mm else None)
        while len(res) < len(corridas): res.append(None)
        pilotos.append((nome, res))
    return corridas, pilotos

if __name__ == "__main__":
    saida = {}
    for y in ["2021","2022","2023","2024","2025","2026"]:
        corridas, pil = parse(baixa(y))
        saida[y] = dict(corridas=corridas, pilotos={n: r for n, r in pil})
        print(f"{y}: {len(corridas)} corridas, {len(pil)} pilotos")
        print("   ", " ".join(corridas))
        n0, r0 = pil[0]
        print(f"    {n0}: {r0}")
    json.dump(saida, open(AQUI / "wiki_pos.json", "w", encoding="utf-8"), ensure_ascii=False)
