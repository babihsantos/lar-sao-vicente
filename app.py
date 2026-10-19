<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lar São Vicente — Doações</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(-45deg, #0a0a1a, #111827, #1a0b2e, #061a17);
    background-size: 400% 400%;
    animation: bgShift 20s ease infinite;
    color: #e2e8f0;
    min-height: 100vh;
  }
  @keyframes bgShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  .layout { display: flex; min-height: 100vh; }
  /* SIDEBAR */
  .sidebar {
    width: 280px; flex-shrink: 0;
    background: linear-gradient(160deg, #0f172a 0%, #1e1b4b 50%, #4c1d95 100%);
    border-right: 1px solid rgba(255,255,255,0.06);
    padding: 1.5rem 1rem; position: sticky; top: 0; height: 100vh; overflow-y: auto;
  }
  .sidebar h2 {
    margin: 0 0 .25rem 0; font-weight: 900;
    background: linear-gradient(90deg, #67e8f9, #a78bfa);
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
  }
  .sidebar .cap { font-size: .8rem; opacity: .7; margin-bottom: 1rem; }
  .sidebar hr { border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 1rem 0; }
  .menu-btn {
    display: block; width: 100%; text-align: left; background: transparent;
    color: #e2e8f0; border: none; padding: .6rem .8rem; border-radius: 10px;
    font-family: inherit; font-size: .92rem; font-weight: 600; cursor: pointer;
    transition: all .2s; margin-bottom: .15rem;
  }
  .menu-btn:hover { background: rgba(255,255,255,0.08); }
  .menu-btn.active { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: #fff; box-shadow: 0 4px 14px rgba(139,92,246,0.35); }
  .sidebar .foot { font-size: .75rem; opacity: .7; margin-top: .4rem; }
  .btn-reload {
    width: 100%; margin-top: .5rem; padding: .55rem; border-radius: 10px; border: none;
    background: linear-gradient(135deg, #6366f1, #8b5cf6); color: #fff;
    font-weight: 700; font-family: inherit; cursor: pointer; transition: all .2s;
  }
  .btn-reload:hover { transform: translateY(-2px); box-shadow: 0 8px 22px rgba(139,92,246,0.5); }
  /* MAIN */
  .main { flex: 1; padding: 1.5rem 2rem 3rem; max-width: 1450px; }
  /* HERO */
  .hero {
    position: relative; padding: 2.4rem 2.6rem; border-radius: 26px;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
    background-size: 200% 200%; animation: gradMove 10s ease infinite;
    color: #fff; margin-bottom: 1.8rem; overflow: hidden;
    box-shadow: 0 20px 50px rgba(168,85,247,0.45);
  }
  @keyframes gradMove { 0%{background-position:0% 50%;} 50%{background-position:100% 50%;} 100%{background-position:0% 50%;} }
  .hero::before, .hero::after {
    content: ""; position: absolute; border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.22), transparent 65%);
  }
  .hero::before { top: -30%; right: -5%; width: 420px; height: 420px; animation: float 8s ease-in-out infinite; }
  .hero::after { bottom: -40%; left: -5%; width: 320px; height: 320px; background: radial-gradient(circle, rgba(255,255,255,0.15), transparent 65%); animation: float 10s ease-in-out infinite reverse; }
  @keyframes float { 0%,100%{transform:translateY(0) translateX(0);} 50%{transform:translateY(-24px) translateX(18px);} }
  .hero h1 { margin: 0; font-size: 2.3rem; font-weight: 900; letter-spacing: -1px; line-height: 1.1; position: relative; z-index: 1; }
  .hero .sub { opacity: .96; margin-top: .55rem; font-size: 1.05rem; font-weight: 500; position: relative; z-index: 1; }
  .hero .meta { margin-top: 1.3rem; font-size: .88rem; font-weight: 600; display: flex; gap: 1.6rem; flex-wrap: wrap; position: relative; z-index: 1; }
  .hero .meta span {
    display: inline-flex; align-items: center; gap: .4rem;
    background: rgba(255,255,255,0.15); padding: .4rem .9rem; border-radius: 999px;
    backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);
  }
  /* SECTION TITLE */
  .section-title {
    font-size: 1.35rem; font-weight: 900; color: #f1f5f9;
    margin: 2rem 0 1rem 0; display: flex; align-items: center; gap: .7rem; letter-spacing: -.3px;
  }
  .section-title::before {
    content: ""; width: 6px; height: 26px; border-radius: 4px;
    background: linear-gradient(180deg, #6366f1, #ec4899);
    box-shadow: 0 0 12px rgba(99,102,241,.8);
  }
  /* KPI */
  .kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 1rem; }
  .kpi {
    position: relative; background: rgba(30,41,59,0.55); backdrop-filter: blur(20px);
    padding: 1.2rem 1.3rem; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,.4);
    border: 1px solid rgba(148,163,184,.12); overflow: hidden; transition: all .25s;
  }
  .kpi::before { content: ""; position: absolute; top:0; left:0; right:0; height: 4px; background: var(--grad); }
  .kpi:hover { transform: translateY(-6px) scale(1.02); box-shadow: 0 18px 45px rgba(0,0,0,.6); }
  .kpi .icon { font-size: 1.9rem; }
  .kpi .label { font-size: .74rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; margin-top: .55rem; }
  .kpi .value {
    font-size: 2rem; font-weight: 900; margin-top: .2rem; line-height: 1.05;
    background: var(--grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
  }
  .kpi .delta { font-size: .78rem; color: #64748b; margin-top: .35rem; font-weight: 500; }
  /* ALERTS */
  .alert-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: .8rem; }
  .alert {
    padding: 1.2rem 1.3rem; border-radius: 18px; display: flex; align-items: center; gap: 1.1rem;
    font-weight: 600; box-shadow: 0 6px 20px rgba(0,0,0,.3); transition: transform .2s;
  }
  .alert:hover { transform: translateY(-3px); }
  .alert .icon { font-size: 2.1rem; }
  .alert .count { font-size: 1.6rem; font-weight: 900; line-height: 1; }
  .alert .txt { font-size: .85rem; font-weight: 500; opacity: .9; margin-top: .15rem; }
  .alert.danger { background: linear-gradient(135deg, rgba(220,38,38,.25), rgba(127,29,29,.35)); border-left: 6px solid #dc2626; color: #fecaca; }
  .alert.warn { background: linear-gradient(135deg, rgba(245,158,11,.25), rgba(120,53,15,.35)); border-left: 6px solid #f59e0b; color: #fde68a; }
  .alert.ok { background: linear-gradient(135deg, rgba(16,185,129,.25), rgba(20,83,45,.35)); border-left: 6px solid #16a34a; color: #bbf7d0; }
  .alert.info { background: linear-gradient(135deg, rgba(37,99,235,.25), rgba(30,58,138,.35)); border-left: 6px solid #2563eb; color: #bfdbfe; }
  /* CARD */
  .card {
    background: rgba(30,41,59,0.55); backdrop-filter: blur(20px);
    border-radius: 20px; padding: 1.3rem 1.4rem; box-shadow: 0 8px 30px rgba(0,0,0,.4);
    border: 1px solid rgba(148,163,184,.12); transition: all .25s;
  }
  .card:hover { box-shadow: 0 14px 40px rgba(0,0,0,.6); }
  .card h4 { margin: 0 0 .8rem 0; color: #f1f5f9; font-size: 1.05rem; font-weight: 800; }
  .grid-2 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 1rem; }
  .grid-2b { display: grid; grid-template-columns: 1.4fr 1fr; gap: 1rem; }
  @media (max-width: 900px) { .grid-2, .grid-2b { grid-template-columns: 1fr; } .layout { flex-direction: column; } .sidebar { width: 100%; height: auto; position: static; } }
  /* TIMELINE */
  .timeline { position: relative; padding-left: 1.5rem; }
  .timeline::before { content: ""; position: absolute; left: 7px; top: 4px; bottom: 4px; width: 2px; background: linear-gradient(180deg, #6366f1, #ec4899, transparent); border-radius: 2px; }
  .tl-item {
    position: relative; margin-bottom: 1rem; background: rgba(30,41,59,0.55);
    padding: .85rem 1rem; border-radius: 14px; box-shadow: 0 4px 14px rgba(0,0,0,.35);
    border: 1px solid rgba(148,163,184,.12); transition: transform .2s;
  }
  .tl-item:hover { transform: translateX(6px); }
  .tl-item::before { content: ""; position: absolute; left: -1.25rem; top: 18px; width: 14px; height: 14px; border-radius: 50%; background: var(--dot); border: 3px solid #0f172a; box-shadow: 0 0 0 3px var(--dot), 0 0 16px var(--dot); }
  .tl-item .t { font-size: .74rem; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: .5px; }
  .tl-item .h { font-weight: 800; color: #f1f5f9; margin-top: .2rem; font-size: .95rem; }
  .tl-item .d { font-size: .82rem; color: #cbd5e1; margin-top: .15rem; }
  /* BADGE */
  .badge { display: inline-block; padding: .2rem .65rem; border-radius: 999px; font-size: .72rem; font-weight: 800; text-transform: uppercase; letter-spacing: .5px; }
  .badge.in { background: rgba(16,185,129,.25); color: #6ee7b7; }
  .badge.out { background: rgba(239,68,68,.25); color: #fca5a5; }
  .badge.del { background: rgba(100,116,139,.25); color: #cbd5e1; }
  .badge.edit { background: rgba(245,158,11,.25); color: #fcd34d; }
  /* RANK */
  .rank-row { display: flex; justify-content: space-between; align-items: center; padding: .7rem .5rem; border-bottom: 1px solid rgba(148,163,184,.12); border-radius: 8px; transition: background .15s; }
  .rank-row:hover { background: rgba(99,102,241,.12); }
  .rank-row:last-child { border-bottom: none; }
  .rank-row .medal { font-size: 1.3rem; margin-right: .6rem; }
  .rank-row .val { font-weight: 900; font-size: 1rem; background: linear-gradient(90deg, #818cf8, #f472b6); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
  .rank-row .nm { font-weight: 700; color: #f1f5f9; }
  .rank-row .cat { font-size: .75rem; color: #94a3b8; }
  /* FORM / INPUTS */
  .form-card { background: rgba(30,41,59,.35); border: 1px solid rgba(148,163,184,.15); border-radius: 20px; padding: 1.2rem 1.4rem; backdrop-filter: blur(20px); }
  label.fld { display: block; font-size: .8rem; color: #cbd5e1; font-weight: 600; margin: .6rem 0 .25rem; }
  input[type=text], input[type=number], input[type=date], select, textarea {
    width: 100%; background: #1e293b; color: #e2e8f0; border: 1px solid #334155;
    border-radius: 10px; padding: .55rem .7rem; font-family: inherit; font-size: .92rem;
  }
  input:focus, select:focus, textarea:focus { outline: none; border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99,102,241,.25); }
  input:disabled { opacity: .5; }
  .chk { display: flex; align-items: center; gap: .5rem; font-size: .9rem; color: #cbd5e1; margin: .5rem 0; }
  .grid-form { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
  @media (max-width: 700px) { .grid-form { grid-template-columns: 1fr; } }
  .btn {
    border-radius: 12px; font-weight: 700; font-family: inherit; cursor: pointer;
    border: none; padding: .65rem 1.2rem; font-size: .92rem; transition: all .2s;
  }
  .btn-primary { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: #fff; box-shadow: 0 4px 14px rgba(99,102,241,.4); }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 22px rgba(99,102,241,.6); }
  .btn-green { background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 14px rgba(16,185,129,.4); }
  .btn-red { background: linear-gradient(135deg, #ef4444, #ec4899); color: #fff; box-shadow: 0 4px 14px rgba(239,68,68,.4); }
  .btn:disabled { opacity: .4; cursor: not-allowed; transform: none !important; }
  .btn-block { width: 100%; }
  /* TABLE */
  .tbl-wrap { border-radius: 16px; overflow: auto; box-shadow: 0 6px 20px rgba(0,0,0,.4); border: 1px solid rgba(148,163,184,.15); background: rgba(30,41,59,.55); }
  table { width: 100%; border-collapse: collapse; font-size: .85rem; }
  thead th { background: rgba(99,102,241,.25); color: #e2e8f0; text-align: left; padding: .7rem .8rem; font-weight: 800; position: sticky; top: 0; }
  tbody td { padding: .6rem .8rem; border-top: 1px solid rgba(148,163,184,.12); color: #cbd5e1; }
  tbody tr:nth-child(even) { background: rgba(15,23,42,.3); }
  tbody tr:hover { background: rgba(99,102,241,.12); }
  .empty { text-align: center; padding: 2rem; color: #94a3b8; }
  /* MSG */
  .msg { padding: .8rem 1rem; border-radius: 12px; font-weight: 600; margin: .6rem 0; }
  .msg.ok { background: rgba(16,185,129,.2); color: #6ee7b7; border-left: 4px solid #10b981; }
  .msg.err { background: rgba(239,68,68,.2); color: #fca5a5; border-left: 4px solid #ef4444; }
  .msg.warn { background: rgba(245,158,11,.2); color: #fde68a; border-left: 4px solid #f59e0b; }
  .msg.info { background: rgba(37,99,235,.2); color: #bfdbfe; border-left: 4px solid #2563eb; }
  /* CANVAS */
  canvas { max-width: 100%; }
  .toolbar { display: flex; gap: .6rem; flex-wrap: wrap; margin: .8rem 0; }
  /* TABS */
  .tabs { display: flex; gap: .5rem; background: rgba(30,41,59,.5); padding: .4rem; border-radius: 14px; backdrop-filter: blur(10px); margin-bottom: 1rem; flex-wrap: wrap; }
  .tab { border-radius: 10px; font-weight: 700; padding: .5rem 1rem; color: #cbd5e1; background: transparent; border: none; font-family: inherit; cursor: pointer; font-size: .9rem; }
  .tab.active { background: linear-gradient(135deg, #6366f1, #a855f7); color: #fff; }
  .hidden { display: none !important; }
  @media print {
    .sidebar, .hero, .no-print { display: none !important; }
    body { background: #fff !important; color: #000 !important; }
    .main { padding: 0; }
    .card, .tbl-wrap { box-shadow: none; border: 1px solid #ccc; background: #fff; }
    thead th { background: #e5e7eb !important; color: #000 !important; }
    tbody td { color: #000 !important; }
  }
</style>
</head>
<body>
<div class="layout">
  <!-- SIDEBAR -->
  <aside class="sidebar">
    <h2>💚 Lar São Vicente</h2>
    <div class="cap">Painel de gestão</div>
    <hr>
    <nav id="menu"></nav>
    <hr>
    <button class="btn-reload" onclick="recarregar()">🔄 Recarregar dados</button>
    <div class="foot" id="clock">🕐 --:--:-- · Brasília</div>
    <div class="foot">💾 Dados no navegador</div>
  </aside>

  <!-- MAIN -->
  <main class="main">
    <div class="hero">
      <h1>💚 Lar São Vicente de Paulo</h1>
      <div class="sub">Sistema de Controlo de Doações &amp; Inventário · São José do Rio Preto</div>
      <div class="meta">
        <span id="hero-clock">🕐 --</span>
        <span>💾 LocalStorage</span>
        <span>✨ Tempo real</span>
      </div>
    </div>
    <div id="view"></div>
  </main>
</div>

<script>
/* =========================================================
   CONFIG
========================================================= */
const DIAS_ALERTA = 30;
const CATEGORIAS_PADRAO = ["Alimentação","Higiene Pessoal","Limpeza","Medicamentos","Vestuário","Outros"];
const LS_INV = "lsv_inventario_v1";
const LS_MOV = "lsv_movimentos_v1";
const GRAD = {
  azul: "linear-gradient(90deg, #3b82f6, #06b6d4)",
  roxo: "linear-gradient(90deg, #8b5cf6, #d946ef)",
  verde: "linear-gradient(90deg, #10b981, #84cc16)",
  laranja: "linear-gradient(90deg, #f59e0b, #ef4444)",
  vermelho: "linear-gradient(90deg, #ef4444, #ec4899)",
  rosa: "linear-gradient(90deg, #ec4899, #8b5cf6)",
};
const MENU = [
  { id: "dashboard", icon: "📊", label: "Dashboard" },
  { id: "doacao", icon: "📦", label: "Registar Doação" },
  { id: "inventario", icon: "🔍", label: "Inventário" },
  { id: "baixa", icon: "📤", label: "Dar Baixa" },
  { id: "validade", icon: "⚠️", label: "Alertas de Validade" },
  { id: "estoque", icon: "📉", label: "Estoque Baixo" },
  { id: "doadores", icon: "👥", label: "Doadores" },
  { id: "relatorios", icon: "📈", label: "Relatórios" },
  { id: "historico", icon: "🕓", label: "Histórico" },
  { id: "apagar", icon: "🗑️", label: "Apagar Item" },
];

/* =========================================================
   HELPERS
========================================================= */
function agoraBR() {
  return new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
}
function fmtDataHora(d) {
  const dt = new Date(d);
  if (isNaN(dt)) return "—";
  return dt.toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo", day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit" });
}
function fmtDataCurta(d) {
  const dt = new Date(d);
  if (isNaN(dt)) return "—";
  return dt.toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo", day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit" });
}
function isoAgora() {
  const now = new Date();
  const br = new Date(now.toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
  const pad = n => String(n).padStart(2, "0");
  return `${br.getFullYear()}-${pad(br.getMonth()+1)}-${pad(br.getDate())}T${pad(br.getHours())}:${pad(br.getMinutes())}:${pad(br.getSeconds())}`;
}
function hojeISO() {
  const br = new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
  const pad = n => String(n).padStart(2, "0");
  return `${br.getFullYear()}-${pad(br.getMonth()+1)}-${pad(br.getDate())}`;
}
function addDias(dias) {
  const d = new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
  d.setDate(d.getDate() + dias);
  const pad = n => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}
function uid() {
  return "id-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 9);
}
function esc(s) { return String(s ?? "").replace(/[&<>"']/g, c => ({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[c])); }
function num(v) { const n = Number(v); return isNaN(n) ? 0 : n; }
function numFmt(n) { return num(n).toLocaleString("pt-BR"); }

function statusValidade(v) {
  if (!v) return "Sem validade";
  const d = new Date(v + "T00:00:00");
  if (isNaN(d)) return "Inválida";
  const hoje = new Date(hojeISO() + "T00:00:00");
  const diff = (d - hoje) / 86400000;
  if (diff < 0) return "Vencido";
  if (diff <= DIAS_ALERTA) return "A vencer";
  return "OK";
}
function badge(tipo) {
  const cls = { "Entrada":"in", "Saída":"out", "Eliminação":"del", "Edição":"edit" }[tipo] || "del";
  return `<span class="badge ${cls}">${esc(tipo)}</span>`;
}
function kpiCard(icon, label, value, grad, extra="") {
  return `<div class="kpi" style="--grad:${grad}">
    <div class="icon">${icon}</div>
    <div class="label">${esc(label)}</div>
    <div class="value">${value}</div>
    <div class="delta">${esc(extra)}</div>
  </div>`;
}
function alertCard(kind, icon, count, text) {
  return `<div class="alert ${kind}">
    <div class="icon">${icon}</div>
    <div><div class="count">${count}</div><div class="txt">${esc(text)}</div></div>
  </div>`;
}
function sectionTitle(t) { return `<div class="section-title">${t}</div>`; }
function msg(kind, text) { return `<div class="msg ${kind}">${text}</div>`; }

/* =========================================================
   STORAGE
========================================================= */
function loadInv() {
  try { return JSON.parse(localStorage.getItem(LS_INV)) || []; } catch { return []; }
}
function saveInv(v) { localStorage.setItem(LS_INV, JSON.stringify(v)); }
function loadMov() {
  try { return JSON.parse(localStorage.getItem(LS_MOV)) || []; } catch { return []; }
}
function saveMov(v) { localStorage.setItem(LS_MOV, JSON.stringify(v)); }
function recarregar() { render(currentView); }

/* =========================================================
   CRUD
========================================================= */
function registarEntrada(item, categoria, quantidade, validade, doador, estoque_minimo) {
  const inv = loadInv();
  const mov = loadMov();
  const idx = inv.findIndex(i => i.item.toLowerCase() === item.trim().toLowerCase() && (i.validade || "") === (validade || ""));
  if (idx >= 0) {
    inv[idx].quantidade = num(inv[idx].quantidade) + num(quantidade);
    inv[idx].estoque_minimo = num(estoque_minimo);
  } else {
    inv.push({
      id: uid(), item: item.trim(), categoria, quantidade: num(quantidade),
      validade: validade || "", doador: (doador || "").trim() || "Anónimo",
      estoque_minimo: num(estoque_minimo), data_entrada: isoAgora(),
    });
  }
  mov.push({
    id: uid(), data: isoAgora(), tipo: "Entrada", item: item.trim(),
    categoria, quantidade: num(quantidade), pessoa: (doador || "").trim() || "Anónimo",
    observacoes: "Doação registada",
  });
  saveInv(inv); saveMov(mov);
}
function atualizarItem(id, item, categoria, qtd, validade, doador, minimo) {
  const inv = loadInv(); const mov = loadMov();
  const it = inv.find(i => i.id === id);
  if (!it) return;
  it.item = item.trim(); it.categoria = categoria; it.quantidade = num(qtd);
  it.validade = validade || ""; it.doador = (doador || "").trim() || "Anónimo";
  it.estoque_minimo = num(minimo);
  mov.push({
    id: uid(), data: isoAgora(), tipo: "Edição", item: it.item, categoria,
    quantidade: num(qtd), pessoa: "Sistema", observacoes: "Item editado",
  });
  saveInv(inv); saveMov(mov);
}
function darBaixa(id, qtd, destino, obs) {
  const inv = loadInv(); const mov = loadMov();
  const idx = inv.findIndex(i => i.id === id);
  if (idx < 0) return { ok: false, msg: "Item não encontrado." };
  const it = inv[idx];
  if (num(qtd) > num(it.quantidade)) return { ok: false, msg: `Stock insuficiente (disponível: ${it.quantidade}).` };
  it.quantidade = num(it.quantidade) - num(qtd);
  if (it.quantidade === 0) inv.splice(idx, 1);
  mov.push({
    id: uid(), data: isoAgora(), tipo: "Saída", item: it.item, categoria: it.categoria,
    quantidade: num(qtd), pessoa: (destino || "").trim() || "—",
    observacoes: (obs || "").trim() || "Baixa de stock",
  });
  saveInv(inv); saveMov(mov);
  return { ok: true, msg: "Baixa registada." };
}
function apagarItem(id) {
  const inv = loadInv(); const mov = loadMov();
  const idx = inv.findIndex(i => i.id === id);
  if (idx < 0) return { ok: false, msg: "Item não encontrado." };
  const it = inv[idx];
  inv.splice(idx, 1);
  mov.push({
    id: uid(), data: isoAgora(), tipo: "Eliminação", item: it.item, categoria: it.categoria,
    quantidade: num(it.quantidade), pessoa: "Sistema", observacoes: "Item eliminado",
  });
  saveInv(inv); saveMov(mov);
  return { ok: true, msg: "Item eliminado." };
}

/* =========================================================
   TABELAS
========================================================= */
function renderTabela(arr, opts = {}) {
  if (!arr || !arr.length) return `<div class="empty">Sem registos.</div>`;
  const cols = opts.cols || Object.keys(arr[0]).filter(k => k !== "id");
  const labels = opts.labels || {};
  let html = `<div class="tbl-wrap"><table><thead><tr>`;
  html += cols.map(c => `<th>${esc(labels[c] || c)}</th>`).join("");
  html += `</tr></thead><tbody>`;
  arr.forEach(r => {
    html += "<tr>" + cols.map(c => {
      let v = r[c];
      if (c === "validade" || c === "data") v = v ? fmtDataHora(v) : "—";
      if (c === "Estado") {
        const cls = v === "Vencido" ? "out" : v === "A vencer" ? "edit" : v === "OK" ? "in" : "del";
        return `<td><span class="badge ${cls}">${esc(v)}</span></td>`;
      }
      return `<td>${esc(v ?? "")}</td>`;
    }).join("") + "</tr>";
  });
  html += `</tbody></table></div>`;
  return html;
}

/* =========================================================
   GRÁFICOS (Canvas puro)
========================================================= */
function drawBarH(canvas, labels, values, colors) {
  const ctx = canvas.getContext("2d");
  const dpr = window.devicePixelRatio || 1;
  const W = canvas.clientWidth || 600, H = canvas.height;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + "px"; canvas.style.height = H + "px";
  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, W, H);
  const pad = { l: 130, r: 60, t: 10, b: 20 };
  const max = Math.max(1, ...values);
  const rowH = (H - pad.t - pad.b) / labels.length;
  const barH = Math.min(28, rowH * 0.6);
  ctx.font = "12px Inter, sans-serif";
  labels.forEach((lb, i) => {
    const y = pad.t + i * rowH + rowH / 2;
    const v = values[i];
    const w = (v / max) * (W - pad.l - pad.r);
    ctx.fillStyle = "#cbd5e1"; ctx.textAlign = "right"; ctx.textBaseline = "middle";
    ctx.fillText(String(lb).slice(0, 18), pad.l - 10, y);
    const grad = ctx.createLinearGradient(pad.l, 0, pad.l + w, 0);
    grad.addColorStop(0, colors[0] || "#6366f1");
    grad.addColorStop(1, colors[1] || "#ec4899");
    ctx.fillStyle = grad;
    roundRect(ctx, pad.l, y - barH / 2, Math.max(2, w), barH, 6);
    ctx.fill();
    ctx.fillStyle = "#f1f5f9"; ctx.textAlign = "left";
    ctx.fillText(String(v), pad.l + w + 8, y);
  });
}
function drawDonut(canvas, labels, values, colors) {
  const ctx = canvas.getContext("2d");
  const dpr = window.devicePixelRatio || 1;
  const W = canvas.clientWidth || 400, H = canvas.height;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + "px"; canvas.style.height = H + "px";
  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, W, H);
  const cx = W / 2, cy = H / 2 - 10, R = Math.min(W, H) / 2 - 30, r = R * 0.55;
  const total = values.reduce((a, b) => a + b, 0) || 1;
  let ang = -Math.PI / 2;
  labels.forEach((lb, i) => {
    const slice = (values[i] / total) * Math.PI * 2;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.arc(cx, cy, R, ang, ang + slice);
    ctx.closePath();
    ctx.fillStyle = colors[i % colors.length];
    ctx.fill();
    ang += slice;
  });
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.fillStyle = "#0f172a";
  ctx.fill();
  ctx.fillStyle = "#f1f5f9"; ctx.font = "bold 14px Inter, sans-serif"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
  ctx.fillText("Total", cx, cy - 10);
  ctx.font = "bold 20px Inter, sans-serif";
  ctx.fillText(String(total), cx, cy + 12);
  // legend
  let ly = H - 40;
  let lx = 10;
  ctx.font = "11px Inter, sans-serif"; ctx.textAlign = "left"; ctx.textBaseline = "middle";
  labels.forEach((lb, i) => {
    const txt = `${lb} (${values[i]})`;
    const w = ctx.measureText(txt).width + 30;
    if (lx + w > W) { lx = 10; ly += 18; }
    ctx.fillStyle = colors[i % colors.length];
    ctx.fillRect(lx, ly - 5, 10, 10);
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(txt, lx + 14, ly);
    lx += w;
  });
}
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

/* =========================================================
   VIEWS
========================================================= */
let currentView = "dashboard";

function renderDashboard() {
  const inv = loadInv(); const mov = loadMov();
  if (!inv.length) return msg("info", "Ainda não há dados. Vai a <b>📦 Registar Doação</b> para começar.");
  inv.forEach(i => i._status = statusValidade(i.validade));
  const totalUn = inv.reduce((s, i) => s + num(i.quantidade), 0);
  const venc = inv.filter(i => i._status === "Vencido").reduce((s, i) => s + num(i.quantidade), 0);
  const aven = inv.filter(i => i._status === "A vencer").reduce((s, i) => s + num(i.quantidade), 0);
  const baixo = inv.filter(i => num(i.quantidade) <= num(i.estoque_minimo)).length;
  const totalDoa = mov.filter(m => m.tipo === "Entrada").reduce((s, m) => s + num(m.quantidade), 0);
  const cats = [...new Set(inv.map(i => i.categoria))];

  let html = `<div class="kpi-grid">
    ${kpiCard("📦","Unidades em stock",numFmt(totalUn),GRAD.azul,`${inv.length} lotes`)}
    ${kpiCard("🏷️","Itens distintos",inv.length,GRAD.roxo,`${cats.length} categorias`)}
    ${kpiCard("📥","Doações recebidas",numFmt(totalDoa),GRAD.verde,"histórico total")}
    ${kpiCard("⚠️","A vencer (30d)",numFmt(aven),GRAD.laranja,`${inv.filter(i=>i._status==='A vencer').length} lotes`)}
    ${kpiCard("🚫","Vencidos",numFmt(venc),GRAD.vermelho,`${inv.filter(i=>i._status==='Vencido').length} lotes`)}
    ${kpiCard("📉","Estoque baixo",baixo,GRAD.rosa,"repor urgente")}
  </div>`;

  html += sectionTitle("🚨 Estado do Inventário");
  html += `<div class="alert-grid">
    ${venc > 0 ? alertCard("danger","🚫",inv.filter(i=>i._status==='Vencido').length,"Lotes vencidos — retirar do stock!") : alertCard("ok","✅",0,"Nenhum item vencido")}
    ${aven > 0 ? alertCard("warn","⚠️",inv.filter(i=>i._status==='A vencer').length,`A vencer nos próximos ${DIAS_ALERTA} dias`) : alertCard("ok","✅",0,"Nada a vencer")}
    ${baixo > 0 ? alertCard("warn","📉",baixo,"Itens abaixo do estoque mínimo") : alertCard("ok","✅",0,"Estoque saudável")}
  </div>`;

  // charts
  const porCat = {};
  inv.forEach(i => porCat[i.categoria] = (porCat[i.categoria] || 0) + num(i.quantidade));
  const catLabels = Object.keys(porCat).sort((a, b) => porCat[a] - porCat[b]);
  const catVals = catLabels.map(k => porCat[k]);
  const palette = ["#6366f1","#a855f7","#ec4899","#06b6d4","#10b981","#f59e0b"];

  html += sectionTitle("📊 Análise Visual");
  html += `<div class="grid-2">
    <div class="card"><h4>Stock por categoria</h4><canvas id="chartBar" height="400"></canvas></div>
    <div class="card"><h4>Distribuição</h4><canvas id="chartDonut" height="400"></canvas></div>
  </div>`;

  // timeline + top
  const top = [...inv].sort((a, b) => num(b.quantidade) - num(a.quantidade)).slice(0, 5);
  const medals = ["🥇","🥈","🥉","4️⃣","5️⃣"];
  let tl = "";
  mov.slice().sort((a, b) => (b.data || "").localeCompare(a.data || "")).slice(0, 6).forEach(r => {
    const cor = { "Entrada":"#10b981","Saída":"#ef4444","Eliminação":"#94a3b8","Edição":"#f59e0b" }[r.tipo] || "#6366f1";
    tl += `<div class="tl-item" style="--dot:${cor}">
      <div class="t">${fmtDataCurta(r.data)} ${badge(r.tipo)}</div>
      <div class="h">${esc(r.item)}</div>
      <div class="d">📦 ${num(r.quantidade)} un · 👤 ${esc(r.pessoa || "—")}</div>
    </div>`;
  });
  let rank = "";
  top.forEach((r, i) => {
    rank += `<div class="rank-row">
      <div style="display:flex;align-items:center">
        <span class="medal">${medals[i]}</span>
        <div><div class="nm">${esc(r.item)}</div><div class="cat">${esc(r.categoria)}</div></div>
      </div>
      <div class="val">${num(r.quantidade)}</div>
    </div>`;
  });
  html += sectionTitle("🕓 Atividade Recente");
  html += `<div class="grid-2b">
    <div class="card"><h4>📋 Últimas movimentações</h4><div class="timeline">${tl || '<div class="empty">Sem movimentos.</div>'}</div></div>
    <div class="card"><h4>🏆 Top 5 em stock</h4>${rank || '<div class="empty">Sem dados.</div>'}</div>
  </div>`;

  html += sectionTitle("📋 Inventário Completo");
  html += `<div class="toolbar"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button></div>`;
  html += renderTabela(inv, { cols: ["item","categoria","quantidade","validade","doador","data_entrada","estoque_minimo"], labels: {item:"Item",categoria:"Categoria",quantidade:"Qtd",validade:"Validade",doador:"Doador",data_entrada:"Data Entrada",estoque_minimo:"Est. Mínimo"} });

  // after render, draw charts
  setTimeout(() => {
    const c1 = document.getElementById("chartBar");
    const c2 = document.getElementById("chartDonut");
    if (c1) drawBarH(c1, catLabels, catVals, ["#6366f1", "#ec4899"]);
    if (c2) drawDonut(c2, catLabels, catVals, palette);
  }, 30);

  return html;
}

function renderDoacao() {
  let html = sectionTitle("📦 Registar Nova Doação");
  html += `<div class="form-card">
    <div class="grid-form">
      <div>
        <label class="fld">Nome do Item *</label>
        <input type="text" id="f_item" placeholder="Ex.: Leite, Arroz…">
        <label class="fld">Categoria *</label>
        <select id="f_cat">${CATEGORIAS_PADRAO.map(c => `<option>${c}</option>`).join("")}</select>
        <label class="fld">Quantidade *</label>
        <input type="number" id="f_qtd" min="1" step="1" value="1">
        <label class="fld">Estoque mínimo</label>
        <input type="number" id="f_min" min="0" step="1" value="5">
      </div>
      <div>
        <label class="chk"><input type="checkbox" id="f_temval" checked onchange="document.getElementById('f_val').disabled=!this.checked"> Este item tem validade?</label>
        <label class="fld">Data de Validade</label>
        <input type="date" id="f_val" value="${addDias(90)}">
        <label class="fld">Doador / Origem</label>
        <input type="text" id="f_doador" placeholder="Nome ou 'Anónimo'">
      </div>
    </div>
    <div id="doacao_msg"></div>
    <button class="btn btn-primary btn-block" style="margin-top:1rem" onclick="submitDoacao()">💾 Guardar Registo</button>
  </div>`;
  return html;
}
function submitDoacao() {
  const item = document.getElementById("f_item").value.trim();
  const cat = document.getElementById("f_cat").value;
  const qtd = num(document.getElementById("f_qtd").value);
  const min = num(document.getElementById("f_min").value);
  const temval = document.getElementById("f_temval").checked;
  const val = temval ? document.getElementById("f_val").value : "";
  const doador = document.getElementById("f_doador").value;
  const box = document.getElementById("doacao_msg");
  if (!item) { box.innerHTML = msg("warn", "⚠️ Preenche o <b>Nome do Item</b>."); return; }
  if (qtd <= 0) { box.innerHTML = msg("warn", "⚠️ Quantidade inválida."); return; }
  registarEntrada(item, cat, qtd, val, doador, min);
  box.innerHTML = msg("ok", `✅ '${esc(item)}' registado!`);
  document.getElementById("f_item").value = "";
  document.getElementById("f_qtd").value = 1;
  document.getElementById("f_doador").value = "";
  // refresh dashboard data silently
  currentView = "dashboard";
  document.querySelectorAll(".menu-btn").forEach(b => b.classList.toggle("active", b.dataset.id === "dashboard"));
  render("dashboard");
}

function renderInventario() {
  const inv = loadInv();
  if (!inv.length) return msg("info", "Sem dados.");
  const cats = ["Todas", ...new Set(inv.map(i => i.categoria))].sort();
  let html = sectionTitle("🔍 Consultar / Editar Inventário");
  html += `<div class="form-card" style="margin-bottom:1rem"><div class="grid-form">
    <div><label class="fld">Categoria</label><select id="inv_cat">${cats.map(c=>`<option>${c}</option>`).join("")}</select></div>
    <div><label class="fld">🔎 Pesquisar por nome ou doador</label><input type="text" id="inv_busca" oninput="filtrarInv()"></div>
  </div>
  <div class="grid-form" style="margin-top:.6rem">
    <div><label class="fld">Ordenar por</label><select id="inv_ord" onchange="filtrarInv()"><option>Item</option><option>Quantidade</option><option>Validade</option></select></div>
  </div></div>`;
  html += `<div id="inv_metrics" class="kpi-grid" style="margin-bottom:1rem"></div>`;
  html += `<div id="inv_tabela"></div>`;
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button><button class="btn btn-primary" onclick="exportarCSVInv()">⬇️ Exportar CSV</button></div>`;
  // edit form
  html += `<hr style="border-color:rgba(148,163,184,.15);margin:1.5rem 0">`;
  html += sectionTitle("✏️ Editar item");
  html += `<div class="form-card"><div id="edit_area"></div></div>`;
  setTimeout(filtrarInv, 20);
  return html;
}
function filtrarInv() {
  const inv = loadInv();
  const cat = document.getElementById("inv_cat")?.value || "Todas";
  const busca = (document.getElementById("inv_busca")?.value || "").toLowerCase();
  const ord = document.getElementById("inv_ord")?.value || "Item";
  let df = inv.filter(i => (cat === "Todas" || i.categoria === cat)
    && (!busca || i.item.toLowerCase().includes(busca) || (i.doador||"").toLowerCase().includes(busca)));
  df.sort((a, b) => {
    if (ord === "Quantidade") return num(b.quantidade) - num(a.quantidade);
    if (ord === "Validade") return (a.validade || "9999").localeCompare(b.validade || "9999");
    return a.item.localeCompare(b.item);
  });
  const met = document.getElementById("inv_metrics");
  if (met) met.innerHTML = kpiCard("📦","Itens filtrados",df.length,GRAD.azul) + kpiCard("🔢","Unidades totais",numFmt(df.reduce((s,i)=>s+num(i.quantidade),0)),GRAD.verde);
  const tb = document.getElementById("inv_tabela");
  if (tb) tb.innerHTML = renderTabela(df, { cols: ["item","categoria","quantidade","validade","doador","estoque_minimo"], labels: {item:"Item",categoria:"Categoria",quantidade:"Qtd",validade:"Validade",doador:"Doador",estoque_minimo:"Est. Mínimo"} });
  // edit area
  const area = document.getElementById("edit_area");
  if (!area) return;
  if (!df.length) { area.innerHTML = msg("info", "Sem itens para editar."); return; }
  const opts = df.map(i => `<option value="${i.id}">${esc(i.item)} — ${esc(i.categoria)} | qtd: ${i.quantidade}</option>`).join("");
  area.innerHTML = `<label class="fld">Escolhe o item</label>
    <select id="edit_sel" onchange="carregarEdit()">${opts}</select>
    <div id="edit_form" style="margin-top:1rem"></div>`;
  setTimeout(carregarEdit, 20);
}
function carregarEdit() {
  const id = document.getElementById("edit_sel")?.value;
  const inv = loadInv();
  const it = inv.find(i => i.id === id);
  if (!it) return;
  const box = document.getElementById("edit_form");
  box.innerHTML = `<div class="grid-form">
    <div>
      <label class="fld">Nome</label><input type="text" id="e_item" value="${esc(it.item)}">
      <label class="fld">Categoria</label><select id="e_cat">${CATEGORIAS_PADRAO.map(c=>`<option ${c===it.categoria?"selected":""}>${c}</option>`).join("")}</select>
      <label class="fld">Quantidade</label><input type="number" id="e_qtd" min="0" value="${num(it.quantidade)}">
    </div>
    <div>
      <label class="chk"><input type="checkbox" id="e_temval" ${it.validade?"checked":""} onchange="document.getElementById('e_val').disabled=!this.checked"> Tem validade?</label>
      <label class="fld">Validade</label><input type="date" id="e_val" value="${it.validade||""}" ${it.validade?"":"disabled"}>
      <label class="fld">Doador</label><input type="text" id="e_doador" value="${esc(it.doador||"")}">
      <label class="fld">Estoque mínimo</label><input type="number" id="e_min" min="0" value="${num(it.estoque_minimo)}">
    </div>
  </div>
  <div id="edit_msg"></div>
  <button class="btn btn-primary btn-block" style="margin-top:1rem" onclick="submitEdit('${id}')">💾 Guardar alterações</button>`;
}
function submitEdit(id) {
  const item = document.getElementById("e_item").value.trim();
  const cat = document.getElementById("e_cat").value;
  const qtd = num(document.getElementById("e_qtd").value);
  const temval = document.getElementById("e_temval").checked;
  const val = temval ? document.getElementById("e_val").value : "";
  const doador = document.getElementById("e_doador").value;
  const min = num(document.getElementById("e_min").value);
  if (!item) { document.getElementById("edit_msg").innerHTML = msg("warn", "⚠️ Nome obrigatório."); return; }
  atualizarItem(id, item, cat, qtd, val, doador, min);
  document.getElementById("edit_msg").innerHTML = msg("ok", "✅ Item atualizado!");
  setTimeout(() => render("inventario"), 600);
}
function exportarCSVInv() {
  const inv = loadInv();
  const cols = ["item","categoria","quantidade","validade","doador","estoque_minimo","data_entrada"];
  const rows = [cols.join(",")].concat(inv.map(i => cols.map(c => `"${String(i[c]??"").replace(/"/g,'""')}"`).join(",")));
  const blob = new Blob([rows.join("\n")], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = `inventario_${hojeISO()}.csv`; a.click();
}

function renderBaixa() {
  const inv = loadInv();
  if (!inv.length) return msg("info", "Sem itens em stock.");
  let html = sectionTitle("📤 Registar Saída / Baixa");
  html += `<div class="form-card">
    <label class="fld">Item</label>
    <select id="b_sel" onchange="atualizarMaxBaixa()">${inv.map(i=>`<option value="${i.id}">${esc(i.item)} — ${esc(i.categoria)} | stock: ${i.quantidade}</option>`).join("")}</select>
    <div class="grid-form" style="margin-top:1rem">
      <div>
        <label class="fld">Quantidade *</label>
        <input type="number" id="b_qtd" min="1" value="1" max="${inv[0].quantidade}">
        <label class="fld">Destino / Beneficiário</label>
        <input type="text" id="b_dest">
      </div>
      <div>
        <label class="fld">Observações</label>
        <textarea id="b_obs" rows="4"></textarea>
      </div>
    </div>
    <div id="baixa_msg"></div>
    <button class="btn btn-primary btn-block" style="margin-top:1rem" onclick="submitBaixa()">📤 Confirmar Saída</button>
  </div>`;
  return html;
}
function atualizarMaxBaixa() {
  const id = document.getElementById("b_sel").value;
  const it = loadInv().find(i => i.id === id);
  const inp = document.getElementById("b_qtd");
  if (it && inp) { inp.max = it.quantidade; if (num(inp.value) > it.quantidade) inp.value = it.quantidade; }
}
function submitBaixa() {
  const id = document.getElementById("b_sel").value;
  const qtd = num(document.getElementById("b_qtd").value);
  const dest = document.getElementById("b_dest").value;
  const obs = document.getElementById("b_obs").value;
  const r = darBaixa(id, qtd, dest, obs);
  document.getElementById("baixa_msg").innerHTML = r.ok ? msg("ok", "✅ " + r.msg) : msg("err", "❌ " + r.msg);
  if (r.ok) setTimeout(() => render("baixa"), 700);
}

function renderValidade() {
  const inv = loadInv();
  if (!inv.length) return msg("info", "Sem dados.");
  const venc = [], aven = [], sem = [];
  inv.forEach(i => {
    const s = statusValidade(i.validade);
    if (s === "Vencido") venc.push(i);
    else if (s === "A vencer") aven.push(i);
    else if (s === "Sem validade") sem.push(i);
  });
  let html = sectionTitle("⚠️ Alertas de Validade");
  html += `<div class="kpi-grid">
    ${kpiCard("🚫","Vencidos",venc.length,GRAD.vermelho)}
    ${kpiCard("⚠️",`A vencer (${DIAS_ALERTA}d)`,aven.length,GRAD.laranja)}
    ${kpiCard("❔","Sem validade",sem.length,GRAD.roxo)}
  </div>`;
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button></div>`;
  const cols = ["item","categoria","quantidade","validade","doador"];
  const labels = {item:"Item",categoria:"Categoria",quantidade:"Qtd",validade:"Validade",doador:"Doador"};
  if (venc.length) { html += msg("err", `🚫 <b>${venc.length} lote(s) vencido(s)</b> — retirar do stock!`); html += renderTabela(venc, {cols,labels}); }
  if (aven.length) { html += msg("warn", `⚠️ <b>${aven.length} lote(s) a vencer</b>`); html += renderTabela(aven, {cols,labels}); }
  if (!venc.length && !aven.length) html += msg("ok", "✅ Tudo em ordem!");
  if (sem.length) { html += msg("info", `❔ ${sem.length} sem validade`); html += renderTabela(sem, {cols,labels}); }
  return html;
}

function renderEstoque() {
  const inv = loadInv();
  if (!inv.length) return msg("info", "Sem dados.");
  const baixo = inv.filter(i => num(i.quantidade) <= num(i.estoque_minimo)).sort((a,b)=>num(a.quantidade)-num(b.quantidade));
  let html = sectionTitle("📉 Itens abaixo do estoque mínimo");
  if (!baixo.length) return html + msg("ok", "✅ Nenhum item abaixo do mínimo definido.");
  html += msg("warn", `⚠️ <b>${baixo.length} item(ns)</b> precisam de reposição.`);
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button></div>`;
  html += renderTabela(baixo, { cols:["item","categoria","quantidade","estoque_minimo","doador"], labels:{item:"Item",categoria:"Categoria",quantidade:"Qtd",estoque_minimo:"Est. Mínimo",doador:"Doador"} });
  return html;
}

function renderDoadores() {
  const mov = loadMov();
  if (!mov.length) return msg("info", "Sem movimentos ainda.");
  const ent = mov.filter(m => m.tipo === "Entrada");
  if (!ent.length) return msg("info", "Ainda sem doações registadas.");
  const map = {};
  ent.forEach(m => {
    const k = m.pessoa || "Anónimo";
    if (!map[k]) map[k] = { Doador: k, Doações: 0, Unidades: 0, Última: "" };
    map[k].Doações++; map[k].Unidades += num(m.quantidade);
    if ((m.data || "") > map[k].Última) map[k].Última = m.data;
  });
  const resumo = Object.values(map).sort((a, b) => b.Unidades - a.Unidades);
  let html = sectionTitle("👥 Doadores e Histórico");
  html += `<div class="kpi-grid">
    ${kpiCard("👥","Total doadores",resumo.length,GRAD.azul)}
    ${kpiCard("📦","Unidades doadas",numFmt(resumo.reduce((s,r)=>s+r.Unidades,0)),GRAD.verde)}
    ${kpiCard("📥","Doações totais",numFmt(resumo.reduce((s,r)=>s+r.Doações,0)),GRAD.roxo)}
  </div>`;
  const top10 = resumo.slice(0, 10);
  html += `<div class="grid-2" style="margin-top:1rem">
    <div class="card"><h4>🏆 Top 10 doadores</h4><canvas id="doadoresChart" height="420"></canvas></div>
    <div class="card"><h4>📋 Ranking completo</h4>${renderTabela(resumo)}</div>
  </div>`;
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button></div>`;
  setTimeout(() => {
    const c = document.getElementById("doadoresChart");
    if (c) drawBarH(c, top10.map(r=>r.Doador).reverse(), top10.map(r=>r.Unidades).reverse(), ["#6366f1","#ec4899"]);
  }, 30);
  return html;
}

function renderRelatorios() {
  const mov = loadMov(); const inv = loadInv();
  if (!mov.length) return msg("info", "Sem dados para analisar.");
  let html = sectionTitle("📈 Relatórios e Análises");
  // monthly flow
  const fluxoMap = {};
  mov.forEach(m => {
    const d = new Date(m.data);
    if (isNaN(d)) return;
    const mes = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}`;
    if (!fluxoMap[mes]) fluxoMap[mes] = {};
    fluxoMap[mes][m.tipo] = (fluxoMap[mes][m.tipo] || 0) + num(m.quantidade);
  });
  const meses = Object.keys(fluxoMap).sort();
  const tipos = ["Entrada","Saída","Eliminação","Edição"];
  const cores = { "Entrada":"#10b981","Saída":"#ef4444","Eliminação":"#94a3b8","Edição":"#f59e0b" };

  // Summary KPIs
  const ent = mov.filter(m=>m.tipo==="Entrada").reduce((s,m)=>s+num(m.quantidade),0);
  const sai = mov.filter(m=>m.tipo==="Saída").reduce((s,m)=>s+num(m.quantidade),0);
  html += `<div class="kpi-grid">
    ${kpiCard("📥","Entradas",numFmt(ent),GRAD.verde)}
    ${kpiCard("📤","Saídas",numFmt(sai),GRAD.vermelho)}
    ${kpiCard("🕓","Movimentos",mov.length,GRAD.roxo)}
    ${kpiCard("📦","Stock atual",numFmt(inv.reduce((s,i)=>s+num(i.quantidade),0)),GRAD.laranja)}
  </div>`;

  html += `<div class="card" style="margin-top:1rem"><h4>📅 Fluxo Mensal</h4><canvas id="fluxoChart" height="440"></canvas></div>`;
  // table resumo
  const resumo = meses.map(mes => {
    const row = { Mês: mes };
    tipos.forEach(t => row[t] = fluxoMap[mes][t] || 0);
    return row;
  });
  html += `<div class="card" style="margin-top:1rem"><h4>Resumo por mês</h4>${renderTabela(resumo)}</div>`;
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button></div>`;
  setTimeout(() => {
    const c = document.getElementById("fluxoChart");
    if (!c) return;
    // group bars by month
    const ctx = c.getContext("2d");
    const dpr = window.devicePixelRatio || 1;
    const W = c.clientWidth || 800, H = c.height;
    c.width = W*dpr; c.height = H*dpr; c.style.width = W+"px"; c.style.height = H+"px";
    ctx.scale(dpr, dpr); ctx.clearRect(0,0,W,H);
    const pad = { l: 50, r: 20, t: 20, b: 50 };
    const max = Math.max(1, ...meses.flatMap(m => tipos.map(t => fluxoMap[m][t] || 0)));
    const groupW = (W - pad.l - pad.r) / Math.max(1, meses.length);
    ctx.font = "11px Inter, sans-serif";
    ctx.fillStyle = "#94a3b8"; ctx.textAlign = "right"; ctx.textBaseline = "middle";
    for (let g = 0; g <= 4; g++) {
      const y = pad.t + (H - pad.t - pad.b) * (g / 4);
      ctx.fillText(String(Math.round(max * (1 - g/4))), pad.l - 8, y);
      ctx.strokeStyle = "rgba(148,163,184,.15)";
      ctx.beginPath(); ctx.moveTo(pad.l, y); ctx.lineTo(W - pad.r, y); ctx.stroke();
    }
    const bw = (groupW * 0.8) / tipos.length;
    meses.forEach((mes, i) => {
      const x0 = pad.l + i * groupW + groupW * 0.1;
      tipos.forEach((t, j) => {
        const v = fluxoMap[mes][t] || 0;
        const h = (v / max) * (H - pad.t - pad.b);
        ctx.fillStyle = cores[t];
        roundRect(ctx, x0 + j * bw, H - pad.b - h, bw - 2, h, 4); ctx.fill();
      });
      ctx.fillStyle = "#cbd5e1"; ctx.textAlign = "center"; ctx.textBaseline = "top";
      ctx.fillText(mes, x0 + (bw * tipos.length) / 2, H - pad.b + 8);
    });
    // legend
    let lx = pad.l, ly = 6;
    tipos.forEach(t => {
      ctx.fillStyle = cores[t]; ctx.fillRect(lx, ly, 10, 10);
      ctx.fillStyle = "#cbd5e1"; ctx.textAlign = "left"; ctx.textBaseline = "middle";
      ctx.fillText(t, lx + 14, ly + 5);
      lx += ctx.measureText(t).width + 40;
    });
  }, 30);
  return html;
}

function renderHistorico() {
  const mov = loadMov();
  if (!mov.length) return msg("info", "Sem movimentos.");
  let html = sectionTitle("🕓 Histórico de Movimentos");
  html += `<div class="form-card" style="margin-bottom:1rem"><div class="grid-form">
    <div><label class="fld">Tipo</label><select id="h_tipo" onchange="filtrarHist()"><option>Todos</option><option>Entrada</option><option>Saída</option><option>Eliminação</option><option>Edição</option></select></div>
    <div><label class="fld">🔎 Pesquisar</label><input type="text" id="h_busca" oninput="filtrarHist()"></div>
  </div></div>`;
  html += `<div id="h_metrics"></div><div id="h_tabela"></div>`;
  html += `<div class="toolbar no-print"><button class="btn btn-green" onclick="window.print()">📄 Imprimir / Salvar PDF</button><button class="btn btn-primary" onclick="exportarCSVMov()">⬇️ Exportar CSV</button></div>`;
  setTimeout(filtrarHist, 20);
  return html;
}
function filtrarHist() {
  const mov = loadMov();
  const tipo = document.getElementById("h_tipo")?.value || "Todos";
  const busca = (document.getElementById("h_busca")?.value || "").toLowerCase();
  let df = mov.filter(m => (tipo === "Todos" || m.tipo === tipo)
    && (!busca || m.item.toLowerCase().includes(busca) || (m.pessoa||"").toLowerCase().includes(busca)));
  df.sort((a,b) => (b.data||"").localeCompare(a.data||""));
  const met = document.getElementById("h_metrics");
  if (met) met.innerHTML = kpiCard("🕓","Movimentos filtrados",df.length,GRAD.roxo);
  const tb = document.getElementById("h_tabela");
  if (tb) tb.innerHTML = renderTabela(df, { cols:["data","tipo","item","categoria","quantidade","pessoa","observacoes"], labels:{data:"Data/Hora",tipo:"Tipo",item:"Item",categoria:"Categoria",quantidade:"Qtd",pessoa:"Pessoa",observacoes:"Obs."} });
}
function exportarCSVMov() {
  const mov = loadMov();
  const cols = ["data","tipo","item","categoria","quantidade","pessoa","observacoes"];
  const rows = [cols.join(",")].concat(mov.map(i => cols.map(c => `"${String(i[c]??"").replace(/"/g,'""')}"`).join(",")));
  const blob = new Blob([rows.join("\n")], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = `movimentos_${hojeISO()}.csv`; a.click();
}

function renderApagar() {
  const inv = loadInv();
  if (!inv.length) return msg("info", "Sem dados.");
  let html = sectionTitle("🗑️ Apagar Item");
  html += msg("warn", "⚠️ Ação irreversível. Para saída parcial usa <b>📤 Dar Baixa</b>.");
  html += `<div class="form-card">
    <label class="fld">Item</label>
    <select id="a_sel">${inv.map(i=>`<option value="${i.id}">${esc(i.item)} — ${esc(i.categoria)} | qtd: ${i.quantidade}</option>`).join("")}</select>
    <label class="chk" style="margin-top:.8rem"><input type="checkbox" id="a_conf" onchange="document.getElementById('a_btn').disabled=!this.checked"> Confirmo que quero eliminar permanentemente.</label>
    <div id="apagar_msg"></div>
    <button class="btn btn-red btn-block" id="a_btn" disabled style="margin-top:.8rem" onclick="submitApagar()">🗑️ Eliminar</button>
  </div>`;
  return html;
}
function submitApagar() {
  const id = document.getElementById("a_sel").value;
  const r = apagarItem(id);
  document.getElementById("apagar_msg").innerHTML = r.ok ? msg("ok", "✅ " + r.msg) : msg("err", "❌ " + r.msg);
  if (r.ok) setTimeout(() => render("apagar"), 700);
}

/* =========================================================
   ROUTER / RENDER
========================================================= */
const VIEWS = {
  dashboard: renderDashboard,
  doacao: renderDoacao,
  inventario: renderInventario,
  baixa: renderBaixa,
  validade: renderValidade,
  estoque: renderEstoque,
  doadores: renderDoadores,
  relatorios: renderRelatorios,
  historico: renderHistorico,
  apagar: renderApagar,
};
function render(view) {
  currentView = view;
  document.querySelectorAll(".menu-btn").forEach(b => b.classList.toggle("active", b.dataset.id === view));
  const el = document.getElementById("view");
  el.innerHTML = VIEWS[view] ? VIEWS[view]() : msg("info", "View não encontrada.");
}
function buildMenu() {
  document.getElementById("menu").innerHTML = MENU.map(m =>
    `<button class="menu-btn" data-id="${m.id}" onclick="render('${m.id}')">${m.icon} ${m.label}</button>`
  ).join("");
}
function tickClock() {
  const now = new Date();
  const br = now.toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo", day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit", second: "2-digit" });
  const h = document.getElementById("clock");
  if (h) h.textContent = `🕐 ${br.split(" ")[1] || ""} · Brasília`;
  const hh = document.getElementById("hero-clock");
  if (hh) hh.textContent = `🕐 ${br} (Brasília)`;
}
/* INIT */
buildMenu();
render("dashboard");
tickClock();
setInterval(tickClock, 1000);
</script>
</body>
</html>
