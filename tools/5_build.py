# -*- coding: utf-8 -*-
import json

ANALISES = {
"2021": """
<p><span class="drv">Palou</span> é campeão nas nove réguas, com folga em todas. Abaixo dele, porém, 2021 é o melhor
laboratório da coleção para uma pergunta específica: <em>o que a dobra da Indy 500 fazia?</em></p>
<p>A regra estava em vigor, então a coluna <strong>+Indy 500</strong> é o sistema real da época e a régua base mostra o
ano sem ela. Tirar a dobra troca o terceiro lugar: <span class="drv">O'Ward</span>, que foi quarto nas 500 Milhas, cai
para quarto no campeonato, e <span class="drv">Dixon</span> — décimo sétimo em Indianápolis — sobe a terceiro. Mais
atrás, <span class="drv">Ericsson</span> sai do top 5 e <span class="drv">Herta</span> entra. Nenhum título em jogo,
duas posições trocadas.</p>
<p>Trocar a curva inteira faz menos diferença que isso. A pontuação da F1 devolve exatamente o top 5 oficial da
temporada — Palou, Newgarden, O'Ward, Dixon, Herta — e a proposta Indy 30 chega ao mesmo resultado. Só a régua da
final em dobro reordena de verdade: Herta venceu Long Beach, a decisão do ano, e sobe de quinto para quarto, enquanto
O'Ward, que abandonou ali, cai para quinto.</p>
""",
"2022": """
<p>O ano em que a régua deveria importar e não importou. <span class="drv">Power</span> foi campeão com <em>uma</em>
vitória, contra cinco de <span class="drv">Newgarden</span> e três de <span class="drv">McLaughlin</span> — exatamente
o perfil de campeão que se acusa a tabela achatada da IndyCar de fabricar. E ele vence nas nove réguas, inclusive na da
F1, porque a regularidade dele não era de décimos lugares: foram <strong>nove pódios em dezessete provas</strong>. A
pontuação da F1 pune o sétimo lugar, não o segundo.</p>
<p>A dobra da Indy 500 ainda valia, e 2022 mostra o maior efeito dela em seis anos. <span class="drv">Ericsson</span>
venceu as 500 Milhas; com a regra da época ele é quarto no campeonato, e <strong>sem a dobra cai para sexto</strong> —
duas posições que dependiam de uma corrida só. <span class="drv">McLaughlin</span> e <span class="drv">Palou</span>
sobem no lugar dele.</p>
<p>Os outros movimentos são os de sempre. McLaughlin passa Dixon pela terceira colocação nas réguas mais íngremes —
três vitórias e sete pódios contra duas e quatro — e, na régua com peso no misto, chega a tomar o vice de
<span class="drv">Newgarden</span>, o único lugar da página em que isso acontece. E Palou salta de quinto para terceiro
quando a final vale dobrado, porque venceu Laguna Seca.</p>
""",
"2023": """
<p>Primeira temporada sem a dobra da Indy 500, e a primeira em que a coluna <strong>+Indy 500</strong> deixa de ser
história para virar proposta. Reintroduzir o multiplicador promoveria <span class="drv">Newgarden</span>, vencedor das
500 Milhas, de quinto a terceiro — mas não chega perto do título.</p>
<p>Título e vice estão fechados em qualquer régua: <span class="drv">Palou</span> com cinco vitórias e dez pódios em
dezessete provas, <span class="drv">Dixon</span> em segundo nas nove. A disputa é pelo terceiro lugar, e ela é
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
<p>Oito vitórias em dezessete provas. Nenhuma das nove réguas chega perto de ameaçar <span class="drv">Palou</span> — e todas
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
<span class="drv">Palou</span> lidera nas nove réguas e seis vitórias em catorze top 10 não deixam margem para a tabela
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
<meta name="description" content="Seis temporadas da IndyCar (2021–2026) recalculadas sob nove sistemas de pontuação diferentes, incluindo o da Fórmula 1.">
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
        <span class="eyebrow">IndyCar · 2021–2026 · nove sistemas de pontuação</span>
        <h1>E se a IndyCar<br>pontuasse <em>diferente</em>?</h1>
        <p class="lead">
          Hoje uma vitória na IndyCar vale 50 pontos e o segundo lugar, 40 — uma curva muito mais achatada que a da
          Fórmula 1, onde a mesma distância custa 25 contra 18 e o décimo primeiro lugar não vale nada. Seis temporadas
          completas foram recalculadas aqui sob nove réguas diferentes, sempre a partir da posição de chegada real de
          cada prova. A pergunta é simples: <strong>o campeonato teria dado outro resultado?</strong>
        </p>
      </div>
      <div class="keyfigs">
        <div class="keyfig"><div class="n">54</div><div class="l">campeonatos recalculados<br>6 anos × 9 réguas</div></div>
        <div class="keyfig"><div class="n">38</div><div class="l">com o top 5 reordenado<br>de 48 comparações</div></div>
        <div class="keyfig"><div class="n hit">2</div><div class="l">com outro campeão<br>ambos em 2024</div></div>
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
      <p>Todas as 102 provas das seis temporadas entram nos cálculos, com uma exceção declarada: Laguna Seca 2026, que
      ainda não foi disputada. O Thermal Club de 2024 fica de fora por não ter valido pontos de campeonato. Nos anos em
      que a Indy 500 valia dobro (2021 e 2022) as colunas estão rotuladas de acordo.</p>
    </div>
    <div>
      <h4>Fontes</h4>
      <p>Pontos e classificação oficial: arquivos <code>Indy2021.txt</code> … <code>Indy2026.txt</code>, cuja soma
      confere com o total de cada piloto nos seis anos. Posições de chegada, calendários e tipo de piso: tabelas de
      classificação das temporadas na Wikipédia — que conferem com os arquivos em 1698 das 1700 células comparáveis.</p>
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
