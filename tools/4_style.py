CSS = r"""
:root{
  --paper:#F2F2EE; --surface:#FFFFFF; --surface-2:#FAFAF8; --raise:#EDEDE7;
  --ink:#16191B; --ink-2:#454B4F; --muted:#787E83; --rule:#DBDCD5; --rule-2:#C7C9C0;
  --accent:#0F7D57; --accent-soft:#E4F0EA; --gold:#8A6B12; --gold-soft:#F5EEDA;
  --up:#0F7D57; --down:#B4501E; --blue:#2F5FA8;
  --s1:#0F7D57; --s2:#2F5FA8; --s3:#96417F; --s4:#C25A22;
  --shadow:0 1px 2px rgba(20,25,28,.05), 0 6px 20px -12px rgba(20,25,28,.18);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#131619; --surface:#1B1F23; --surface-2:#20252A; --raise:#262C31;
    --ink:#E9EAE6; --ink-2:#B7BDC1; --muted:#8B9297; --rule:#2E343A; --rule-2:#3C444B;
    --accent:#2E9E73; --accent-soft:#15302A; --gold:#D4B25C; --gold-soft:#2C2718;
    --up:#2E9E73; --down:#CE7A3E; --blue:#5A88D4;
    --s1:#2E9E73; --s2:#5A88D4; --s3:#C066A8; --s4:#CE7A3E;
    --shadow:0 1px 2px rgba(0,0,0,.3), 0 8px 24px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --paper:#131619; --surface:#1B1F23; --surface-2:#20252A; --raise:#262C31;
  --ink:#E9EAE6; --ink-2:#B7BDC1; --muted:#8B9297; --rule:#2E343A; --rule-2:#3C444B;
  --accent:#2E9E73; --accent-soft:#15302A; --gold:#D4B25C; --gold-soft:#2C2718;
  --up:#2E9E73; --down:#CE7A3E; --blue:#5A88D4;
  --s1:#2E9E73; --s2:#5A88D4; --s3:#C066A8; --s4:#CE7A3E;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 8px 24px -14px rgba(0,0,0,.7);
}

*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"Archivo","Helvetica Neue",Arial,sans-serif;
  font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1180px; margin:0 auto; padding:0 24px}
h1,h2,h3,h4{margin:0; text-wrap:balance; font-weight:700; letter-spacing:-.017em}
p{margin:0}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent); outline-offset:3px; border-radius:2px}

.eyebrow{
  font-size:11px; font-weight:600; letter-spacing:.13em; text-transform:uppercase;
  color:var(--muted); font-family:"IBM Plex Mono",ui-monospace,monospace;
}

/* ---------- cabeçalho ---------- */
.masthead{border-bottom:1px solid var(--rule); background:var(--surface)}
.masthead .wrap{padding-top:44px; padding-bottom:34px}
.mast-grid{display:grid; grid-template-columns:minmax(0,1.35fr) minmax(0,1fr); gap:52px; align-items:end}
h1{font-size:clamp(34px,5vw,54px); line-height:1.03; margin:14px 0 0}
h1 em{font-style:normal; color:var(--accent)}
.lead{
  font-family:"Source Serif 4",Georgia,serif; font-size:17px; line-height:1.62;
  color:var(--ink-2); max-width:62ch; margin-top:18px;
}
.keyfigs{display:grid; grid-template-columns:repeat(3,1fr); gap:1px; background:var(--rule);
  border:1px solid var(--rule); border-radius:3px; overflow:hidden}
.keyfig{background:var(--surface); padding:14px 16px}
.keyfig .n{font-family:"IBM Plex Mono",monospace; font-size:28px; font-weight:600;
  letter-spacing:-.03em; font-variant-numeric:tabular-nums; line-height:1.1}
.keyfig .n.hit{color:var(--gold)}
.keyfig .l{font-size:11.5px; color:var(--muted); line-height:1.35; margin-top:4px}

/* ---------- abas ---------- */
.tabbar{position:sticky; top:0; z-index:20; background:var(--surface);
  border-bottom:1px solid var(--rule); box-shadow:0 1px 0 rgba(0,0,0,.02)}
.tabbar .wrap{display:flex; align-items:center; gap:2px}
#tabs{scrollbar-width:thin}
.tab{
  appearance:none; background:none; border:0; cursor:pointer; white-space:nowrap;
  font-family:inherit; font-size:13.5px; font-weight:600; color:var(--muted);
  padding:14px 15px 12px; border-bottom:2px solid transparent; letter-spacing:.005em;
}
.tab:hover{color:var(--ink)}
.tab[aria-selected="true"]{color:var(--ink); border-bottom-color:var(--accent)}
.tab.sep{margin-left:auto}
.themebtn{appearance:none; background:none; border:0; cursor:pointer; color:var(--muted);
  padding:0 4px 0 14px; font-size:15px; line-height:1}
.themebtn:hover{color:var(--ink)}

/* ---------- painel ---------- */
.panel{display:none; padding:40px 0 72px}
.panel.on{display:block}
.panel-head{display:flex; flex-wrap:wrap; align-items:flex-end; gap:10px 28px; margin-bottom:6px}
.panel-head h2{font-size:38px; letter-spacing:-.028em; line-height:1; font-weight:700}
.panel-head h2.ano{font-family:"IBM Plex Mono",monospace; font-weight:600; letter-spacing:-.03em}
.ctx{display:flex; flex-wrap:wrap; gap:6px 18px; font-size:12.5px; color:var(--muted);
  padding-bottom:4px}
.ctx b{color:var(--ink-2); font-weight:600}

.notice{
  display:flex; gap:11px; margin:20px 0 0; padding:12px 15px; border-radius:3px;
  background:var(--gold-soft); border-left:2px solid var(--gold);
  font-size:13px; line-height:1.5; color:var(--ink-2); max-width:none;
}
.notice b{color:var(--ink)}
.notice .mk{font-family:"IBM Plex Mono",monospace; color:var(--gold); font-weight:600; flex:none}

/* ---------- matriz ---------- */
.matrix-scroll{overflow-x:auto; margin-top:26px; border:1px solid var(--rule);
  border-radius:3px; background:var(--surface); box-shadow:var(--shadow)}
table.matrix{border-collapse:separate; border-spacing:0; width:100%; min-width:1360px}
.matrix th,.matrix td{text-align:left; padding:0; vertical-align:top}
.matrix thead th{
  position:sticky; top:0; background:var(--surface-2); border-bottom:1px solid var(--rule-2);
  padding:11px 12px 10px; font-size:11.5px; font-weight:700; letter-spacing:.045em;
  text-transform:uppercase; color:var(--ink-2); line-height:1.25; white-space:nowrap;
}
.matrix thead th .sub{display:block; font-weight:500; text-transform:none; letter-spacing:0;
  font-size:10px; color:var(--muted); margin-top:3px; font-family:"IBM Plex Mono",monospace;
  white-space:normal; line-height:1.3; max-width:15em}
.matrix thead th.ruler{color:var(--accent)}
.matrix thead th.official{color:var(--muted)}
.matrix th.poscol,.matrix td.poscol{
  width:44px; text-align:center; font-family:"IBM Plex Mono",monospace;
  font-variant-numeric:tabular-nums; color:var(--muted); font-size:12px;
  background:var(--surface-2); border-right:1px solid var(--rule);
  position:sticky; left:0; z-index:2;
}
.matrix thead th.poscol{z-index:4}
.matrix td.poscol{padding:10px 0; font-weight:600}
.matrix tbody tr:not(:last-child) td{border-bottom:1px solid var(--rule)}
.matrix tbody tr.champrow td{background:var(--gold-soft)}
.matrix tbody tr.champrow td.poscol{background:var(--gold-soft); color:var(--gold); font-weight:700}
.cell{padding:9px 12px; min-width:128px; display:block; border-left:1px solid transparent;
  transition:background .09s linear}
.cell .nm{display:block; font-size:13.5px; font-weight:600; letter-spacing:-.005em;
  line-height:1.25; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.cell .row2{display:flex; align-items:baseline; gap:7px; margin-top:1px}
.cell .pt{font-family:"IBM Plex Mono",monospace; font-size:11.5px; color:var(--muted);
  font-variant-numeric:tabular-nums}
.cell .dl{font-family:"IBM Plex Mono",monospace; font-size:11px; font-weight:600;
  font-variant-numeric:tabular-nums}
.dl.up{color:var(--up)} .dl.down{color:var(--down)}
td.is-ruler .cell{background:var(--accent-soft)}
td.is-official .cell{color:var(--ink-2)}
td.is-official .cell .nm{font-weight:500}
tbody tr:first-child .cell .nm{font-weight:700}
.matrix td.hl .cell{background:var(--raise)}
.matrix td.hl.is-ruler .cell{background:var(--accent-soft); box-shadow:inset 0 0 0 1px var(--accent)}
.matrix td.hl .cell .nm{color:var(--ink)}
.champbar td{border-bottom:1px solid var(--rule-2) !important}
.champbar .cell{padding:7px 12px 8px; background:var(--surface-2)}
.champbar .nm{font-size:11px; font-weight:700; letter-spacing:.07em; text-transform:uppercase;
  color:var(--muted)}
.champbar td.diff .cell{background:var(--gold-soft)}
.champbar td.diff .nm{color:var(--gold)}

.legendrow{display:flex; flex-wrap:wrap; gap:8px 22px; margin-top:11px; font-size:11.5px;
  color:var(--muted); align-items:center}
.legendrow .sw{display:inline-block; width:11px; height:11px; border-radius:2px;
  vertical-align:-1px; margin-right:6px}

/* ---------- análise ---------- */
.analysis{margin-top:38px; display:grid; grid-template-columns:minmax(0,1fr) 290px; gap:44px;
  align-items:start}
.analysis h3{font-size:13px; text-transform:uppercase; letter-spacing:.09em; color:var(--muted);
  font-weight:700; margin-bottom:12px}
.prose{font-family:"Source Serif 4",Georgia,serif; font-size:16.5px; line-height:1.68;
  color:var(--ink-2); max-width:66ch}
.prose p+p{margin-top:14px}
.prose strong{color:var(--ink); font-weight:600}
.prose em{color:var(--ink); font-style:italic}
.prose .drv{font-family:"Archivo",sans-serif; font-weight:600; font-size:15.5px; color:var(--ink)}
.sidecard{background:var(--surface); border:1px solid var(--rule); border-radius:3px;
  padding:16px 17px; font-size:13px}
.sidecard h4{font-size:11px; text-transform:uppercase; letter-spacing:.09em; color:var(--muted);
  margin-bottom:11px}
.sidecard table{width:100%; border-collapse:collapse; font-size:12.5px}
.sidecard td{padding:4px 0; border-bottom:1px solid var(--rule)}
.sidecard tr:last-child td{border-bottom:0}
.sidecard td:last-child{text-align:right; font-family:"IBM Plex Mono",monospace;
  font-variant-numeric:tabular-nums; color:var(--ink-2)}
.stagelist{display:flex; flex-wrap:wrap; gap:4px; margin-top:4px}
.stg{font-family:"IBM Plex Mono",monospace; font-size:10.5px; padding:2px 6px; border-radius:2px;
  background:var(--surface-2); border:1px solid var(--rule); color:var(--muted); white-space:nowrap}
.stg.oval{background:var(--accent-soft); border-color:color-mix(in srgb,var(--accent) 30%,transparent);
  color:var(--accent)}
.stg.i5{border-color:var(--gold); color:var(--gold); background:var(--gold-soft); font-weight:600}
.stg.fin{border-style:dashed; border-color:var(--rule-2); color:var(--ink-2)}
.stg.off{opacity:.5; text-decoration:line-through}

/* ---------- sistemas ---------- */
.syslist{display:grid; grid-template-columns:repeat(auto-fill,minmax(292px,1fr)); gap:14px;
  margin-top:26px}
.syscard{background:var(--surface); padding:17px 18px 18px; border:1px solid var(--rule);
  border-radius:3px; display:flex; flex-direction:column}
.syscard.ref{background:var(--surface-2); border-style:dashed}
.syscard .formula{margin-top:auto; padding-top:10px}
.syscard .tag{font-family:"IBM Plex Mono",monospace; font-size:10.5px; color:var(--muted);
  letter-spacing:.06em}
.syscard h4{font-size:16px; margin:5px 0 8px; letter-spacing:-.012em}
.syscard p{font-size:13.5px; color:var(--ink-2); line-height:1.56}
.formula{font-family:"IBM Plex Mono",monospace; font-size:11.5px; color:var(--accent);
  margin-top:10px; letter-spacing:-.01em; word-spacing:-.05em}

figure.chart{margin:34px 0 0; background:var(--surface); border:1px solid var(--rule);
  border-radius:3px; padding:20px 22px 16px; box-shadow:var(--shadow)}
figure.chart figcaption{font-size:12.5px; color:var(--muted); margin-top:12px; line-height:1.5;
  max-width:70ch}
.chart-title{font-size:15px; font-weight:700; letter-spacing:-.01em}
.chart-sub{font-size:12.5px; color:var(--muted); margin-top:2px}
.chartlegend{display:flex; flex-wrap:wrap; gap:16px; margin:12px 0 6px; font-size:12.5px}
.chartlegend span{display:flex; align-items:center; gap:7px; color:var(--ink-2)}
.chartlegend i{width:14px; height:2px; border-radius:1px; display:block}
.svgbox{position:relative; overflow-x:auto}
svg.curves{display:block; width:100%; height:auto; min-width:520px}
.gridline{stroke:var(--rule); stroke-width:1}
.axistext{fill:var(--muted); font-size:10.5px; font-family:"IBM Plex Mono",monospace}
.axislabel{fill:var(--muted); font-size:10.5px; font-family:"Archivo",sans-serif;
  letter-spacing:.06em; text-transform:uppercase}
.dlabel{font-size:11.5px; font-weight:700; font-family:"Archivo",sans-serif}
.hovline{stroke:var(--rule-2); stroke-width:1; stroke-dasharray:3 3}
#tip{position:absolute; pointer-events:none; background:var(--surface); border:1px solid var(--rule-2);
  border-radius:3px; padding:8px 10px; font-size:12px; box-shadow:var(--shadow); opacity:0;
  transition:opacity .1s; min-width:140px; z-index:5}
#tip .th{font-weight:700; font-size:11px; text-transform:uppercase; letter-spacing:.07em;
  color:var(--muted); margin-bottom:5px}
#tip .tr{display:flex; align-items:center; gap:7px; justify-content:space-between;
  font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums}
#tip .tr i{width:9px; height:9px; border-radius:2px; flex:none}
#tip .tr span:first-of-type{flex:1; font-family:"Archivo",sans-serif}

table.ptable{border-collapse:collapse; width:100%; margin-top:14px; font-size:12px;
  font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums}
.ptable th,.ptable td{padding:5px 4px; text-align:right; border-bottom:1px solid var(--rule)}
.ptable th:first-child,.ptable td:first-child{text-align:left; font-family:"Archivo",sans-serif;
  font-weight:600; white-space:nowrap; padding-right:14px}
.ptable thead th{color:var(--muted); font-weight:600; font-family:"IBM Plex Mono",monospace;
  border-bottom:1px solid var(--rule-2)}
.ptable td.zero{color:var(--rule-2)}

/* ---------- panorama ---------- */
table.grid2{border-collapse:separate; border-spacing:0; width:100%; margin-top:24px;
  background:var(--surface); border:1px solid var(--rule); border-radius:3px; overflow:hidden}
.grid2 th,.grid2 td{padding:11px 13px; text-align:left; font-size:13px;
  border-bottom:1px solid var(--rule)}
.grid2 thead th{background:var(--surface-2); font-size:11px; text-transform:uppercase;
  letter-spacing:.05em; color:var(--ink-2); border-bottom:1px solid var(--rule-2); white-space:nowrap}
.grid2 tbody tr:last-child td{border-bottom:0}
.grid2 td.yr{font-family:"IBM Plex Mono",monospace; font-weight:600; color:var(--ink)}
.grid2 td.same{color:var(--ink-2)}
.grid2 td.chg{background:var(--gold-soft); color:var(--gold); font-weight:700}
.bignum{font-family:"IBM Plex Mono",monospace; font-size:64px; font-weight:600;
  letter-spacing:-.045em; line-height:1; color:var(--accent)}

.section-intro{font-family:"Source Serif 4",Georgia,serif; font-size:17px; line-height:1.65;
  color:var(--ink-2); max-width:64ch; margin-top:14px}
.blockquote{border-left:2px solid var(--accent); padding-left:20px; margin-top:30px;
  font-family:"Source Serif 4",Georgia,serif; font-size:19px; line-height:1.5; color:var(--ink);
  max-width:52ch}

footer.foot{border-top:1px solid var(--rule); background:var(--surface); margin-top:0}
footer.foot .wrap{padding:30px 24px 44px; display:grid;
  grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:28px}
footer.foot h4{font-size:11px; text-transform:uppercase; letter-spacing:.09em; color:var(--muted);
  margin-bottom:8px}
footer.foot p{font-size:12.5px; color:var(--ink-2); line-height:1.6}
footer.foot code{font-family:"IBM Plex Mono",monospace; font-size:11.5px; color:var(--accent)}


/* ---------- novos componentes ---------- */
.subhead{font-size:13px; text-transform:uppercase; letter-spacing:.1em; color:var(--muted);
  font-weight:700; margin:44px 0 16px; padding-bottom:9px; border-bottom:1px solid var(--rule)}
.subhead.sm{margin:0 0 10px; border:0; padding:0; font-size:12.5px}
.note{font-size:12.5px; color:var(--muted); line-height:1.55; margin-top:11px}
.note.wide{max-width:74ch; margin-top:14px; font-size:13px}
.prose.sm{font-size:15.5px}
.fourup{display:grid; grid-template-columns:repeat(auto-fit,minmax(238px,1fr)); gap:34px; margin-top:44px}

/* grade de pontos por posição */
.grade{display:grid; grid-template-columns:repeat(auto-fit,minmax(66px,1fr)); gap:5px; margin-top:4px}
.gp{background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:8px 4px 7px;
  text-align:center; display:flex; flex-direction:column; gap:1px}
.gp-pos{font-size:10.5px; color:var(--muted); font-family:"IBM Plex Mono",monospace; letter-spacing:.02em}
.gp-pts{font-family:"IBM Plex Mono",monospace; font-size:17px; font-weight:600; color:var(--ink);
  font-variant-numeric:tabular-nums; letter-spacing:-.02em}
.gp.sc{background:var(--accent-soft); border-color:color-mix(in srgb,var(--accent) 24%,transparent)}
.gp.sc .gp-pts{color:var(--accent)}
.gp.top{border-color:var(--accent)}
.gp.resto{background:var(--surface-2); border-style:dashed}
.gp.resto .gp-pts{color:var(--muted)}

/* bônus */
.bonuslist{display:grid; grid-template-columns:repeat(auto-fit,minmax(272px,1fr)); gap:10px; margin-top:22px}
.bonus{background:var(--surface); padding:13px 15px; display:flex; gap:13px; align-items:flex-start;
  border:1px solid var(--rule); border-radius:3px}
.bonus .bv{font-family:"IBM Plex Mono",monospace; font-weight:600; font-size:14px; color:var(--accent);
  min-width:38px; text-align:right; font-variant-numeric:tabular-nums; flex:none; padding-top:1px}
.bonus > span:last-child{display:flex; flex-direction:column; gap:2px}
.bonus b{font-size:13.5px; font-weight:600}
.bonus span span{font-size:12.5px; color:var(--muted); line-height:1.45}

/* linha do tempo da regra */
.timeline{display:grid; grid-template-columns:repeat(auto-fit,minmax(232px,1fr)); gap:12px; margin-top:20px}
.era{border:1px solid var(--rule); border-radius:3px; padding:15px 17px 16px; background:var(--surface);
  border-top:2px solid var(--rule-2)}
.era.now{border-top-color:var(--accent); background:var(--surface)}
.era > b{display:block; font-size:16px; margin:6px 0 7px; letter-spacing:-.012em}
.era p b{font-weight:600; color:var(--ink)}
.era p{font-size:13.5px; color:var(--ink-2); line-height:1.56}
.era.now > b{color:var(--accent)}

.syscard.base{border-color:var(--accent)}
.syscard.base .tag{color:var(--accent)}
.matrix thead th .sub.mark{color:var(--gold); font-weight:600}
.matrix thead th.ruler .sub.mark{color:var(--accent)}
.stagelist.legenda{margin-top:13px; padding-top:11px; border-top:1px solid var(--rule)}
.grid2 td.yr .mini{display:block; font-family:"Archivo",sans-serif; font-size:10px; font-weight:600;
  color:var(--gold); letter-spacing:.04em; margin-top:2px}


/* ---------- aba de abertura: as réguas ---------- */
.reguas{display:flex; flex-direction:column; gap:14px; margin-top:28px}
.regua{display:grid; grid-template-columns:74px minmax(0,1fr); gap:4px;
  background:var(--surface); border:1px solid var(--rule); border-radius:3px; overflow:hidden}
.regua.base{border-color:var(--accent)}
.rnum{background:var(--surface-2); display:flex; flex-direction:column; align-items:center;
  justify-content:flex-start; gap:7px; padding:17px 8px; border-right:1px solid var(--rule)}
.rnum > span:first-child{font-family:"IBM Plex Mono",monospace; font-size:20px; font-weight:600;
  color:var(--muted); letter-spacing:-.03em; line-height:1}
.regua.base .rnum{background:var(--accent-soft); border-right-color:var(--accent)}
.regua.base .rnum > span:first-child{color:var(--accent)}
.rbadge{font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:.08em;
  color:var(--accent); border:1px solid var(--accent); border-radius:2px; padding:1px 5px}
.rbody{padding:17px 20px 18px; min-width:0; display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,280px); gap:6px 28px;
  grid-template-areas:"h h" "f f" "p e"; align-content:start}
.rbody h3{grid-area:h}
.rbody .formula{grid-area:f}
.rbody > p{grid-area:p}
.rbody .exemplo{grid-area:e; align-self:start}
.rbody h3{font-size:19px; letter-spacing:-.018em; margin-bottom:7px}
.rbody .formula{margin:0 0 12px; padding:0}
.rbody > p{font-family:"Source Serif 4",Georgia,serif; font-size:16px; line-height:1.62;
  color:var(--ink-2); max-width:74ch}
.rbody > p b{color:var(--ink); font-weight:600}
.exemplo{margin-top:8px; padding:12px 15px; background:var(--surface-2); border-radius:3px;
  border-left:2px solid var(--rule-2); font-size:13.5px; line-height:1.55; color:var(--ink-2);
  max-width:80ch}
.regua.base .exemplo{border-left-color:var(--accent)}
.exlabel{display:block; font-size:9.5px; font-weight:700; text-transform:uppercase;
  letter-spacing:.1em; color:var(--muted); margin-bottom:4px; font-family:"Archivo",sans-serif}

/* guia de leitura */
.guia{display:grid; grid-template-columns:repeat(auto-fit,minmax(258px,1fr)); gap:12px; margin-top:20px}
.gitem{display:flex; gap:13px; align-items:flex-start; background:var(--surface);
  border:1px solid var(--rule); border-radius:3px; padding:13px 15px}
.gic{flex:none; width:34px; display:flex; align-items:center; justify-content:center; padding-top:2px}
.gitem b{font-size:13.5px; display:block; margin-bottom:3px}
.gitem p{font-size:12.5px; color:var(--muted); line-height:1.5}
.gnum{font-family:"IBM Plex Mono",monospace; font-size:11.5px; color:var(--muted);
  font-variant-numeric:tabular-nums}


/* histórico dos multiplicadores */
.hist{display:flex; flex-direction:column; gap:1px; margin-top:20px; background:var(--rule);
  border:1px solid var(--rule); border-radius:3px; overflow:hidden}
.hitem{background:var(--surface); padding:14px 17px; display:grid;
  grid-template-columns:150px minmax(0,1fr); gap:20px; align-items:start}
.hitem.atual{background:var(--accent-soft)}
.hmeta{display:flex; flex-direction:column; gap:2px}
.hcat{font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.09em; color:var(--muted)}
.hano{font-family:"IBM Plex Mono",monospace; font-size:14px; font-weight:600; color:var(--ink);
  font-variant-numeric:tabular-nums; letter-spacing:-.01em}
.hitem.atual .hano, .hitem.atual .hcat{color:var(--accent)}
.hitem > div > b{font-size:14px; display:block; margin-bottom:3px; letter-spacing:-.01em}
.hitem p b{font-weight:600; color:var(--ink)}
.hitem p{font-size:13px; color:var(--ink-2); line-height:1.55; max-width:78ch}
@media (max-width:620px){ .hitem{grid-template-columns:1fr; gap:6px} }

@media (max-width:860px){
  .rbody{grid-template-columns:1fr; grid-template-areas:"h" "f" "p" "e"}
  .rbody .exemplo{margin-top:14px}
}
@media (max-width:640px){
  .regua{grid-template-columns:1fr}
  .rnum{flex-direction:row; justify-content:flex-start; padding:9px 16px;
    border-right:0; border-bottom:1px solid var(--rule)}
  .regua.base .rnum{border-right:0; border-bottom-color:var(--accent)}
}

@media (max-width:900px){
  .mast-grid{grid-template-columns:1fr; gap:26px; align-items:start}
  .analysis{grid-template-columns:1fr; gap:26px}
  h1{font-size:32px}
}
@media (prefers-reduced-motion:reduce){*{transition:none !important; animation:none !important}}
"""
import pathlib
pathlib.Path(__file__).resolve().with_name("style.css").write_text(CSS, encoding="utf-8")
print(len(CSS), "bytes de CSS")
