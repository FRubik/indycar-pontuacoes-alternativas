# -*- coding: utf-8 -*-
import json
import pathlib
AQUI = pathlib.Path(__file__).resolve().parent
D = json.load(open(AQUI / "dados2.json", encoding="utf-8"))
SIS = [
 dict(id="indy",nome="IndyCar, etapas iguais",curta="IndyCar",
      desc="A tabela de posições em vigor na IndyCar (50-40-35-32-30…), aplicada só pela posição de chegada, com todas as etapas valendo o mesmo. É a régua de comparação."),
 dict(id="f1",nome="Fórmula 1",curta="F1",
      desc="25-18-15-12-10-8-6-4-2-1. Só o top 10 pontua, e não há bônus de volta rápida (a F1 aboliu o ponto extra em 2025)."),
 dict(id="cart",nome="CART 1983–2003",curta="CART",
      desc="A tabela que a CART usou por 21 anos, antecessora direta da IndyCar atual: 20-16-14-12-10-8-6-5-4-3-2-1, pontuando até o 12º lugar."),
 dict(id="i500",nome="Indy 500 em dobro",curta="+Indy 500",
      desc="A tabela da IndyCar com as 500 Milhas valendo pontuação dobrada."),
 dict(id="final",nome="Última etapa em dobro",curta="+Final",
      desc="A tabela da IndyCar com a decisão do campeonato valendo o dobro, no espírito do finale da NASCAR."),
 dict(id="ambas",nome="Indy 500 e final em dobro",curta="+Ambas",
      desc="As duas etapas de maior apelo — a corrida mais importante do ano e a decisão do título — valendo o dobro."),
 dict(id="hib",nome="Híbrido, peso no oval",curta="Oval pesado",
      desc="Tabela da IndyCar nos ovais, pontuação da F1 nos circuitos mistos e de rua. Um oval passa a valer o dobro de um misto."),
 dict(id="hib2",nome="Híbrido, peso no misto",curta="Misto pesado",
      desc="O inverso: tabela da IndyCar nos circuitos mistos e de rua, pontuação da F1 nos ovais. Um misto passa a valer o dobro de um oval."),
 dict(id="i30",nome="Proposta “Indy 30”",curta="Indy 30",
      desc="Proposta própria: 30-22-18-15-13-11-10-9-8-7-6-5-4-3-2 e 1 ponto do 16º em diante, com a Indy 500 valendo 1,5×. Mantém o degrau íngreme da F1 no topo, mas continua pagando a cauda do grid."),
 dict(id="reta",nome="Curva reta",curta="Reta",
      desc="A mesma amplitude da tabela da IndyCar — 50 pontos ao vencedor, 5 ao vigésimo sexto — mas distribuída em linha reta, com cada posição valendo 1,8 ponto a mais que a seguinte. É o oposto de todas as outras: em vez de premiar mais a vitória, premia menos."),
]
def indy_tbl(p):
    t={1:50,2:40,3:35,4:32,5:30,6:28,7:26,8:24,9:22,10:20}
    return t[p] if p in t else (30-p if p<=25 else 5)
def f1_tbl(p): return {1:25,2:18,3:15,4:12,5:10,6:8,7:6,8:4,9:2,10:1}.get(p,0)
def reta_tbl(p):
    return round(50 - 45*(p-1)/25) if p <= 26 else 5
def cart_tbl(p):
    t={1:20,2:16,3:14,4:12,5:10,6:8,7:6,8:5,9:4,10:3,11:2,12:1}
    return t.get(p,0)
def i30_tbl(p):
    t={1:30,2:22,3:18,4:15,5:13,6:11,7:10,8:9,9:8,10:7,11:6,12:5,13:4,14:3,15:2}
    return t.get(p,1)

out=dict(sistemas=SIS,anos={},
  tabelas=dict(indy=[indy_tbl(p) for p in range(1,34)],
               f1=[f1_tbl(p) for p in range(1,34)],
               cart=[cart_tbl(p) for p in range(1,34)],
               reta=[reta_tbl(p) for p in range(1,34)],
               indy30=[i30_tbl(p) for p in range(1,34)]))
for ano,A in D.items():
    pil={}
    for p in A["pilotos"]:
        pil[p["driver"]]=dict(eq=p["equipe"],of=p["oficial"],ofp=p["oficial_pos"],
            s=p["sistemas"],v=p["vitorias"],pd=p["podios"],t10=p["top10"],
            i5=p["pos"][A["i500_idx"]],fi=p["pos"][A["final_idx"]])
    out["anos"][ano]=dict(rank=A["rank"],pilotos=pil,
        etapas=[dict(n=e["nome"],t=e["tipo"],
                     i5=(i==A["i500_idx"]),fin=(i==A["final_idx"]),
                     pend=(e["nome"] in A["pendentes"])) for i,e in enumerate(A["etapas"])],
        n_etapas=A["n_etapas"],n_disp=A["n_disputadas"],pendentes=A["pendentes"],
        n_ovais=A["n_ovais"],i500_round=A["i500_round"],final=A["final_nome"],
        final_real=A["final_real"],epoca=A["epoca"])
json.dump(out, open(AQUI / "slim2.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
print("slim2.json:", (AQUI / "slim2.json").stat().st_size, "bytes")
