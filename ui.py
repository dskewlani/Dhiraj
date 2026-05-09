"""
ui.py — Shared UI components, CSS, and helper rendering functions.
"""

TERMINAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Rajdhani:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

:root {
    --bg:       #050810;
    --bg2:      #080c14;
    --bg3:      #0c1220;
    --surface:  #0f1825;
    --card:     #111d2e;
    --border:   #1a2d45;
    --border2:  #243850;
    --accent:   #00d4ff;
    --accent2:  #0099cc;
    --gold:     #f5a623;
    --green:    #00e676;
    --green2:   #00c853;
    --red:      #ff1744;
    --red2:     #d50000;
    --yellow:   #ffd600;
    --purple:   #d500f9;
    --orange:   #ff6d00;
    --teal:     #1de9b6;
    --text:     #b0c4d8;
    --text2:    #7a9ab5;
    --muted:    #3d5a75;
    --white:    #e8f4fd;
}

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background: var(--bg);
    color: var(--text);
    font-size: 14px;
}

.stApp {
    background: var(--bg);
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg2); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent2); }

/* ── TERMINAL HEADER ── */
.terminal-header {
    background: linear-gradient(135deg, var(--bg2) 0%, var(--bg3) 100%);
    border-bottom: 2px solid var(--accent);
    padding: 12px 24px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
}
.terminal-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        90deg, transparent, transparent 2px,
        rgba(0,212,255,0.02) 2px, rgba(0,212,255,0.02) 4px
    );
    pointer-events: none;
}
.terminal-title {
    font-family: 'Orbitron', monospace;
    font-size: 1.6rem;
    font-weight: 900;
    letter-spacing: 4px;
    background: linear-gradient(90deg, var(--accent), var(--teal), var(--gold));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}
.terminal-sub {
    font-family: 'JetBrains Mono';
    font-size: 0.65rem;
    color: var(--muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── TICKER TAPE ── */
.ticker-outer {
    overflow: hidden;
    background: var(--bg2);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--accent);
    padding: 5px 0;
    margin-bottom: 12px;
}
.ticker-inner {
    display: flex;
    gap: 48px;
    animation: scroll-left 50s linear infinite;
    white-space: nowrap;
}
@keyframes scroll-left {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.t-item {
    font-family: 'JetBrains Mono';
    font-size: 0.72rem;
    color: var(--muted);
    display: inline-flex;
    gap: 6px;
    align-items: center;
}
.t-name { color: var(--text2); font-weight: 600; }
.t-up   { color: var(--green); }
.t-dn   { color: var(--red); }
.t-flat { color: var(--yellow); }

/* ── INDEX CARDS ── */
.idx-card {
    background: linear-gradient(135deg, var(--surface), var(--card));
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.idx-card:hover { border-color: var(--accent2); }
.idx-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
}
.idx-card.bn::after  { background: linear-gradient(90deg,var(--gold),var(--orange)); }
.idx-card.nf::after  { background: linear-gradient(90deg,var(--accent),var(--teal)); }
.idx-card.vx::after  { background: linear-gradient(90deg,var(--red),var(--purple)); }
.idx-card.sx::after  { background: linear-gradient(90deg,var(--purple),var(--accent)); }
.idx-card.it::after  { background: linear-gradient(90deg,var(--teal),var(--green)); }
.idx-price {
    font-family: 'JetBrains Mono';
    font-size: 1.4rem;
    font-weight: 700;
    line-height: 1.1;
}
.idx-label {
    font-size: 0.65rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 4px;
}
.idx-chg {
    font-family: 'JetBrains Mono';
    font-size: 0.72rem;
    margin-top: 3px;
}
.up   { color: var(--green) !important; }
.dn   { color: var(--red) !important; }
.flat { color: var(--yellow) !important; }

/* ── METRIC CARDS ── */
.m-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
}
.m-val  { font-family: 'JetBrains Mono'; font-size: 1.2rem; font-weight: 700; }
.m-lbl  { font-size: 0.62rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; margin-top: 2px; }

/* ── SIGNAL BADGES ── */
.sig { display:inline-block; padding:3px 12px; border-radius:4px; font-family:'JetBrains Mono'; font-size:0.72rem; font-weight:700; letter-spacing:1px; }
.sig-sbuy  { background:rgba(0,230,118,0.15); color:var(--green);  border:1px solid rgba(0,230,118,0.5); }
.sig-buy   { background:rgba(0,230,118,0.08); color:var(--green);  border:1px solid rgba(0,230,118,0.3); }
.sig-wbuy  { background:rgba(29,233,182,0.08); color:var(--teal);  border:1px solid rgba(29,233,182,0.3); }
.sig-ssell { background:rgba(255,23,68,0.15);  color:var(--red);   border:1px solid rgba(255,23,68,0.5); }
.sig-sell  { background:rgba(255,23,68,0.08);  color:var(--red);   border:1px solid rgba(255,23,68,0.3); }
.sig-wsell { background:rgba(255,109,0,0.08);  color:var(--orange); border:1px solid rgba(255,109,0,0.3); }
.sig-neut  { background:rgba(255,214,0,0.08);  color:var(--yellow); border:1px solid rgba(255,214,0,0.3); }

/* ── SECTION TITLE ── */
.sec-ttl {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    letter-spacing: 3px;
    color: var(--accent);
    text-transform: uppercase;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 14px;
    margin-top: 6px;
}

/* ── TRADE CARDS ── */
.tc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px;
    margin-bottom: 8px;
}
.tc.win  { border-left: 3px solid var(--green2); }
.tc.loss { border-left: 3px solid var(--red2); }
.tc.open { border-left: 3px solid var(--accent); }
.tc-head { font-family:'Rajdhani'; font-weight:700; font-size:1rem; }
.tc-meta { font-family:'JetBrains Mono'; font-size:0.7rem; color:var(--text2); }

/* ── PROFIT BOOK ROWS ── */
.pb { background:rgba(0,230,118,0.04); border:1px solid rgba(0,230,118,0.15);
      border-radius:6px; padding:6px 12px; margin:3px 0;
      display:flex; justify-content:space-between; align-items:center; }
.pb-pct { font-family:'JetBrains Mono'; font-size:0.8rem; color:var(--green); font-weight:700; }
.pb-pr  { font-family:'JetBrains Mono'; font-size:0.85rem; }
.pb-lbl { font-size:0.72rem; color:var(--muted); }

/* ── GREEK BOX ── */
.gk { background:rgba(0,0,0,0.4); border:1px solid var(--border); border-radius:6px;
      padding:8px 10px; text-align:center; }
.gk-v { font-family:'JetBrains Mono'; font-size:0.95rem; font-weight:700; }
.gk-l { font-size:0.6rem; color:var(--muted); text-transform:uppercase; letter-spacing:1px; margin-top:2px; }

/* ── S/R LEVELS ── */
.lvl { border-radius:6px; padding:6px 12px; font-family:'JetBrains Mono'; font-size:0.82rem; text-align:center; font-weight:700; }
.lvl-r  { background:rgba(255,23,68,0.08);    border:1px solid rgba(255,23,68,0.3);    color:var(--red); }
.lvl-s  { background:rgba(0,230,118,0.08);    border:1px solid rgba(0,230,118,0.3);    color:var(--green); }
.lvl-e  { background:rgba(0,212,255,0.08);    border:1px solid rgba(0,212,255,0.3);    color:var(--accent); }
.lvl-tg { background:rgba(29,233,182,0.08);   border:1px solid rgba(29,233,182,0.3);   color:var(--teal); }

/* ── STRENGTH BAR ── */
.sb-wrap { background:var(--bg2); border-radius:4px; height:6px; overflow:hidden; margin-top:4px; }
.sb-fill { height:6px; border-radius:4px; }

/* ── INFO/WARN/SUCCESS BOXES ── */
.info-b  { background:rgba(0,212,255,0.06); border:1px solid rgba(0,212,255,0.2);  border-radius:8px; padding:10px 14px; font-size:0.82rem; color:#80deea; margin:6px 0; }
.warn-b  { background:rgba(255,109,0,0.06); border:1px solid rgba(255,109,0,0.25); border-radius:8px; padding:10px 14px; font-size:0.82rem; color:#ffab40; margin:6px 0; }
.success-b { background:rgba(0,230,118,0.06); border:1px solid rgba(0,230,118,0.2); border-radius:8px; padding:10px 14px; font-size:0.82rem; color:#69f0ae; margin:6px 0; }
.danger-b  { background:rgba(255,23,68,0.06);  border:1px solid rgba(255,23,68,0.25); border-radius:8px; padding:10px 14px; font-size:0.82rem; color:#ff6090; margin:6px 0; }

/* ── CE/PE CHIPS ── */
.ce-chip { background:rgba(0,212,255,0.1); border:1px solid rgba(0,212,255,0.35); color:var(--accent); border-radius:4px; padding:2px 10px; font-size:0.75rem; font-family:'JetBrains Mono'; font-weight:700; }
.pe-chip { background:rgba(255,23,68,0.1);  border:1px solid rgba(255,23,68,0.35);  color:var(--red);   border-radius:4px; padding:2px 10px; font-size:0.75rem; font-family:'JetBrains Mono'; font-weight:700; }
.atm-chip { background:rgba(245,166,35,0.12); border:1px solid rgba(245,166,35,0.4); color:var(--gold); border-radius:4px; padding:2px 10px; font-size:0.75rem; font-family:'JetBrains Mono'; font-weight:700; }
.fut-chip { background:rgba(213,0,249,0.1); border:1px solid rgba(213,0,249,0.35); color:var(--purple); border-radius:4px; padding:2px 10px; font-size:0.75rem; font-family:'JetBrains Mono'; font-weight:700; }

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent2), var(--accent));
    color: var(--bg);
    font-family: 'Rajdhani';
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    border: none;
    border-radius: 6px;
    padding: 8px 18px;
    text-transform: uppercase;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }

/* ── TABS ── */
.stTabs [data-baseweb="tab"] {
    font-family: 'Rajdhani';
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 2px;
    color: var(--muted);
    text-transform: uppercase;
    padding: 8px 16px;
}
.stTabs [aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
}

/* ── DATAFRAME ── */
.stDataFrame { border: 1px solid var(--border) !important; border-radius: 8px !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] label { color: var(--text2) !important; }

/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono' !important;
    font-size: 0.82rem !important;
    color: var(--text) !important;
}
.streamlit-expanderContent {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 0 0 6px 6px !important;
}

/* ── OPTION CHAIN TABLE ── */
.oc-hdr {
    display: grid;
    grid-template-columns: 1.5fr 0.8fr 0.7fr 0.6fr 1fr 1.2fr 1fr 0.6fr 0.7fr 0.8fr 1.5fr;
    padding: 8px 12px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 8px 8px 0 0;
    font-size: 0.62rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--muted);
    gap: 4px;
}
.oc-row {
    display: grid;
    grid-template-columns: 1.5fr 0.8fr 0.7fr 0.6fr 1fr 1.2fr 1fr 0.6fr 0.7fr 0.8fr 1.5fr;
    padding: 7px 12px;
    border: 1px solid var(--border);
    border-top: none;
    font-size: 0.78rem;
    gap: 4px;
    align-items: center;
    transition: background 0.15s;
}
.oc-row:hover { background: rgba(0,212,255,0.04) !important; }
.oc-row:last-child { border-radius: 0 0 8px 8px; }
.oc-atm { background: rgba(245,166,35,0.07) !important; border-left: 3px solid var(--gold) !important; border-right: 3px solid var(--gold) !important; }

/* ── JOURNAL TABLE ── */
.jrnl-row { background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:8px 12px; margin:4px 0; display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; }

/* ── PNL SUMMARY ── */
.pnl-pos { color: var(--green); font-family:'JetBrains Mono'; font-weight:700; }
.pnl-neg { color: var(--red);   font-family:'JetBrains Mono'; font-weight:700; }
.pnl-zero { color: var(--yellow); font-family:'JetBrains Mono'; font-weight:700; }

/* ── PROGRESS BAR OVERRIDE ── */
.stProgress > div > div { background: linear-gradient(90deg, var(--accent2), var(--accent)) !important; }

/* ── ATM/ITM/OTM colors ── */
.itm-ce { background: rgba(0,212,255,0.04); }
.itm-pe { background: rgba(255,23,68,0.04); }
.ce-color { color: var(--accent) !important; }
.pe-color { color: var(--red) !important; }
.gold-color { color: var(--gold) !important; }
.green-color { color: var(--green) !important; }
.purple-color { color: var(--purple) !important; }
</style>
"""

def sig_badge(rec):
    cls = {
        "STRONG BUY": "sig-sbuy", "BUY": "sig-buy", "WEAK BUY": "sig-wbuy",
        "STRONG SELL": "sig-ssell", "SELL": "sig-sell", "WEAK SELL": "sig-wsell",
        "NEUTRAL": "sig-neut", "AVOID": "sig-ssell",
    }.get(rec, "sig-neut")
    return f'<span class="sig {cls}">{rec}</span>'

def strength_bar(pct, color="#00e676"):
    return f'''<div class="sb-wrap"><div class="sb-fill" style="width:{pct}%;background:{color};"></div></div>'''

def pnl_fmt(val):
    if val > 0:  return f'<span class="pnl-pos">▲ ₹{val:,.2f}</span>'
    elif val < 0: return f'<span class="pnl-neg">▼ ₹{abs(val):,.2f}</span>'
    return f'<span class="pnl-zero">₹0.00</span>'

def ticker_item(name, price, pct):
    cls  = "t-up" if pct >= 0 else "t-dn"
    arrow= "▲" if pct >= 0 else "▼"
    return (f'<span class="t-item"><span class="t-name">{name}</span>'
            f'<span class="{cls}">{price:,.2f} {arrow}{abs(pct):.2f}%</span></span>')

def metric_card(val, lbl, color="var(--accent)"):
    return f'<div class="m-card"><div class="m-val" style="color:{color};">{val}</div><div class="m-lbl">{lbl}</div></div>'

def level_box(label, val, css_class):
    return f'<div class="lvl {css_class}"><div style="font-size:0.6rem;opacity:0.7">{label}</div>₹{val:,.2f}</div>'

def profit_book_row(pct, price, label, profit_abs):
    return f'''<div class="pb">
        <span class="pb-pct">+{pct}%</span>
        <span class="pb-pr">₹{price:.2f}</span>
        <span class="pb-lbl">{label}</span>
        <span style="font-family:JetBrains Mono;font-size:0.78rem;color:var(--teal);">+₹{profit_abs:.0f}</span>
    </div>'''

def greek_box(val, label, color="var(--text)"):
    return f'<div class="gk"><div class="gk-v" style="color:{color}">{val}</div><div class="gk-l">{label}</div></div>'
