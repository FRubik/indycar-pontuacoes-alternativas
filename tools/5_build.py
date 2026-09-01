# -*- coding: utf-8 -*-
import json

ANALISES = {
"2016": """
<p><span class="drv">Pagenaud</span> vence as dez réguas com folga — cinco vitórias, oito pódios e doze top 10 em
dezesseis provas não deixam brecha para tabela nenhuma. O interesse de 2016 está inteiramente atrás dele, e é o
mais extremo da página.</p>
<p>Era o regime dos dois multiplicadores: Indy 500 <em>e</em> final valendo dobro. Pagenaud fechou o ano vencendo
Sonoma, a decisão, e embolsou 104 pontos numa corrida só. A régua base mostra o ano sem isso, e o efeito é pequeno
no topo: <span class="drv">Power</span> é vice nas dez.</p>
<p>Aí entra a <strong>curva reta</strong>, e 2016 vira outra temporada. Power, com <strong>quatro vitórias e sete
pódios</strong>, <strong>cai do segundo para o sexto lugar</strong> — atrás de <span class="drv">Castroneves</span>,
que não venceu nenhuma corrida, de <span class="drv">Kanaan</span>, que também não, e de
<span class="drv">Kimball</span>, que não subiu ao pódio uma vez sequer no ano. É a maior queda de um vice-campeão em
toda a página, e o argumento mais forte contra achatar a curva: quando o segundo lugar vale 96% de uma vitória, o
campeonato passa a ser uma contagem de chegadas, e vencer quatro corridas rende menos que terminar onze delas em
qualquer lugar do top 10.</p>
""",
"2017": """
<p><strong>A curva reta troca o campeão.</strong> <span class="drv">Newgarden</span> venceu 2017 com quatro vitórias,
nove pódios e treze top 10, e é campeão em nove das dez réguas. Na décima — a mais achatada — ele cai para
<strong>terceiro</strong>, e o título vai para <span class="drv">Pagenaud</span>, que venceu duas corridas mas
terminou <strong>quinze</strong> das dezessete no top 10.</p>
<p>Entre os dois passa <span class="drv">Dixon</span>, com uma vitória e dezesseis top 10 — a temporada mais regular
do ano. A ordem Pagenaud, Dixon, Newgarden na curva reta é o inverso exato da ordem por vitórias, e a distância entre
eles é pequena: 720, 699 e 694. É a mesma mecânica de 2016, só que aqui ela chega ao topo da tabela.</p>
<p>Nas outras nove réguas 2017 é estável, e o pouco que se move é a dobra da Indy 500. Castroneves foi
<strong>segundo</strong> em Indianápolis e Dixon, <strong>trigésimo segundo</strong> — abandonou depois do acidente
com Bourdais. Com o multiplicador da época, Castroneves sobe ao quarto lugar e Power cai ao quinto; sem ele, a ordem
se inverte. Nos pontos oficiais o efeito é ainda mais direto: tirar a dobra
não muda o campeão, mas <strong>troca o vice</strong> — Dixon passa Pagenaud, e a vantagem de Newgarden sobre o
segundo colocado cai de 13 para 7 pontos.</p>
""",
"2018": """
<p><strong>Dois pontos.</strong> É a diferença entre <span class="drv">Rossi</span> e <span class="drv">Dixon</span>
na régua base — 539 a 537, o campeonato mais apertado das onze temporadas — e é por isso que 2018 é o ano em que
<em>tudo</em> depende da régua.</p>
<p>Com todas as etapas valendo o mesmo, Rossi é campeão: três vitórias contra duas, oito pódios cada, catorze top 10
cada. Em <strong>oito das outras nove réguas</strong> o título é de Dixon. A única que acompanha a base é a curva
reta, e pela razão de sempre — quanto mais achatada a curva, mais pesam as três vitórias de Rossi.</p>
<p>O que separa os dois é o regulamento da época, que dobrava a Indy 500 e a final. Dixon foi terceiro em
Indianápolis e segundo em Sonoma; Rossi, quarto e sétimo. Nas duas provas multiplicadas Dixon ganha o suficiente para
inverter a diferença de dois pontos numa vantagem de quinze. <strong>É o caso mais limpo da página de um multiplicador
decidindo um campeonato</strong> — com uma ressalva importante: no mundo real Dixon venceu por 57 pontos, porque as
réguas daqui ignoram pole e voltas lideradas, e nessas ele fez 42 pontos a mais que Rossi. Tirar só a dobra dos pontos
oficiais ainda deixa Dixon quarenta à frente. O multiplicador não decidiu 2018; o que decidiu foram os bônus que ele
ampliava.</p>
<p>Mais atrás, o padrão é o de sempre: <span class="drv">Newgarden</span>, com três vitórias e apenas três pódios,
é terceiro na régua base e <strong>quinto</strong> em quase todas as outras; <span class="drv">Power</span>, com três
vitórias e oito pódios, faz o caminho contrário.</p>
""",
"2019": """
<p>A temporada mais indecisa da página: <strong>três pilotos em quatro pontos</strong> na régua base —
<span class="drv">Dixon</span> 515, <span class="drv">Newgarden</span> 513, <span class="drv">Pagenaud</span> 511 — e
<strong>três campeões diferentes</strong> conforme a régua. Nenhum outro ano produz isso.</p>
<p>Com as etapas iguais o título é de Dixon, que fez <strong>dez pódios</strong> em dezessete provas, mais que
qualquer um. Com os multiplicadores da época — Indy 500 e final em dobro — é de <span class="drv">Pagenaud</span>,
que <strong>venceu as 500 Milhas</strong> e foi quarto em Laguna Seca. Com peso nos ovais, ou pela proposta Indy 30, é
de <span class="drv">Newgarden</span>, que foi quem realmente levou o troféu.</p>
<p>Esse último ponto merece atenção, porque é o único lugar da página em que a régua da época <em>não</em> reproduz o
campeão real. Newgarden venceu 2019 com 641 pontos contra 616 de Pagenaud, e a diferença está inteira nos bônus que
estas réguas não pagam: 72 pontos de pole e voltas lideradas para Newgarden, 23 para Pagenaud. Contando só a posição
de chegada, o ano era de Pagenaud.</p>
<p>Abaixo do trio, <span class="drv">Rossi</span> é quarto em todas as dez, e na régua da época empata com Dixon em
563 — mais um lugar decidido no desempate. 2019 é a temporada que melhor mostra o argumento inteiro da página: quando
o ano é apertado, a régua não é um detalhe de regulamento, é o resultado.</p>
""",
"2020": """
<p>A temporada da pandemia: <strong>catorze provas</strong>, a mais curta do conjunto, seis delas em oval e cinco fins
de semana de prova dupla. <span class="drv">Dixon</span> venceu as três primeiras e é campeão nas dez réguas, com
quatro vitórias, sete pódios e treze top 10 em catorze corridas — 479 a 423 sobre <span class="drv">Newgarden</span>
na régua base. Não há régua nesta página que alcance isso.</p>
<p>E ainda assim <strong>2020 é o ano em que a dobra da Indy 500 chegou mais perto de decidir um campeonato</strong> —
não nas réguas daqui, mas nos pontos oficiais. Dixon foi <em>segundo</em> em Indianápolis e Newgarden, quinto; com os
bônus de pole e voltas lideradas somados, a vantagem oficial de Dixon foi de 16 pontos. Tirando só a parte dobrada,
ela cai para <strong>seis</strong>. É a menor margem em sete temporadas de multiplicador, e a melhor medida de quão
perto a regra passou de contradizer o argumento com que foi abolida.</p>
<p>Atrás dos dois, a régua reordena como sempre. <span class="drv">O'Ward</span> é terceiro em <strong>oito das dez
réguas</strong> <em>sem vencer nenhuma corrida</em> — quatro pódios e dez top 10 —, e cai para quarto só nas duas em
que a tabela da F1 vale nos mistos: ali <span class="drv">Power</span> assume, com duas vitórias e cinco pódios em
apenas sete top 10, o perfil exatamente oposto. E <span class="drv">Herta</span>, <em>terceiro</em> na classificação
oficial, é sétimo na régua base e não passa do quinto em régua nenhuma: boa parte dos 421 pontos dele em 2020 veio de
poles e voltas lideradas, que nenhuma régua daqui paga.</p>
""",
"2021": """
<p><span class="drv">Palou</span> é campeão nas dez réguas, com folga em todas. Abaixo dele, porém, 2021 é o melhor
laboratório da coleção para uma pergunta específica: <em>o que a dobra da Indy 500 fazia?</em></p>
<p>A regra estava em vigor — a final já tinha voltado ao peso normal em 2020 —, então a coluna
<strong>+Indy 500</strong> é o sistema real da época e a régua base mostra o ano sem ela. Tirar a dobra troca o terceiro lugar: <span class="drv">O'Ward</span>, que foi quarto nas 500 Milhas, cai
para quarto no campeonato, e <span class="drv">Dixon</span> — décimo sétimo em Indianápolis — sobe a terceiro. Mais
atrás, <span class="drv">Ericsson</span> sai do top 5 e <span class="drv">Herta</span> entra. Nenhum título em jogo,
duas posições trocadas.</p>
<p>Trocar a curva inteira faz menos diferença que isso. A pontuação da F1 devolve exatamente o top 5 oficial da
temporada — Palou, Newgarden, O'Ward, Dixon, Herta — e a proposta Indy 30 chega ao mesmo resultado. Só a régua da
final em dobro reordena de verdade: Herta venceu Long Beach, a decisão do ano, e sobe de quinto para quarto, enquanto
O'Ward, que abandonou ali, cai para quinto.</p>
<p>Mas é indo na direção <em>oposta</em> que 2021 revela o quanto foi apertado. Com a <strong>curva reta</strong>, a
mais achatada da página, Palou e <span class="drv">Newgarden</span> terminam <strong>empatados em 619 pontos</strong> —
o título só se decide no critério de desempate, pelas três vitórias de Palou contra duas. É o resultado mais apertado
de todo o conjunto, e a explicação está nos piores resultados de cada um: a metade fraca da temporada de Palou inclui
um 27º, um 20º e um 17º lugar; a de Newgarden não passa de um 23º. Numa curva rasa, as vitórias de Palou valem pouco e
os desastres dele custam caro.</p>
""",
"2022": """
<p>O ano em que a régua deveria importar e não importou. <span class="drv">Power</span> foi campeão com <em>uma</em>
vitória, contra cinco de <span class="drv">Newgarden</span> e três de <span class="drv">McLaughlin</span> — exatamente
o perfil de campeão que se acusa a tabela achatada da IndyCar de fabricar. E ele vence nas dez réguas, inclusive na da
F1, porque a regularidade dele não era de décimos lugares: foram <strong>nove pódios em dezessete provas</strong>. A
pontuação da F1 pune o sétimo lugar, não o segundo.</p>
<p>A dobra da Indy 500 ainda valia, e 2022 mostra o maior efeito dela nas onze temporadas. <span class="drv">Ericsson</span>
venceu as 500 Milhas; com a regra da época ele é quarto no campeonato, e <strong>sem a dobra cai para sexto</strong> —
duas posições que dependiam de uma corrida só. <span class="drv">McLaughlin</span> e <span class="drv">Palou</span>
sobem no lugar dele.</p>
<p>Os outros movimentos são os de sempre. McLaughlin passa Dixon pela terceira colocação nas réguas mais íngremes —
três vitórias e sete pódios contra duas e quatro — e, na régua com peso no misto, chega a tomar o vice de
<span class="drv">Newgarden</span>. E Palou salta de quinto para terceiro quando a final vale dobrado, porque venceu
Laguna Seca.</p>
<p>O contraste mais duro vem da <strong>curva reta</strong>. Newgarden, com cinco vitórias, <strong>despenca do segundo
para o quinto lugar</strong> — a maior queda de um vice em toda a página — e quem herda o posto é
<span class="drv">Dixon</span>, com duas vitórias e quinze top 10 em dezessete provas. Quando vencer deixa de valer
muito mais que chegar em quarto, o campeonato passa a ser de quem termina, não de quem ganha.</p>
""",
"2023": """
<p>Primeira temporada sem a dobra da Indy 500, e a primeira em que a coluna <strong>+Indy 500</strong> deixa de ser
história para virar proposta. Reintroduzir o multiplicador promoveria <span class="drv">Newgarden</span>, vencedor das
500 Milhas, de quinto a terceiro — mas não chega perto do título.</p>
<p>Título e vice estão fechados em qualquer régua: <span class="drv">Palou</span> com cinco vitórias e dez pódios em
dezessete provas, <span class="drv">Dixon</span> em segundo nas dez. A disputa é pelo terceiro lugar, e ela é
inteiramente uma questão de tabela.</p>
<p><span class="drv">McLaughlin</span> somou uma vitória, quatro pódios e catorze top 10. Newgarden somou quatro
vitórias, cinco pódios e apenas onze top 10. Na tabela da IndyCar o primeiro é terceiro e o segundo é quinto; na F1, no
híbrido e na Indy 30 a ordem se inverte exatamente. É o caso mais limpo do conjunto: as mesmas duas temporadas produzem
posições opostas conforme se pague pela vitória ou pela presença.</p>
<p>E há um terceiro nome nessa disputa. As três tabelas que realmente existiram dão <strong>três pódios
diferentes</strong>: pela IndyCar o terceiro lugar é de McLaughlin, pela F1 é de Newgarden e pela CART é de
<span class="drv">O'Ward</span> — que não venceu nenhuma corrida no ano, mas fez sete pódios. A tabela da CART paga o
pódio como a IndyCar e corta o meio do pelotão como a F1, e essa combinação favorece exatamente o piloto que sobe muito
ao pódio sem ganhar.</p>
""",
"2024": """
<p><strong>O único ano em que o troféu troca de mãos — e troca duas vezes.</strong></p>
<p>Com a <strong>última etapa valendo o dobro</strong>, <span class="drv">Herta</span> é campeão. Ele venceu Nashville,
a decisão da temporada, com Palou em décimo primeiro. Os 27 pontos que separavam os dois na régua base viram uma
vantagem de quatro pontos para Herta. Foi o ano mais equilibrado do período — cinco pilotos entre 524 e 449 pontos,
todos com duas ou três vitórias — e num campeonato assim qualquer multiplicador colocado na etapa certa decide.</p>
<p>No <strong>híbrido com peso no oval</strong>, <span class="drv">McLaughlin</span> é campeão. 2024 teve sete ovais
em dezessete provas, o calendário mais oval do conjunto. Pagar os ovais pela tabela cheia da IndyCar e os mistos pela
tabela da F1 dobra o peso relativo de um oval, e McLaughlin venceu em Iowa e em Milwaukee enquanto Palou construía o
título dele nos circuitos mistos. É a única régua que muda um campeão sem usar multiplicador nenhum — ela não mexe na
curva de pontos, mexe no calendário.</p>
<p>Inverta o híbrido e o mesmo McLaughlin <strong>despenca para quinto</strong>. É o maior deslocamento de um piloto
entre duas réguas em toda a página, e a melhor medida do quanto 2024 foi uma temporada de especialistas: com peso no
misto quem sobe é <span class="drv">Power</span>, que vai a vice. Nenhum dos dois híbridos é proposta séria de
regulamento — mas juntos mostram que o campeonato de 2024 foi decidido tanto pelo calendário quanto pelos pilotos.</p>
<p>E aqui está o melhor argumento contra multiplicadores: <strong>dobrar as duas etapas devolve o título a Palou</strong>.
Ele foi quinto na Indy 500 e Herta, vigésimo terceiro; os dois multiplicadores se cancelam. Quando o campeão depende de
qual prova alguém decidiu privilegiar, o multiplicador está decidindo mais do que a temporada.</p>
""",
"2025": """
<p>Oito vitórias em dezessete provas. Nenhuma das dez réguas chega perto de ameaçar <span class="drv">Palou</span> — e todas
apenas <em>ampliam</em> o que já era uma temporada desproporcional: a vantagem sobre <span class="drv">O'Ward</span>
passa de 37% na régua base para 72% na pontuação da F1. Curvas mais íngremes não criam campeões novos, engrandecem o
que já existe.</p>
<p>O top 5 tem sempre os mesmos cinco nomes, com <span class="drv">Dixon</span> e <span class="drv">Lundgaard</span>
alternando o terceiro e o quinto lugar. Vale reparar que Lundgaard sobe <em>sem ter vencido nenhuma corrida</em>: são
seis pódios contra três de Dixon. Não é a vitória que a tabela da F1 premia — é o pódio. Entre o primeiro e o segundo
lugar vão sete pontos; entre o terceiro e o oitavo, onze.</p>
<p>Reintroduzir a dobra da Indy 500 também favoreceria Lundgaard, sétimo em Indianápolis, contra um Kirkwood que bateu
e terminou em trigésimo segundo. Fora do top 5 o remanejamento é mais violento: <span class="drv">Power</span> sobe de
nono para sexto na régua da F1 e cai para décimo terceiro no híbrido.</p>
""",
"2026": """
<p>Temporada em andamento, com dezessete das dezoito etapas disputadas — falta apenas Laguna Seca.
<span class="drv">Palou</span> lidera nas dez réguas e seis vitórias em catorze top 10 não deixam margem para a tabela
interferir no título.</p>
<p>A briga é pelo vice, e aqui a régua importa de verdade. Na tabela em vigor,
<span class="drv">Lundgaard</span> é segundo, <span class="drv">Kirkwood</span> terceiro e
<span class="drv">O'Ward</span> quarto, separados por onze pontos. Reintroduza a dobra da Indy 500 e
<strong>O'Ward salta para segundo</strong> — ele foi quarto em Indianápolis, contra décimo sétimo de Lundgaard e décimo
sexto de Kirkwood. O mesmo acontece com a final em dobro, porque O'Ward venceu a última prova disputada. São três
pilotos empilhados dentro da margem de erro de qualquer escolha de regulamento.</p>
<p><em>Uma ressalva:</em> como Laguna Seca ainda não correu, o multiplicador de “final em dobro” está caindo sobre
Milwaukee 2, a última etapa já disputada. Essa coluna precisa ser refeita quando a temporada fechar.</p>
""",
}

import pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
dados = (AQUI / "slim2.json").read_text(encoding="utf-8")
css = (AQUI / "style.css").read_text(encoding="utf-8")
js = (AQUI / "app.js").read_text(encoding="utf-8")

HTML = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pontuações Alternativas da IndyCar</title>
<meta name="description" content="Onze temporadas da IndyCar (2016–2026) recalculadas sob dez sistemas de pontuação diferentes, incluindo o da Fórmula 1.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>
__CSS__
</style>
</head>
<body>

<header class="masthead">
  <div class="wrap">
    <div class="mast-grid">
      <div>
        <span class="eyebrow">IndyCar · 2016–2026 · dez sistemas de pontuação</span>
        <h1>E se a IndyCar<br>pontuasse <em>diferente</em>?</h1>
        <p class="lead">
          Hoje uma vitória na IndyCar vale 50 pontos e o segundo lugar, 40 — uma curva muito mais achatada que a da
          Fórmula 1, onde a mesma distância custa 25 contra 18 e o décimo primeiro lugar não vale nada. Onze temporadas
          foram recalculadas aqui sob dez réguas diferentes, sempre a partir da posição de chegada real de cada prova.
          A pergunta é simples: <strong>o campeonato teria dado outro resultado?</strong>
        </p>
      </div>
      <div class="keyfigs">
        <div class="keyfig"><div class="n">110</div><div class="l">campeonatos recalculados<br>11 anos × 10 réguas</div></div>
        <div class="keyfig"><div class="n">81</div><div class="l">com o top 5 reordenado<br>de 99 comparações</div></div>
        <div class="keyfig"><div class="n hit">4</div><div class="l">anos com outro campeão<br>2017, 2018, 2019, 2024</div></div>
      </div>
    </div>
  </div>
</header>

<nav class="tabbar" aria-label="Temporadas">
  <div class="wrap">
    <div id="tabs" role="tablist" style="display:flex;align-items:stretch;gap:2px;overflow-x:auto;flex:1"></div>
    <button type="button" id="theme" class="themebtn" aria-label="Alternar tema claro e escuro" title="Alternar tema">&#9681;</button>
  </div>
</nav>

<main id="app"></main>

<footer class="foot">
  <div class="wrap">
    <div>
      <h4>Como foi calculado</h4>
      <p>Toda régua parte <em>apenas</em> da posição de chegada de cada prova. Nenhuma paga pole, volta liderada ou
      liderança de mais voltas — bônus que existem no sistema real e que aparecem só na coluna “Oficial”. Empates são
      desfeitos pelo critério da F1: mais vitórias, depois mais segundos lugares, e assim por diante. A aba
      <a href="#p-pontuacao">Pontuação</a> detalha cada tabela.</p>
    </div>
    <div>
      <h4>Cobertura</h4>
      <p>Todas as 182 provas das onze temporadas entram nos cálculos, com uma exceção declarada: Laguna Seca 2026, que
      ainda não foi disputada. O Thermal Club de 2024 fica de fora por não ter valido pontos de campeonato. Nos anos em
      que havia multiplicador — Indy 500 e final de 2016 a 2019, só a Indy 500 de 2020 a 2022 — as colunas estão
      rotuladas de acordo.</p>
    </div>
    <div>
      <h4>Fontes</h4>
      <p>Pontos e classificação oficial: arquivos <code>Indy2016.txt</code> … <code>Indy2026.txt</code>. Posições de
      chegada, calendários e tipo de piso: tabelas de classificação das temporadas na Wikipédia — que conferem com os
      arquivos em 3745 das 3748 células comparáveis (99,92%).</p>
    </div>
  </div>
</footer>

<script>
const DATA = __DADOS__;
const ANALISES = __ANALISES__;
__JS__
</script>
</body>
</html>
"""
HTML = (HTML.replace("__CSS__", css).replace("__DADOS__", dados)
            .replace("__ANALISES__", json.dumps(ANALISES, ensure_ascii=False))
            .replace("__JS__", js))
(RAIZ / "index.html").write_text(HTML, encoding="utf-8")
print("index.html:", len(HTML), "bytes")
