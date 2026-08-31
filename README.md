# E se a IndyCar pontuasse diferente?

Seis temporadas da IndyCar (2021–2026) recalculadas sob dez sistemas de pontuação
diferentes, para separar o que dependia do regulamento do que era inevitável.

**➜ [frubik.github.io/indycar-pontuacoes-alternativas](https://frubik.github.io/indycar-pontuacoes-alternativas/)**

## A pergunta

Hoje uma vitória na IndyCar vale 50 pontos e o segundo lugar, 40 — uma curva muito mais
achatada que a da Fórmula 1, onde a mesma distância custa 25 contra 18 e o décimo primeiro
lugar não vale nada. A IndyCar também paga o último colocado (5 pontos), enquanto a F1 corta
no décimo. Trocar uma tabela pela outra mudaria os campeonatos recentes?

## A resposta

Em **60 campeonatos recalculados** (6 temporadas × 10 réguas), o top 5 sai reordenado em 44
das 54 comparações contra a régua base — mas **o título só troca de dono em dois casos, ambos
em 2024**:

- com a **última etapa valendo o dobro**, Herta é campeão no lugar de Palou (venceu Nashville,
  a decisão do ano, com Palou em 11º);
- com **peso nos ovais**, McLaughlin é campeão (2024 teve sete ovais em dezessete provas).

Dobrar as duas etapas devolve o título a Palou: os multiplicadores se cancelam. É o melhor
argumento contra multiplicadores que os dados produzem — o campeão passa a depender de qual
prova alguém decidiu privilegiar.

Nos outros cinco anos o campeão resiste às dez réguas, porque na IndyCar recente quem ganha
costuma liderar em vitórias *e* em regularidade ao mesmo tempo.

## As dez réguas

Todas partem **apenas da posição de chegada**. Nenhuma paga pole, volta liderada ou liderança
de mais voltas — esses bônus existem no sistema real e aparecem só na coluna "Oficial", que
reproduz a temporada como ela foi. É o que mantém a comparação limpa: a única variável entre
duas colunas é a curva de pontos.

| # | Régua | O que faz |
|---|---|---|
| 01 | IndyCar, etapas iguais | 50-40-35-32-30… até 5. Régua base de comparação |
| 02 | Fórmula 1 | 25-18-15-12-10-8-6-4-2-1; só o top 10 pontua |
| 03 | CART 1983–2003 | 20-16-14-12-10-8-6-5-4-3-2-1; pontua até o 12º |
| 04 | Indy 500 em dobro | Tabela IndyCar, 500 Milhas valendo 2× |
| 05 | Última etapa em dobro | Tabela IndyCar, decisão do campeonato valendo 2× |
| 06 | Indy 500 e final em dobro | As duas anteriores juntas |
| 07 | Híbrido, peso no oval | IndyCar nos ovais, F1 nos mistos e de rua |
| 08 | Híbrido, peso no misto | O inverso — experimento de controle |
| 09 | Proposta "Indy 30" | 30-22-18-15-13… e 1 ponto do 16º em diante; Indy 500 1,5× |
| 10 | Curva reta | Mesma amplitude da IndyCar (50 a 5), mas linear em vez de côncava |

Quatro delas já existiram de verdade: **03** é a tabela da CART, usada por 21 anos e antecessora
direta da IndyCar atual; **05** foi a regra da F1 em 2014 (durou uma temporada), **06** a da
IndyCar de 2015 a 2019 e **04** a de 2020 a 2022. A IndyCar aboliu os multiplicadores em 2023
alegando que nunca haviam alterado um campeonato — o que os números aqui confirmam.

A curva da CART é um meio-termo curioso: o pódio tem exatamente a mesma proporção da IndyCar
de hoje (100%, 80% e 70% de uma vitória), mas cai muito mais rápido depois e corta no 12º. Em
2023 as três tabelas históricas dão **três terceiros lugares diferentes** — McLaughlin pela
IndyCar, Newgarden pela F1 e O'Ward pela CART.

A régua 10 vai na direção oposta de todas as outras. Em vez de premiar mais a vitória, premia
menos: mantém a amplitude exata da tabela atual (50 ao vencedor, 5 ao 26º) e troca a curva
côncava por uma reta, com o 2º valendo 96% de uma vitória em vez de 80%. Serve para testar o
limite da pergunta — e nem no extremo o campeão muda. Mas **2021 termina empatado em 619 a
619** entre Palou e Newgarden, decidido só no desempate por vitórias, e em 2022 Newgarden cai
do 2º para o 5º lugar apesar das cinco vitórias.

Como a Indy 500 valeu pontos dobrados até 2022, a régua 04 muda de sentido conforme o ano: em
2021 e 2022 ela é a *regra da época* e a régua base mostra o ano **sem** a dobra; de 2023 em
diante a relação se inverte. As colunas são rotuladas de acordo em cada aba.

## Os dados

Duas fontes, cruzadas uma contra a outra:

- **Pontos e classificação oficial** — arquivos `Indy2021.txt` … `Indy2026.txt`, colados das
  tabelas de classificação das temporadas. A soma das provas confere com o total de cada
  piloto nos seis anos.
- **Posições de chegada, calendários e tipo de piso (oval / misto / rua)** — extraídos do
  wikitext das páginas `20XX IndyCar Series` da Wikipédia.

As duas fontes concordam em **2419 das 2421 células comparáveis** (99,92%); as duas exceções são casos
de não-largada em 2025, em que o arquivo atribui posição e a Wikipédia deixa vazio. Por isso a
Wikipédia é a fonte das posições e os `.txt` entram só com os pontos oficiais.

Isso importa porque os `.txt` trazem os fins de semana de prova dupla com os pontos das duas
corridas somados numa coluna só (Texas e Detroit em 2021, Milwaukee em 2026): o `colspan` da
tabela original se perde ao copiar. Na Wikipédia essas corridas estão separadas, o que permite
cobrir **as 102 provas** das seis temporadas.

Duas exclusões declaradas: Laguna Seca 2026, ainda não disputada, e o Thermal Club de 2024,
que não valeu pontos de campeonato.

### Os `.txt` não estão neste repositório

São dados de terceiros, facilmente reencontráveis: cada arquivo é a tabela
*Driver standings* da página `20XX IndyCar Series` da Wikipédia, colada como texto. O formato
esperado por prova é `pontos/posição` (ex.: `53/1`), com `-` para quem não participou.

Para regenerar a página você precisa deles na raiz do repositório, ou apontando `INDY_DATA`
para a pasta onde estiverem.

## Regenerar a página

`index.html` é **gerado** — não edite o arquivo diretamente. O pipeline é sequencial e cada
passo grava seu resultado em `tools/`:

```bash
python3 tools/1_fetch_wikipedia.py   # baixa e parseia o wikitext -> wiki_pos.json
python3 tools/2_engine.py            # calcula as dez réguas     -> dados2.json
python3 tools/3_slim.py              # enxuga para a página      -> slim2.json
python3 tools/4_style.py             # gera o CSS                -> style.css
python3 tools/5_build.py             # monta o index.html na raiz
```

O primeiro passo faz cache local dos `.wiki`; apague-os para forçar novo download.
`tools/app.js` é fonte, editado à mão — os outros artefatos em `tools/` são descartáveis.

Para conferir as duas fontes uma contra a outra:

```bash
python3 tools/validate_sources.py
```

A página é um arquivo único, sem build de front-end e sem dependências além do Google Fonts.

## Fontes

- [Temporadas da IndyCar na Wikipédia](https://en.wikipedia.org/wiki/2026_IndyCar_Series) —
  classificações, calendários e tipo de piso
- [Sistemas de pontuação do automobilismo americano](https://en.wikipedia.org/wiki/List_of_American_Championship_car_racing_points_scoring_systems)
- [IndyCar drops double points for Indy 500 — RACER](https://racer.com/2023/02/02/indycar-drops-double-points-for-indy-500)
- [FIA scraps double points at F1 finale — Sky Sports](https://www.skysports.com/f1/news/12433/9591144/fia-scrap-double-points-at-f1-finale-amongst-a-host-of-rule-changes-for-2015)
