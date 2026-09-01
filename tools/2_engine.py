# -*- coding: utf-8 -*-
import os, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
# Os .txt com os pontos oficiais não são versionados (ver README).
# Aponte INDY_DATA para a pasta que os contém, ou deixe-os na raiz do repositório.
DIR = pathlib.Path(os.environ.get("INDY_DATA", RAIZ))
import re, json, glob, os, unicodedata
W = json.load(open(AQUI / "wiki_pos.json", encoding="utf-8"))
DESCARTAR = {"2024": [1]}          # Thermal 2024: evento sem pontos de campeonato
ALIAS = {"veekay": "van kalmthout"}
# Multiplicadores que a IndyCar realmente aplicou. De 2015 a 2019 a Indy 500 e a última
# etapa valiam dobro; de 2020 a 2022 só a Indy 500; de 2023 em diante, nenhum.
def regra_epoca(ano):
    if ano <= 2019: return "ambas"
    if ano <= 2022: return "i500"
    return ""

PISTAS = {
 "BAR":("Barber","road"), "STP":("St. Petersburg","street"), "TMS":("Texas","oval"),
 "IGP":("GP de Indianápolis","road"), "INDY":("Indy 500","oval"),
 "BEL":("Detroit (Belle Isle)","street"), "DET":("Detroit","street"),
 "ROA":("Road America","road"), "MOH":("Mid-Ohio","road"),
 "NSC":("Nashville (rua)","street"), "NSS":("Nashville Superspeedway","oval"),
 "GTW":("Gateway","oval"), "POR":("Portland","road"), "LAG":("Laguna Seca","road"),
 "LBH":("Long Beach","street"), "TOR":("Toronto","street"), "IOW":("Iowa","oval"),
 "THE":("Thermal Club","road"), "MIL":("Milwaukee","oval"), "PHX":("Phoenix","oval"),
 "ARL":("Arlington","street"), "MRK":("Markham","street"), "D.C.":("Washington D.C.","street"),
 "POC":("Pocono","oval"), "WGL":("Watkins Glen","road"), "SON":("Sonoma","road"),
 "IMS":("GP de Indianápolis","road"), "COA":("Circuit of the Americas","road"),
}
def pista(sig):
    m = re.match(r"^([A-Z.]+?)(\d*)\s*(\d*)$", sig.strip())
    base, n1, n2 = m.group(1), m.group(2), m.group(3)
    nome, tipo = PISTAS[base]
    suf = n2 or ""
    return (nome + (" " + suf if suf else ""), tipo)

def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower().strip()
def sob_wiki(n):
    n = re.sub(r"\s*\(.*?\)", "", n).strip()
    p = norm(n).split()
    for i, t in enumerate(p):
        if t in ("van","de","der","da"): return " ".join(p[i:])
    return ALIAS.get(p[-1], p[-1])
def sob_txt(d): return norm(re.sub(r"^[A-Z]\.\s+", "", d))

def cell(c):
    c = c.strip()
    if c in ("-",""): return (None, None)
    if "/" in c:
        a,b = c.split("/"); return (int(a), int(b))
    return (int(c), None)
def parse_txt(path):
    L=[l.rstrip("\n") for l in open(path,encoding="utf-8")]; out=[]; i=1
    while i<len(L):
        if re.fullmatch(r"\d+",L[i].strip()):
            cells=[c.strip() for c in L[i+2].split("\t") if c.strip()!=""]
            nm=L[i+1].strip()
            m=re.search(r"([A-Z]\.\s+(?:[a-z]+\s+)*[A-Z][A-Za-z'\-]+)",nm)
            out.append(dict(pos=int(L[i].strip()),
                            driver=re.sub(r"\s+"," ",m.group(1)) if m else nm,
                            equipe=nm[m.end():].strip() if m else "",
                            total=int(cells[0]), races=[cell(c) for c in cells[1:]]))
            i+=3
        else: i+=1
    return out

# ---------------- tabelas de pontuação ----------------
def indy_tbl(p):
    t={1:50,2:40,3:35,4:32,5:30,6:28,7:26,8:24,9:22,10:20}
    if p in t: return t[p]
    return 30-p if p<=25 else 5
def f1_tbl(p):   return {1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}.get(p,0)
def cart_tbl(p):
    # CART 1983-2003
    t={1:20,2:16,3:14,4:12,5:10,6:8,7:6,8:5,9:4,10:3,11:2,12:1}
    return t.get(p,0)
def i30_tbl(p):
    t={1:30,2:22,3:18,4:15,5:13,6:11,7:10,8:9,9:8,10:7,11:6,12:5,13:4,14:3,15:2}
    return t.get(p,1)
def reta_tbl(p):
    # mesma amplitude da tabela da IndyCar (50 no 1º, 5 no 26º), distribuída em linha reta
    return round(50 - 45*(p-1)/25) if p <= 26 else 5
TBL={"indy":indy_tbl,"reta":reta_tbl,"f1":f1_tbl,"indy30":i30_tbl,"cart":cart_tbl}

SISTEMAS=[
 dict(id="indy",nome="IndyCar, etapas iguais",curta="IndyCar",tbl="indy",x2=[],base=True),
 dict(id="f1",nome="Fórmula 1",curta="F1",tbl="f1",x2=[]),
 dict(id="cart",nome="CART 1983-2003",curta="CART",tbl="cart",x2=[]),
 dict(id="i500",nome="Indy 500 em dobro",curta="+Indy 500",tbl="indy",x2=["i500"]),
 dict(id="final",nome="Última etapa em dobro",curta="+Final",tbl="indy",x2=["final"]),
 dict(id="ambas",nome="Indy 500 e final em dobro",curta="+Ambas",tbl="indy",x2=["i500","final"]),
 dict(id="hib",nome="Híbrido, peso no oval",curta="Oval pesado",tbl="hibrido",x2=[]),
 dict(id="hib2",nome="Híbrido, peso no misto",curta="Misto pesado",tbl="hibrido2",x2=[]),
 dict(id="i30",nome="Proposta “Indy 30”",curta="Indy 30",tbl="indy30",x2=["i500_15"]),
 dict(id="reta",nome="Curva reta",curta="Reta",tbl="reta",x2=[]),
]
def pts(tbl,pos,tipo):
    if tbl=="hibrido":  return indy_tbl(pos) if tipo=="oval" else f1_tbl(pos)
    if tbl=="hibrido2": return f1_tbl(pos)   if tipo=="oval" else indy_tbl(pos)
    return TBL[tbl](pos)

# ---------------- montagem ----------------
DADOS={}; relat=[]
arquivos = sorted(glob.glob(os.path.join(DIR, "Indy*.txt")))
assert arquivos, f"nenhum Indy*.txt encontrado em {DIR} (ver README)"
for f in arquivos:
    ano=re.search(r"\d{4}",f).group(); ai=int(ano)
    txt=parse_txt(f); wk=W[ano]; drop=set(DESCARTAR.get(ano,[]))
    sigs=[c for i,c in enumerate(wk["corridas"]) if i not in drop]
    etapas=[]
    for i,s in enumerate(sigs):
        n,t=pista(s); etapas.append(dict(r=i+1,nome=n,tipo=t,sig=s))
    wpos={sob_wiki(n):[v for i,v in enumerate(r) if i not in drop] for n,r in wk["pilotos"].items()}

    # posições: a Wikipédia é a fonte única (validada contra o .txt em 1698 de 1700 células).
    # O .txt entra só com o total de pontos oficial e a classificação oficial da temporada.
    pilotos = []; sem_par = []
    for x in txt:
        sn = sob_txt(x["driver"])
        if sn not in wpos: sem_par.append(x["driver"])
        wr = list(wpos.get(sn, [None]*len(etapas)))
        pilotos.append(dict(driver=x["driver"], equipe=x["equipe"], oficial=x["total"],
                            oficial_pos=x["pos"], pos=wr))
    relat.append(f"{ano}: {len(etapas)} etapas, {len(pilotos)} pilotos" +
                 (f"  SEM PAR: {sem_par}" if sem_par else ""))

    idx_i500=next(i for i,e in enumerate(etapas) if e["nome"]=="Indy 500")
    disputadas=[i for i,_ in enumerate(etapas) if any(p["pos"][i] is not None for p in pilotos)]
    idx_final=max(disputadas)
    pendentes=[etapas[i]["nome"] for i in range(len(etapas)) if i not in disputadas]

    for p in pilotos:
        p["sistemas"]={}
        posv=[v for v in p["pos"] if v is not None]
        p["vitorias"]=sum(1 for v in posv if v==1); p["podios"]=sum(1 for v in posv if v<=3)
        p["top10"]=sum(1 for v in posv if v<=10); p["cont"]=sorted(posv)
        for S in SISTEMAS:
            tot=0
            for i,e in enumerate(etapas):
                v=p["pos"][i]
                if v is None: continue
                base=pts(S["tbl"],v,e["tipo"]); mult=1.0
                if "i500" in S["x2"] and i==idx_i500: mult=2.0
                if "i500_15" in S["x2"] and i==idx_i500: mult=1.5
                if "final" in S["x2"] and i==idx_final: mult=2.0
                tot+=int(base*mult)
            p["sistemas"][S["id"]]=tot

    def chave(pl,sid):
        c={}
        for v in pl["cont"]: c[v]=c.get(v,0)+1
        return (-pl["sistemas"][sid],[-c.get(k,0) for k in range(1,34)],pl["driver"])
    rank={S["id"]:[p["driver"] for p in sorted(pilotos,key=lambda q:chave(q,S["id"]))] for S in SISTEMAS}
    rank["oficial"]=[p["driver"] for p in sorted(pilotos,key=lambda q:q["oficial_pos"])]

    DADOS[ano]=dict(etapas=etapas,pilotos=pilotos,rank=rank,
        n_etapas=len(etapas),n_disputadas=len(disputadas),pendentes=pendentes,
        i500_idx=idx_i500,i500_round=idx_i500+1,final_nome=etapas[idx_final]["nome"],
        final_idx=idx_final,final_real=(idx_final==len(etapas)-1),
        n_ovais=sum(1 for e in etapas if e["tipo"]=="oval"),
        epoca=regra_epoca(ai))

print("\n".join(relat))
print()
for ano,A in DADOS.items():
    camps={S["curta"]:A["rank"][S["id"]][0] for S in SISTEMAS}
    dif=set(camps.values())
    ep = {"ambas":"Indy 500 e final DOBRADAS na época","i500":"Indy 500 DOBRADA na época",
          "":"sem multiplicador na época"}[A["epoca"]]
    print(f"{ano} ({A['n_disputadas']}/{A['n_etapas']} etapas, {A['n_ovais']} ovais, {ep}) "
          f"campeões: {dif if len(dif)>1 else list(dif)[0]}")
    for S in SISTEMAS:
        print(f"   {S['curta']:<11} " + ", ".join(f"{i+1}.{d.split('. ')[-1]}" for i,d in enumerate(A['rank'][S['id']][:5])))
json.dump(DADOS, open(AQUI / "dados2.json", "w", encoding="utf-8"), ensure_ascii=False)
