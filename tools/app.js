
const SIS = DATA.sistemas, ANOS = Object.keys(DATA.anos), RULER = "indy";
const short = d => d.replace(/^[A-Z]\.\s+/, "");
const el = (t, c, h) => { const n = document.createElement(t); if (c) n.className = c;
  if (h != null) n.innerHTML = h; return n; };
const FORMULAS = {
  indy:"50 · 40 · 35 · 32 · 30 · 28 · 26 · 24 · 22 · 20 · 19 … 6 · 5 (25º e além)",
  f1:"25 · 18 · 15 · 12 · 10 · 8 · 6 · 4 · 2 · 1 · 0 …",
  cart:"20 · 16 · 14 · 12 · 10 · 8 · 6 · 5 · 4 · 3 · 2 · 1 · 0 …",
  i500:"tabela IndyCar · Indy 500 × 2",
  final:"tabela IndyCar · última etapa × 2",
  ambas:"tabela IndyCar · Indy 500 × 2 · última etapa × 2",
  hib:"oval → tabela IndyCar · misto e rua → tabela F1",
  hib2:"misto e rua → tabela IndyCar · oval → tabela F1",
  reta:"50 · 48 · 46 · 45 · 43 · 41 … 16 · 14 · 12 · 10 · 9 · 7 · 5 (26º e além)",
  i30:"30 · 22 · 18 · 15 · 13 · 11 · 10 · 9 · 8 · 7 · 6 · 5 · 4 · 3 · 2 · 1 (16º e além) · Indy 500 × 1,5",
};
/* subtítulo de cada coluna: descreve o que a régua faz.
   A Indy 500 valeu pontos dobrados de 2014 a 2022, então duas colunas mudam de sentido por época. */
const SUB = {
  f1:    "só o top 10 pontua",
  cart:  "top 12, tabela dos anos 90",
  final: "última etapa vale 2×",
  ambas: "Indy 500 e final 2×",
  hib:   "IndyCar no oval, F1 no misto",
  hib2:  "IndyCar no misto, F1 no oval",
  i30:   "curva própria",
  reta:  "50 a 5 em linha reta",
};
const EPOCA = {           // multiplicador que a IndyCar aplicava de verdade naquele ano
  ambas: {curto:"Indy 500 e final ×2", longo:"as 500 Milhas <b>e a última etapa</b> valiam pontuação dobrada"},
  i500:  {curto:"Indy 500 ×2",         longo:"as 500 Milhas valiam <b>pontuação dobrada</b>"},
};
function selo(sid, A){
  if (sid === RULER)  return A.epoca ? (A.epoca === "ambas" ? "sem os multiplicadores da época"
                                                            : "sem a dobra da Indy 500")
                                     : "regra em vigor hoje";
  if (sid === A.epoca) return "regra da época: " + EPOCA[A.epoca].curto;
  if (sid === "i500") return "Indy 500 vale 2×";
  return SUB[sid] || "";
}

/* ---------------- matriz de um ano ---------------- */
function matriz(ano){
  const A = DATA.anos[ano], P = A.pilotos, base = A.rank[RULER];
  const cols = [{id:"oficial", curta:"Oficial",
    desc:"Classificação real da temporada, com os pontos como foram somados na época — inclui os bônus de pole e de voltas lideradas."}].concat(SIS);
  const tb = el("table","matrix");
  const htr = el("tr");
  htr.appendChild(el("th","poscol","#"));
  cols.forEach(c => {
    const th = el("th", c.id === RULER ? "ruler" : (c.id === "oficial" ? "official" : ""));
    const sub = c.id === "oficial" ? "temporada real" : selo(c.id, A);
    const marca = (c.id === RULER || c.id === "i500") ? " mark" : "";
    th.innerHTML = c.curta + '<span class="sub'+marca+'">' + sub + "</span>";
    th.title = c.desc;
    htr.appendChild(th);
  });
  const thead = el("thead"); thead.appendChild(htr); tb.appendChild(thead);

  const tbody = el("tbody");
  const ctr = el("tr","champbar");
  ctr.appendChild(el("td","poscol",""));
  const champBase = base[0];
  cols.forEach(c => {
    const w = A.rank[c.id][0];
    const td = el("td", (c.id !== "oficial" && w !== champBase) ? "diff" : "");
    td.dataset.driver = w;
    td.innerHTML = '<span class="cell"><span class="nm">'+ short(w) +"</span></span>";
    ctr.appendChild(td);
  });
  tbody.appendChild(ctr);

  for (let i = 0; i < 10; i++){
    const tr = el("tr", i === 0 ? "champrow" : "");
    tr.appendChild(el("td","poscol", String(i+1)));
    cols.forEach(c => {
      const d = A.rank[c.id][i];
      const td = el("td", c.id === RULER ? "is-ruler" : (c.id === "oficial" ? "is-official" : ""));
      if (!d){ td.appendChild(el("span","cell","")); tr.appendChild(td); return; }
      td.dataset.driver = d;
      const pts = c.id === "oficial" ? P[d].of : P[d].s[c.id];
      let dl = "";
      if (c.id !== "oficial" && c.id !== RULER){
        const was = base.indexOf(d) + 1, now = i + 1;
        if (was > 0 && was !== now)
          dl = '<span class="dl '+(now < was ? "up" : "down")+'">'+(now < was ? "▲" : "▼")+Math.abs(was-now)+"</span>";
      }
      td.innerHTML = '<span class="cell"><span class="nm">'+ short(d) +"</span>"+
        '<span class="row2"><span class="pt">'+ pts +"</span>"+ dl +"</span></span>";
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  }
  tb.appendChild(tbody);
  return tb;
}

/* ---------------- painel de ano ---------------- */
function painelAno(ano){
  const A = DATA.anos[ano], sec = el("section","panel"), w = el("div","wrap");
  sec.id = "p-" + ano;

  const head = el("div","panel-head");
  head.appendChild(el("h2","ano", ano));
  const champs = new Set(SIS.map(s => A.rank[s.id][0]));
  const ctx = el("div","ctx");
  ctx.innerHTML =
    "<span><b>"+A.n_etapas+"</b> etapas</span>" +
    "<span><b>"+A.n_ovais+"</b> em oval</span>" +
    "<span>Indy 500 na <b>"+A.i500_round+"ª</b></span>" +
    "<span>final em <b>"+A.final+"</b></span>" +
    (A.epoca ? '<span style="color:var(--gold);font-weight:600">'+EPOCA[A.epoca].curto+" na época</span>" : "") +
    (champs.size > 1 ? '<span style="color:var(--gold);font-weight:600">'+champs.size+" campeões diferentes</span>" : "");
  head.appendChild(ctx);
  w.appendChild(head);

  let aviso = "";
  if (A.epoca)
    aviso = "Em "+ano+" "+EPOCA[A.epoca].longo+". Aqui a coluna <b>"+
      (A.epoca === "ambas" ? "+Ambas" : "+Indy 500")+"</b> é, portanto, a <em>regra da época</em>, e a régua base "+
      "é o contrafactual: como o ano teria terminado com todas as etapas valendo o mesmo. As duas colunas lado a "+
      "lado respondem exatamente a isso.";
  else if (A.pendentes.length)
    aviso = "Temporada em andamento: <b>"+A.pendentes.join(" e ")+"</b> ainda não "+
      (A.pendentes.length>1?"foi disputada":"foi disputada")+". O multiplicador de “final em dobro” está aplicado a <b>"+
      A.final+"</b>, a última etapa já corrida, e não à decisão real do campeonato — essa coluna precisa ser refeita quando o ano fechar.";
  if (aviso){
    const n = el("div","notice");
    n.innerHTML = '<span class="mk">!</span><span>'+aviso+"</span>";
    w.appendChild(n);
  }

  const sc = el("div","matrix-scroll"); sc.appendChild(matriz(ano)); w.appendChild(sc);

  const lg = el("div","legendrow");
  lg.innerHTML =
    '<span><span class="sw" style="background:var(--accent-soft);box-shadow:inset 0 0 0 1px var(--accent)"></span>régua base</span>' +
    '<span><span class="dl up">▲</span> subiu / <span class="dl down">▼</span> caiu em relação à régua base</span>' +
    '<span><span class="sw" style="background:var(--gold-soft);box-shadow:inset 0 0 0 1px var(--gold)"></span>campeão diferente</span>' +
    '<span style="color:var(--ink-2)">passe o cursor sobre um piloto para segui-lo entre as réguas</span>';
  w.appendChild(lg);

  const an = el("div","analysis");
  const left = el("div");
  left.appendChild(el("h3", null, "O que muda em " + ano));
  left.appendChild(el("div","prose", ANALISES[ano]));
  an.appendChild(left);

  const right = el("div");
  const c1 = el("div","sidecard");
  let rows = "";
  A.rank[RULER].slice(0,6).forEach(d => {
    const p = A.pilotos[d];
    rows += "<tr><td>"+short(d)+"</td><td>"+p.v+"V · "+p.pd+"P · "+p.t10+"T10</td></tr>";
  });
  c1.innerHTML = "<h4>Perfil dos seis primeiros</h4><table>"+rows+"</table>"+
    '<p class="note">Vitórias · pódios · top 10 nas '+A.n_disp+" etapas disputadas. É o que separa uma régua da outra.</p>";
  right.appendChild(c1);

  const c2 = el("div","sidecard"); c2.style.marginTop = "14px";
  let rows2 = "";
  A.rank[RULER].slice(0,6).forEach(d => {
    const p = A.pilotos[d];
    rows2 += "<tr><td>"+short(d)+"</td><td>"+(p.i5 ? p.i5+"º" : "—")+" · "+(p.fi ? p.fi+"º" : "—")+"</td></tr>";
  });
  c2.innerHTML = "<h4>Nas etapas multiplicadas</h4><table>"+rows2+"</table>"+
    '<p class="note">Posição na Indy 500 e na '+A.final+". São essas duas corridas que os multiplicadores ampliam.</p>";
  right.appendChild(c2);

  const c3 = el("div","sidecard"); c3.style.marginTop = "14px";
  let chips = "";
  A.etapas.forEach(e => {
    const cls = "stg" + (e.t === "oval" ? " oval" : "") + (e.i5 ? " i5" : "") +
                (e.fin ? " fin" : "") + (e.pend ? " off" : "");
    let tt = e.t === "oval" ? "oval" : (e.t === "street" ? "circuito de rua" : "circuito misto");
    if (e.pend) tt += " · ainda não disputada";
    chips += '<span class="'+cls+'" title="'+tt+'">'+e.n+"</span>";
  });
  c3.innerHTML = "<h4>Calendário</h4><div class=\"stagelist\">"+chips+"</div>"+
    '<div class="stagelist legenda"><span class="stg oval">oval</span><span class="stg i5">Indy 500</span>'+
    '<span class="stg fin">final</span>'+(A.pendentes.length?'<span class="stg off">por correr</span>':"")+"</div>";
  right.appendChild(c3);
  an.appendChild(right);
  w.appendChild(an);
  sec.appendChild(w);
  return sec;
}

/* ---------------- gráfico das curvas ---------------- */
const CURVAS = [
  {id:"indy",   nome:"IndyCar",   cor:"var(--s1)", key:"indy"},
  {id:"f1",     nome:"Fórmula 1", cor:"var(--s2)", key:"f1"},
  {id:"cart",   nome:"CART",      cor:"var(--s3)", key:"cart"},
  {id:"indy30", nome:"Indy 30",   cor:"var(--s4)", key:"indy30"},
  {id:"reta",   nome:"Reta",      cor:"var(--s1)", key:"reta", dash:"6 4"},
];
const NPOS = 25;
function grafico(){
  const W = 780, H = 362, m = {t:14, r:104, b:44, l:46};
  const iw = W - m.l - m.r, ih = H - m.t - m.b;
  const x = p => m.l + (p - 1) / (NPOS - 1) * iw;
  const y = v => m.t + (1 - v / 100) * ih;
  const series = CURVAS.map(c => {
    const raw = DATA.tabelas[c.key].slice(0, NPOS);
    return Object.assign({}, c, {vals: raw.map(v => v / raw[0] * 100)});
  });
  let s = '<svg class="curves" viewBox="0 0 '+W+" "+H+'" role="img" aria-label="Curvas de pontuação normalizadas">';
  [0,25,50,75,100].forEach(v => {
    s += '<line class="gridline" x1="'+m.l+'" x2="'+(m.l+iw)+'" y1="'+y(v)+'" y2="'+y(v)+'"/>';
    s += '<text class="axistext" x="'+(m.l-9)+'" y="'+(y(v)+3.5)+'" text-anchor="end">'+v+"%</text>";
  });
  [1,5,10,15,20,25].forEach(p => {
    s += '<text class="axistext" x="'+x(p)+'" y="'+(m.t+ih+16)+'" text-anchor="middle">'+p+"º</text>";
  });
  s += '<text class="axislabel" x="'+(m.l+iw/2)+'" y="'+(m.t+ih+35)+'" text-anchor="middle">posição de chegada</text>';
  series.forEach(se => {
    const d = se.vals.map((v,j) => (j?"L":"M") + x(j+1).toFixed(1) + " " + y(v).toFixed(1)).join(" ");
    s += '<path d="'+d+'" fill="none" stroke="'+se.cor+'" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"'+
         (se.dash ? ' stroke-dasharray="'+se.dash+'"' : "") + "/>";
  });
  // rótulos diretos à direita: empurra para baixo o que colidiria (várias curvas terminam em zero)
  const GAP = 13;
  const rot = series.map(se => ({nome:se.nome, cor:se.cor, y:y(se.vals[NPOS-1])}))
                    .sort((a,b) => a.y - b.y);
  rot.forEach((r,i) => { if (i && r.y - rot[i-1].y < GAP) r.y = rot[i-1].y + GAP; });
  rot.forEach(r => {
    s += '<text class="dlabel" x="'+(x(NPOS)+12)+'" y="'+(r.y+4).toFixed(1)+'" fill="'+r.cor+'">'+r.nome+"</text>";
  });
  s += '<g id="hov" style="opacity:0"><line class="hovline" y1="'+m.t+'" y2="'+(m.t+ih)+'"/>';
  series.forEach((se,i) => s += '<circle r="4.5" fill="'+se.cor+'" stroke="var(--surface)" stroke-width="2" data-s="'+i+'"/>');
  s += "</g>";
  s += '<rect id="hit" x="'+m.l+'" y="'+m.t+'" width="'+iw+'" height="'+ih+'" fill="transparent"/></svg>';
  return {svg:s, series, x, y, m, iw, ih, W};
}
function ligarGrafico(g){
  const svg = document.querySelector("#p-pontuacao svg.curves");
  if (!svg) return;
  const hit = svg.querySelector("#hit"), hov = svg.querySelector("#hov");
  const line = hov.querySelector("line"), dots = [...hov.querySelectorAll("circle")];
  const tip = document.getElementById("tip");
  const mostra = ev => {
    const r = svg.getBoundingClientRect(), sc = g.W / r.width;
    let p = Math.round(((ev.clientX - r.left) * sc - g.m.l) / g.iw * (NPOS - 1)) + 1;
    p = Math.max(1, Math.min(NPOS, p));
    const X = g.x(p);
    hov.style.opacity = 1; line.setAttribute("x1", X); line.setAttribute("x2", X);
    dots.forEach((c,i) => { c.setAttribute("cx", X); c.setAttribute("cy", g.y(g.series[i].vals[p-1])); });
    tip.innerHTML = '<div class="th">'+p+"º lugar</div>" + g.series.map(s =>
      '<div class="tr"><i style="background:'+s.cor+'"></i><span>'+s.nome+"</span><span>"+
      DATA.tabelas[s.key][p-1]+" pts · "+Math.round(s.vals[p-1])+"%</span></div>").join("");
    tip.style.opacity = 1;
    tip.style.left = Math.min(X/sc + 16, r.width - tip.offsetWidth - 8) + "px";
    tip.style.top = "10px";
  };
  hit.addEventListener("mousemove", mostra);
  hit.addEventListener("mouseleave", () => { hov.style.opacity = 0; tip.style.opacity = 0; });
}

/* ---------------- painel: pontuação ---------------- */
function painelPontuacao(){
  const sec = el("section","panel"); sec.id = "p-pontuacao";
  const w = el("div","wrap");
  const head = el("div","panel-head"); head.appendChild(el("h2", null, "Pontuação"));
  w.appendChild(head);
  w.appendChild(el("p","section-intro",
    "Primeiro como a IndyCar realmente pontua — a tabela, os bônus e a regra que mudou em 2023. "+
    "Depois a comparação numérica entre as tabelas de pontos que as dez réguas usam."));

  /* --- o sistema real --- */
  w.appendChild(el("h3","subhead","O sistema da IndyCar hoje"));
  const grade = el("div","grade");
  const t = DATA.tabelas.indy;
  for (let p = 1; p <= 25; p++){
    const c = el("div","gp" + (p <= 3 ? " top" : "") + (p <= 10 ? " sc" : ""));
    c.innerHTML = '<span class="gp-pos">'+p+"º</span><span class=\"gp-pts\">"+t[p-1]+"</span>";
    grade.appendChild(c);
  }
  const cx = el("div","gp resto");
  cx.innerHTML = '<span class="gp-pos">26º+</span><span class="gp-pts">5</span>';
  grade.appendChild(cx);
  w.appendChild(grade);
  w.appendChild(el("p","note wide",
    "Todo piloto que larga pontua: a tabela desce de 50 até 5 e nunca chega a zero. "+
    "Numa categoria em que equipes pequenas disputam o ano inteiro, essa cauda é uma decisão deliberada — e é a maior diferença estrutural para a Fórmula 1."));

  const bonus = el("div","bonuslist");
  [["+1","Pole position","Em todas as etapas menos a Indy 500, e só quando há classificação."],
   ["+1","Liderar uma volta","Basta cruzar a linha na frente uma vez durante a corrida."],
   ["+2","Liderar mais voltas","Para quem liderar o maior número de voltas da prova."],
   ["1–12","Classificação da Indy 500","Os doze pilotos do Fast 12 pontuam pela qualificação, de 12 pontos para o mais rápido."],
   ["−10","Troca de motor","Perda de 10 pontos por troca feita antes de o motor cumprir a quilometragem exigida."]
  ].forEach(([v,t2,d]) => {
    const b = el("div","bonus");
    b.innerHTML = '<span class="bv">'+v+'</span><span><b>'+t2+"</b><span>"+d+"</span></span>";
    bonus.appendChild(b);
  });
  w.appendChild(bonus);
  w.appendChild(el("p","note wide",
    "Nenhuma das réguas desta página usa esses bônus: todas partem só da posição de chegada. "+
    "É o que mantém a comparação limpa — a única variável entre duas colunas é a curva de pontos. "+
    "Os bônus aparecem apenas na coluna “Oficial”, que reproduz a temporada como ela foi."));

  /* --- a regra que mudou --- */
  w.appendChild(el("h3","subhead","Os multiplicadores que a IndyCar já usou"));
  const tl = el("div","timeline");
  tl.innerHTML =
    '<div class="era"><span class="eyebrow">2014</span><b>Dobro nas provas de 500 milhas</b>'+
    "<p>Indy 500, Pocono e Fontana pagavam 100 pontos ao vencedor em vez de 50.</p></div>"+
    '<div class="era"><span class="eyebrow">2015 – 2019</span><b>Dobro na Indy 500 e na final</b>'+
    "<p>A última corrida do ano passou a valer o dobro também, fosse ela oval, misto ou rua. É sob esta versão "+
    "que <b>2016 a 2019</b> foram disputadas.</p></div>"+
    '<div class="era"><span class="eyebrow">2020 – 2022</span><b>Dobro só na Indy 500</b>'+
    "<p>A final voltou ao peso normal. É sob esta versão que <b>2020, 2021 e 2022</b> foram disputadas.</p></div>"+
    '<div class="era now"><span class="eyebrow">2023 – hoje</span><b>Nenhum multiplicador</b>'+
    "<p>A IndyCar aboliu a dobra em fevereiro de 2023. O argumento do então presidente Jay Frye foi que a regra "+
    "<em>nunca havia alterado quem ganhou um campeonato</em>, mas volta e meia prejudicava a posição final de equipes "+
    "que disputavam o ano todo, à medida que o grid da Indy 500 crescia.</p></div>";
  w.appendChild(tl);
  w.appendChild(el("p","note wide",
    "Isso muda o que as colunas de multiplicador significam em cada aba. De 2016 a 2019 a régua da época é "+
    "<b>+Ambas</b>; de 2020 a 2022, <b>+Indy 500</b>; nos dois casos a régua base mostra como o ano teria terminado "+
    "sem os multiplicadores. De 2023 em diante a relação se inverte: a base é a regra em vigor e as colunas de "+
    "multiplicador viram propostas de reintroduzi-lo. "+
    "<b>Os dados dão razão a Frye:</b> refazendo as sete temporadas afetadas com os pontos oficiais e retirando só a "+
    "parte dobrada, o campeão continua o mesmo em todas. O mais perto que a regra chegou de decidir um título foi "+
    "<b>2020</b>, em que a margem de Dixon sobre Newgarden cai de 16 para 6 pontos. Em <b>2017</b> a regra não "+
    "decidiu o título, mas decidiu o vice: Dixon abandonou na Indy 500, que valia dobro, e sem o multiplicador ele "+
    "passa Pagenaud."));

  w.appendChild(el("p","note wide",
    'As dez réguas em si estão descritas na aba <a href="#p-reguas">As réguas</a>. '+
    "O que segue é a comparação numérica entre as cinco tabelas de pontos que elas usam."));

  /* --- gráfico --- */
  const g = grafico();
  const fig = el("figure","chart");
  fig.innerHTML =
    '<div class="chart-title">O que cada tabela paga, em relação à vitória</div>'+
    '<div class="chart-sub">Pontos de cada posição como porcentagem dos pontos de uma vitória — as cinco tabelas na mesma escala.</div>'+
    '<div class="chartlegend">'+ CURVAS.map(c => '<span><i style="'+(c.dash
      ? "background:repeating-linear-gradient(90deg,"+c.cor+" 0 5px,transparent 5px 8px)"
      : "background:"+c.cor)+'"></i>'+c.nome+"</span>").join("") +"</div>"+
    '<div class="svgbox">'+ g.svg +'<div id="tip"></div></div>'+
    "<figcaption>A IndyCar nunca desce muito: um décimo lugar ainda vale 40% de uma vitória e o último colocado leva 10%. "+
    "A F1 desaba — o décimo vale 4% e o décimo primeiro, nada. A CART fica no meio: pódio idêntico ao da IndyCar "+
    "(80% e 70%), queda rápida depois e corte no décimo segundo. A proposta “Indy 30” copia o degrau íngreme da F1 nos "+
    "cinco primeiros e depois estica uma cauda rasa até o fim do grid, em vez de cortá-la. A “Reta” é a mesma faixa de "+
    "pontos da IndyCar — 50 no primeiro, 5 no vigésimo sexto — traçada como reta: por isso aparece na mesma cor, "+
    "tracejada. Tudo o que muda entre as duas é a curvatura.</figcaption>";
  w.appendChild(fig);

  const card = el("figure","chart");
  let th = "<thead><tr><th>Tabela</th>";
  for (let p = 1; p <= 15; p++) th += "<th>"+p+"º</th>";
  th += "<th>20º</th><th>25º</th></tr></thead><tbody>";
  CURVAS.forEach(c => {
    const t2 = DATA.tabelas[c.key];
    th += "<tr><td>"+c.nome+"</td>";
    for (let p = 1; p <= 15; p++) th += "<td"+(t2[p-1]===0?' class="zero"':"")+">"+t2[p-1]+"</td>";
    th += "<td"+(t2[19]===0?' class="zero"':"")+">"+t2[19]+"</td><td"+(t2[24]===0?' class="zero"':"")+">"+t2[24]+"</td></tr>";
  });
  th += "</tbody>";
  card.innerHTML = '<div class="chart-title">Pontos por posição</div>'+
    '<div class="chart-sub">Os mesmos números do gráfico, em valores absolutos.</div>'+
    '<div style="overflow-x:auto"><table class="ptable">'+th+"</table></div>";
  w.appendChild(card);

  sec.appendChild(w);
  setTimeout(() => ligarGrafico(g), 0);
  return sec;
}


/* ---------------- painel: as réguas (abertura) ---------------- */
const EXPLICA = [
 {id:"indy", ex:"É a coluna verde nas tabelas de cada ano. As setas ▲▼ nas outras colunas contam quantas posições o piloto sobe ou desce em relação a ela."},
 {id:"f1",   ex:"Em 2023, McLaughlin é terceiro na tabela da IndyCar com uma vitória e catorze top 10. Na da F1 ele cai para quinto e Newgarden, com quatro vitórias mas só onze top 10, assume o terceiro lugar."},
 {id:"cart", ex:"Em 2023 as três tabelas históricas produzem <b>três terceiros lugares diferentes</b>: McLaughlin pela IndyCar, Newgarden pela F1 e O'Ward pela CART. E em 2026 ela é a única das dez réguas que dá o vice a Kirkwood em vez de Lundgaard."},
 {id:"i500", ex:"Em 2022 é o que garante o quarto lugar a Ericsson, vencedor das 500 Milhas. Sem a dobra ele cai para sexto — duas posições que dependiam de uma corrida só."},
 {id:"final",ex:"Em 2024 dá o título a Herta, que venceu Nashville enquanto Palou terminava em décimo primeiro. Em 2019, aplicada junto com a dobra da Indy 500 — como era a regra da época —, tira o título de Dixon e o dá a Pagenaud."},
 {id:"ambas",ex:"Em 2024 os dois multiplicadores se anulam e o título volta para Palou, que foi quinto na Indy 500 — onde Herta foi vigésimo terceiro. Não é hipótese: foi a regra real de 2015 a 2019, e nesses anos é ela, e não a régua base, que reproduz o regulamento vigente."},
 {id:"hib",  ex:"Em 2024, com sete ovais em dezessete provas, é o bastante para fazer McLaughlin campeão no lugar de Palou. Em 2019 dá o título a Newgarden, que a régua base põe em segundo — e que foi, de fato, o campeão daquele ano."},
 {id:"hib2", ex:"O contraste com a régua anterior é o mais forte da página: o mesmo McLaughlin de 2024 que era campeão com peso no oval cai para <b>quinto</b> com peso no misto. Em 2022, é a única régua em que Newgarden perde o vice para McLaughlin."},
 {id:"reta", ex:"Em 2021 ela leva o campeonato a um <b>empate exato — 619 a 619</b> entre Palou e Newgarden, decidido só no critério de desempate, pelas três vitórias de Palou contra duas. Em 2017 chega a trocar o campeão, e em 2016 derruba Power do segundo para o <b>sexto</b> lugar apesar das quatro vitórias."},
 {id:"i30",  ex:"Na prática ela se comporta como a tabela da F1 no topo do campeonato e como a da IndyCar no meio do pelotão. Em cinco dos onze anos devolve o mesmo top 5 da régua da F1."},
];
const TEXTO = {
 indy:"A tabela que a IndyCar usa hoje: <b>50 pontos ao vencedor, 40 ao segundo, 35 ao terceiro</b>, descendo até 5 pontos para quem terminar em 25º ou pior. Todas as corridas do ano valem o mesmo. É a régua contra a qual as outras nove são comparadas.<br><br><b>De 2016 a 2022 ela ganha um segundo sentido.</b> Havia multiplicadores em vigor naqueles anos — Indy 500 e final até 2019, só a Indy 500 de 2020 a 2022 —, então dar peso igual a todas as etapas equivale a <em>removê-los</em>, e a coluna aparece rotulada de acordo nessas abas. É a resposta à pergunta: como o campeonato teria terminado se todas as provas valessem o mesmo?",
 f1:"A tabela da Fórmula 1 atual: <b>25-18-15-12-10-8-6-4-2-1</b>, sem o ponto de volta rápida (a F1 o aboliu em 2025). Duas diferenças grandes em relação à IndyCar.<br><br>A primeira é o <b>degrau do topo</b>: na IndyCar, o segundo lugar vale 80% de uma vitória; na F1, 72%. A segunda, e maior, é o <b>corte</b>: do décimo primeiro em diante ninguém pontua, enquanto na IndyCar até o último colocado leva 5 pontos. Na prática, favorece quem vence e faz pódio e penaliza quem termina muitas corridas entre o oitavo e o décimo quinto lugar.",
 cart:"A tabela que a <b>CART</b> usou de 1983 a 2003, quando era a principal categoria do automobilismo americano e antecessora direta da IndyCar de hoje: <b>20-16-14-12-10-8-6-5-4-3-2-1</b>, pontuando até o décimo segundo lugar.<br><br>O que a torna interessante é que ela é <b>exatamente intermediária</b> entre as duas tabelas modernas. O pódio tem a mesma proporção da IndyCar atual — 100%, 80% e 70% de uma vitória — mas a partir do quarto lugar a curva desce muito mais rápido, e o corte no décimo segundo fica entre o décimo da F1 e a cauda sem fim da IndyCar. Ela premia o pódio como a IndyCar e o meio do pelotão como a F1, o que a faz produzir resultados que nenhuma das outras duas produz.",
 i500:"Mantém a tabela da IndyCar, mas as <b>500 Milhas de Indianápolis pagam o dobro</b>: 100 pontos ao vencedor em vez de 50, 80 ao segundo, e assim por diante.<br><br>Não é invenção — foi a regra real da IndyCar <b>de 2014 a 2022</b>, abolida em 2023. Por isso esta coluna significa coisas diferentes conforme o ano: de 2020 a 2022 ela é <em>o que de fato aconteceu</em> (antes disso a final também dobrava, e a regra da época é a régua 06); de 2023 em diante é uma proposta de trazer a regra de volta.",
 final:"A tabela da IndyCar com a <b>última corrida do ano valendo o dobro</b>, no espírito do finale da NASCAR. A ideia é impedir que o título seja decidido antes da prova final e garantir que a decisão tenha público.<br><br>É o multiplicador mais agressivo do conjunto, porque concentra o desempate numa corrida só. Também existiu de verdade: entre 2015 e 2019 a final valia dobro na IndyCar, sempre em conjunto com a Indy 500.",
 ambas:"As duas réguas anteriores aplicadas juntas: <b>Indy 500 e última etapa valendo o dobro</b>. Serve para testar o que acontece quando se privilegia ao mesmo tempo a corrida mais importante do ano e a que decide o campeonato.<br><br>O resultado é o melhor argumento contra multiplicadores em geral: eles podem se cancelar, e aí o campeão passa a depender de qual etapa alguém decidiu privilegiar.",
 hib:"A única régua que <b>não mexe na curva de pontos</b> — ela muda o peso conforme o tipo de pista. Os <b>ovais</b> pagam pela tabela cheia da IndyCar (50 ao vencedor); os <b>circuitos mistos e de rua</b> pagam pela tabela da F1 (25 ao vencedor). Na prática, um oval passa a valer o dobro de um circuito misto.<br><br>A ideia é tratar as duas disciplinas como campeonatos de lógicas diferentes, já que exigem carros, pilotagem e coragem distintos. O efeito depende inteiramente de quantos ovais o calendário teve naquele ano.",
 hib2:"O espelho da régua anterior: os <b>circuitos mistos e de rua</b> pagam pela tabela cheia da IndyCar (50 ao vencedor) e os <b>ovais</b> pagam pela tabela da F1 (25). Um misto passa a valer o dobro de um oval.<br><br>Não é uma proposta séria de regulamento — nenhuma categoria trataria a Indy 500 como meia corrida. Serve como experimento de controle: rodar as duas versões do híbrido mostra <em>quanto</em> do resultado de um ano dependia do equilíbrio entre ovais e mistos no calendário, e não do desempenho dos pilotos. Quanto mais um piloto se move entre as duas colunas, mais especializado ele era.",
 reta:"Todas as outras réguas desta página são <em>mais</em> íngremes que a da IndyCar, ou mexem em multiplicadores e calendário. Esta vai na direção oposta: e se a curva fosse ainda mais achatada, premiando menos a dominância e mais a presença?<br><br>Ela mantém <b>exatamente a mesma amplitude</b> da tabela atual — 50 pontos ao vencedor, 5 ao vigésimo sexto — e muda só o formato: em vez de despencar do primeiro ao quinto lugar e depois virar quase plana, desce em <b>linha reta</b>, 1,8 ponto por posição. O segundo lugar passa a valer 96% de uma vitória (contra 80% hoje) e o décimo, 68% (contra 40%). Isolar a curvatura assim é o teste mais limpo possível da pergunta: o que muda quando só a <em>forma</em> da curva muda, e não a escala?<br><br>A resposta é que ela troca o campeão de <b>2017</b> — Pagenaud no lugar de Newgarden — e deixa 2021 a zero ponto de trocar, num empate em 619. Mais atrás, é a régua que mais embaralha: em 2022 Newgarden cai do segundo para o quinto lugar, e em <b>2016 Power cai do segundo para o sexto</b> com quatro vitórias no ano, atrás de Kimball, que não subiu ao pódio nenhuma vez. Quando vencer deixa de valer muito mais que chegar em quarto, o campeonato passa a ser de quem termina.",
 i30:"Proposta própria, desenhada para corrigir os dois defeitos opostos das tabelas anteriores. A da <b>IndyCar achata demais o topo</b>: entre vencer e ficar em segundo vão apenas 20% de diferença, o que faz a regularidade valer mais que a vitória. A da <b>F1 corta cedo demais</b> para um grid de 27 carros em que equipes pequenas disputam o ano inteiro sem chance de top 10.<br><br>A Indy 30 usa <b>30-22-18-15-13-11-10-9-8-7-6-5-4-3-2</b> e 1 ponto do décimo sexto em diante. O degrau proporcional dos cinco primeiros é o mesmo da F1, mas a cauda continua pagando até o último colocado. E a Indy 500 vale <b>1,5×</b>: reconhece o peso da corrida sem dobrá-la.",
};
function painelReguas(){
  const sec = el("section","panel"); sec.id = "p-reguas";
  const w = el("div","wrap");
  const head = el("div","panel-head"); head.appendChild(el("h2", null, "As réguas"));
  w.appendChild(head);
  w.appendChild(el("p","section-intro",
    "Uma <b>régua</b> é um jeito de transformar a posição de chegada em pontos de campeonato. "+
    "Esta página recalcula onze temporadas da IndyCar sob dez delas, para ver quais resultados dependiam do "+
    "regulamento e quais eram inevitáveis. Todas usam <em>apenas</em> a ordem de chegada de cada prova — nenhuma "+
    "paga pole, volta liderada ou liderança de mais voltas."));

  const lista = el("div","reguas");
  SIS.forEach((S, i) => {
    const E = EXPLICA.find(e => e.id === S.id);
    const d = el("article","regua" + (S.id === RULER ? " base" : ""));
    d.innerHTML =
      '<div class="rnum"><span>'+String(i+1).padStart(2,"0")+"</span>"+
        (S.id === RULER ? '<span class="rbadge">base</span>' : "")+"</div>"+
      '<div class="rbody"><h3>'+S.nome+"</h3>"+
        '<div class="formula">'+FORMULAS[S.id]+"</div>"+
        "<p>"+TEXTO[S.id]+"</p>"+
        '<div class="exemplo"><span class="exlabel">Na prática</span>'+E.ex+"</div></div>";
    lista.appendChild(d);
  });
  w.appendChild(lista);

  /* precedente historico dos multiplicadores */
  w.appendChild(el("h3","subhead","Três dessas réguas não são invenções"));
  w.appendChild(el("p","note wide",
    "Dobrar a pontuação de uma corrida soa como exercício de fã, mas é uma ideia que as duas categorias já "+
    "colocaram em prática — e abandonaram. As réguas 04, 05 e 06 desta página reconstroem regras que existiram de verdade."));
  const hist = el("div","hist");
  [["IndyCar","2014","Dobro nas três provas de 500 milhas",
    "Indy 500, Pocono e Fontana. Uma retomada de tradição: nos anos 1950 a Indy 500 chegou a valer 1000 pontos contra 200 de uma corrida comum."],
   ["Fórmula 1","2014","Dobro na última corrida",
    "Ideia de Bernie Ecclestone para segurar audiência até Abu Dhabi. Durou <b>uma temporada</b>: a reação de equipes e público foi tão ruim que a FIA a revogou antes de 2015. Não chegou a alterar o título — Hamilton venceria de qualquer forma. É exatamente a régua 05."],
   ["IndyCar","2015–2019","Dobro na Indy 500 e na final",
    "A final passou a valer o dobro independentemente de ser oval, misto ou rua. É exatamente a régua 06 — e é o regulamento sob o qual 2016, 2017, 2018 e 2019 foram disputadas."],
   ["IndyCar","2020–2022","Dobro só na Indy 500",
    "A final voltou ao peso normal. É a régua 04, e é o sistema sob o qual 2020, 2021 e 2022 foram disputadas."],
   ["IndyCar","2023–hoje","Nenhum multiplicador",
    "Todas as corridas valem igual. O então presidente Jay Frye justificou dizendo que a dobra <em>nunca havia alterado quem ganhou um campeonato</em> — o que os pontos oficiais das sete temporadas afetadas confirmam, ainda que por 6 pontos em 2020."]
  ].forEach(([cat, ano, tit, txt]) => {
    const h = el("div","hitem" + (ano === "2023–hoje" ? " atual" : ""));
    h.innerHTML = '<div class="hmeta"><span class="hcat">'+cat+'</span><span class="hano">'+ano+"</span></div>"+
      "<div><b>"+tit+"</b><p>"+txt+"</p></div>";
    hist.appendChild(h);
  });
  w.appendChild(hist);
  w.appendChild(el("p","note wide",
    "As duas categorias chegaram à mesma conclusão por caminhos diferentes: a F1 desistiu em um ano por rejeição do "+
    "público, a IndyCar em nove por constatar que a regra não mudava campeonatos. As abas de cada temporada mostram "+
    "o que ela mudava de fato — quase sempre uma ou duas posições logo atrás do líder, e em 2020 seis pontos de margem."));

  /* como ler as tabelas */
  w.appendChild(el("h3","subhead","Como ler as tabelas de cada ano"));
  w.appendChild(el("p","note wide",
    "Cada aba de temporada traz uma tabela com os dez primeiros do campeonato em cada régua, lado a lado. "+
    "As colunas são as réguas; as linhas, as posições finais. A primeira coluna, <b>Oficial</b>, não é uma régua: "+
    "é a classificação real daquele ano, com os bônus e os multiplicadores como valiam na época."));
  const guia = el("div","guia");
  [["<span class=\"sw\" style=\"background:var(--accent-soft);box-shadow:inset 0 0 0 1px var(--accent)\"></span>",
    "Coluna verde", "É a régua base — a tabela da IndyCar com todas as etapas valendo o mesmo. Tudo é comparado a ela."],
   ['<span class="dl up">▲2</span>',
    "Seta e número", "Quantas posições o piloto sobe (verde) ou cai (laranja) naquela régua em relação à coluna verde. Sem seta, ficou no mesmo lugar."],
   ["<span class=\"sw\" style=\"background:var(--gold-soft);box-shadow:inset 0 0 0 1px var(--gold)\"></span>",
    "Faixa dourada", "Marca uma régua que produz um campeão diferente da régua base. Acontece em quatro dos onze anos: 2017, 2018, 2019 e 2024."],
   ['<span class="gnum">548</span>',
    "Número menor", "O total de pontos do piloto naquela régua. Só faz sentido comparar dentro da mesma coluna — cada tabela tem sua própria escala."]
  ].forEach(([ic, t, d]) => {
    const g = el("div","gitem");
    g.innerHTML = '<div class="gic">'+ic+"</div><div><b>"+t+"</b><p>"+d+"</p></div>";
    guia.appendChild(g);
  });
  w.appendChild(guia);
  w.appendChild(el("p","note wide",
    'A aba <a href="#p-pontuacao">Pontuação</a> traz a tabela oficial da IndyCar em detalhe, os bônus que ela paga, '+
    "a história da dobra da Indy 500 e a comparação numérica entre as curvas."));
  sec.appendChild(w);
  return sec;
}

/* ---------------- painel: panorama ---------------- */
function painelPanorama(){
  const sec = el("section","panel"); sec.id = "p-panorama";
  const w = el("div","wrap");
  const head = el("div","panel-head"); head.appendChild(el("h2", null, "Panorama"));
  w.appendChild(head);

  let trocas = 0, total = 0, reord = 0;
  ANOS.forEach(a => {
    const A = DATA.anos[a], base = A.rank[RULER];
    SIS.forEach(S => {
      total++;
      if (A.rank[S.id][0] !== base[0]) trocas++;
      if (S.id !== RULER && A.rank[S.id].slice(0,5).join("|") !== base.slice(0,5).join("|")) reord++;
    });
  });
  const anosTroca = ANOS.filter(a => SIS.some(S =>
    DATA.anos[a].rank[S.id][0] !== DATA.anos[a].rank[RULER][0]));
  w.appendChild(el("p","section-intro",
    "Onze temporadas × dez réguas = <b>"+total+"</b> campeonatos recalculados. Confrontadas com a régua base, as nove "+
    "réguas alternativas reordenam o top 5 em <b>"+reord+"</b> das <b>"+(ANOS.length*(SIS.length-1))+"</b> comparações, "+
    "e o troféu troca de dono em <b>"+trocas+"</b> delas — concentradas em <b>"+anosTroca.length+"</b> temporadas: "+
    anosTroca.join(", ")+". Nos outros sete anos o campeão resiste às dez réguas."));

  const tb = el("table","grid2");
  let h = "<thead><tr><th>Ano</th>";
  SIS.forEach(S => h += "<th>"+S.curta+"</th>");
  h += "</tr></thead><tbody>";
  ANOS.forEach(a => {
    const A = DATA.anos[a], b = A.rank[RULER][0];
    h += '<tr><td class="yr">'+a+(A.epoca?'<span class="mini">'+EPOCA[A.epoca].curto+"</span>":"")+"</td>";
    SIS.forEach(S => {
      const c = A.rank[S.id][0];
      h += '<td class="'+(c === b ? "same" : "chg")+'">'+short(c)+"</td>";
    });
    h += "</tr>";
  });
  tb.innerHTML = h + "</tbody>";
  w.appendChild(tb);

  const grid = el("div","fourup");
  [["Quem a régua favorece",
    "O padrão se repete nos onze anos: quem sobe quando se aperta a curva tem <strong>vitórias e pódios</strong>; quem cai tem <strong>presença</strong>. Newgarden ganha duas posições em 2023, McLaughlin uma em 2022, Lundgaard duas em 2025. <strong>Dixon</strong> é o caso mais consistente na direção oposta: aparece no top 6 da régua base em dez das onze temporadas e perde posição em quase todas as curvas mais íngremes — dez anos de regularidade que qualquer tabela menos achatada desconta."],
   ["Quando o campeão muda",
    "Nos sete anos em que o campeão resiste às dez réguas, ele venceu as duas disputas ao mesmo tempo — Palou lidera em vitórias <em>e</em> em regularidade em 2021, 2023, 2025 e 2026, e aí nenhuma curva importa. As quatro exceções são os anos apertados: 2018 tem <strong>dois pontos</strong> entre Rossi e Dixon na régua base, 2019 tem três pilotos em quatro pontos, 2017 tem dezenove, e 2024 teve cinco pilotos com duas ou três vitórias cada."],
   ["A dobra da Indy 500 não decide nada",
    "Foi o que a IndyCar alegou ao abolir a regra em 2023. Refazendo as sete temporadas afetadas com os pontos oficiais e tirando só a parte dobrada, o campeão é o mesmo em todas — mas em <strong>2020</strong> a margem de Dixon sobre Newgarden cai de 16 para 6 pontos, e em 2017 o vice troca de Pagenaud para Dixon. Dobrar a <em>final</em> é outra coisa: é o que dá 2024 a Herta e, somado à Indy 500, 2019 a Pagenaud."],
   ["O que os dois híbridos revelam",
    "Rodar o mesmo ano com peso no oval e depois com peso no misto mede o quanto um piloto era especialista. O contraste extremo é <strong>McLaughlin em 2024</strong>: campeão numa régua, quinto na outra. Em 2019 o peso no oval dá o título a Newgarden — que a régua base põe em segundo e que foi o campeão de verdade. Elas não reordenam a curva de pontos, reordenam o calendário."]
  ].forEach(([t,p]) => {
    const d = el("div");
    d.appendChild(el("h3","subhead sm", t));
    d.appendChild(el("div","prose sm", "<p>"+p+"</p>"));
    grid.appendChild(d);
  });
  w.appendChild(grid);
  w.appendChild(el("div","blockquote",
    "A tabela da IndyCar é muito mais achatada que a da F1 — mas em onze temporadas isso decidiu um campeonato em quatro delas, sempre as mais apertadas. Quando o ano é folgado, nenhuma régua alcança o campeão; quando é apertado, cada régua aponta para um nome diferente."));
  sec.appendChild(w);
  return sec;
}

/* ---------------- montagem ---------------- */
const main = document.getElementById("app");
main.appendChild(painelReguas());
ANOS.forEach(a => main.appendChild(painelAno(a)));
main.appendChild(painelPanorama());
main.appendChild(painelPontuacao());

const bar = document.getElementById("tabs");
const abas = [["As réguas","p-reguas"]].concat(ANOS.map(a => [a, "p-"+a]))
  .concat([["Panorama","p-panorama"], ["Pontuação","p-pontuacao"]]);
abas.forEach(([rot,id], i) => {
  const b = el("button","tab"+(rot === "Panorama" ? " sep" : ""), rot);
  b.type = "button"; b.setAttribute("role","tab"); b.dataset.target = id;
  b.setAttribute("aria-selected", i === 0 ? "true" : "false");
  b.addEventListener("click", () => selecionar(id));
  bar.appendChild(b);
});
function selecionar(id){
  document.querySelectorAll(".panel").forEach(p => p.classList.toggle("on", p.id === id));
  document.querySelectorAll(".tab").forEach(t =>
    t.setAttribute("aria-selected", t.dataset.target === id ? "true" : "false"));
  if (location.hash.slice(1) !== id) history.replaceState(null, "", "#" + id);
  window.scrollTo({top: 0, behavior: "instant"});
}
selecionar(document.getElementById(location.hash.slice(1)) ? location.hash.slice(1) : "p-reguas");

document.addEventListener("mouseover", e => {
  const td = e.target.closest("td[data-driver]");
  document.querySelectorAll("td.hl").forEach(n => n.classList.remove("hl"));
  if (!td) return;
  td.closest(".panel").querySelectorAll('td[data-driver="'+CSS.escape(td.dataset.driver)+'"]')
    .forEach(n => n.classList.add("hl"));
});
document.addEventListener("click", e => {
  const a = e.target.closest('a[href^="#p-"]');
  if (!a) return;
  e.preventDefault(); selecionar(a.getAttribute("href").slice(1));
});
document.getElementById("theme").addEventListener("click", () => {
  const cur = document.documentElement.getAttribute("data-theme");
  const escuro = cur ? cur === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.setAttribute("data-theme", escuro ? "light" : "dark");
});
