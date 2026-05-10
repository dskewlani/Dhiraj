"""
ui.py — ProTrader Terminal v4 UI
Upstox-inspired: deep purple backgrounds, crisp white text, violet accents.
Fonts: Sora (display) + DM Mono (data) + DM Sans (body)
"""

TERMINAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
    /* ── Upstox Purple Surface System ── */
    --bg:        #0d0b1a;
    --bg2:       #110e22;
    --bg3:       #15122a;
    --surface:   #1a1630;
    --card:      #1f1b38;
    --card2:     #251f44;
    --overlay:   #2c2750;

    /* ── Borders ── */
    --border:    #2e2850;
    --border2:   #3d3668;
    --border3:   #504880;

    /* ── Upstox Signature Violet/Purple Accent ── */
    --purple:    #7c3aed;
    --purple2:   #6d28d9;
    --purple3:   #8b5cf6;
    --purple4:   #a78bfa;
    --purple-light: #ede9fe;
    --purple-bg: rgba(124,58,237,0.12);
    --purple-glow: rgba(124,58,237,0.3);
    --purple-border: rgba(124,58,237,0.4);

    /* ── Semantic ── */
    --green:     #22c55e;
    --green2:    #16a34a;
    --green3:    #4ade80;
    --green-bg:  rgba(34,197,94,0.1);
    --green-border: rgba(34,197,94,0.35);
    --red:       #f43f5e;
    --red2:      #e11d48;
    --red3:      #fb7185;
    --red-bg:    rgba(244,63,94,0.1);
    --red-border: rgba(244,63,94,0.35);
    --gold:      #f59e0b;
    --gold2:     #fbbf24;
    --gold-bg:   rgba(245,158,11,0.1);
    --gold-border: rgba(245,158,11,0.35);
    --blue:      #3b82f6;
    --blue-bg:   rgba(59,130,246,0.1);
    --teal:      #14b8a6;
    --teal-bg:   rgba(20,184,166,0.1);
    --orange:    #f97316;

    /* ── Text (Upstox uses near-white on dark purple) ── */
    --white:     #ffffff;
    --text:      #f1f0f8;
    --text2:     #c4bfe8;
    --text3:     #8b84b8;
    --muted:     #564f80;
    --dim:       #3a3460;

    /* ── Fonts ── */
    --font-ui:    'DM Sans', sans-serif;
    --font-mono:  'DM Mono', monospace;
    --font-disp:  'Sora', sans-serif;
}

/* ════════ BASE RESET ════════ */
html, body, [class*="css"] {
    font-family: var(--font-ui);
    background: var(--bg) !important;
    color: var(--text);
    font-size: 14px;
}
.stApp { background: var(--bg) !important; }
* { box-sizing: border-box; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg2); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--purple3); }

/* ════════ TERMINAL HEADER ════════ */
.terminal-header {
    background: linear-gradient(135deg, var(--bg2) 0%, var(--bg3) 60%, #1e1540 100%);
    border-bottom: 1px solid var(--border2);
    padding: 14px 28px 12px;
    margin-bottom: 0;
    position: relative;
    overflow: hidden;
}
.terminal-header::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 80% at 80% 50%, rgba(124,58,237,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 30% 50% at 10% 50%, rgba(139,92,246,0.06) 0%, transparent 50%);
    pointer-events: none;
}
.terminal-title {
    font-family: var(--font-disp);
    font-size: 1.55rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: var(--white);
    line-height: 1.1;
}
.terminal-title span {
    background: linear-gradient(90deg, var(--purple3), var(--purple4), #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.terminal-sub {
    font-family: var(--font-mono);
    font-size: 0.63rem;
    color: var(--muted);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-top: 3px;
}
.terminal-dot {
    display: inline-block;
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 8px var(--green);
    animation: pulse-dot 2s ease-in-out infinite;
    margin-right: 6px;
    vertical-align: middle;
}
@keyframes pulse-dot {
    0%,100% { opacity: 1; box-shadow: 0 0 8px var(--green); }
    50%      { opacity: 0.5; box-shadow: 0 0 3px var(--green); }
}

/* ════════ TICKER TAPE ════════ */
.ticker-outer {
    overflow: hidden;
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 6px 0;
    margin-bottom: 0;
}
.ticker-inner {
    display: flex;
    gap: 52px;
    animation: scroll-left 55s linear infinite;
    white-space: nowrap;
}
@keyframes scroll-left {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.t-item {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    color: var(--muted);
    display: inline-flex;
    gap: 7px;
    align-items: center;
}
.t-name { color: var(--text2); font-weight: 500; letter-spacing: 0.3px; }
.t-up   { color: var(--green3); }
.t-dn   { color: var(--red3); }
.t-flat { color: var(--gold2); }

/* ════════ INDEX CARDS ════════ */
.idx-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.idx-card:hover {
    border-color: var(--border3);
    box-shadow: 0 4px 24px rgba(124,58,237,0.12);
}
.idx-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.idx-card.bn::before  { background: linear-gradient(90deg, var(--purple), var(--purple3)); }
.idx-card.nf::before  { background: linear-gradient(90deg, var(--purple3), var(--blue)); }
.idx-card.vx::before  { background: linear-gradient(90deg, var(--red), var(--orange)); }
.idx-card.sx::before  { background: linear-gradient(90deg, var(--gold), var(--orange)); }
.idx-card.it::before  { background: linear-gradient(90deg, var(--teal), var(--blue)); }
.idx-label {
    font-family: var(--font-ui);
    font-size: 0.62rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.8px;
    margin-bottom: 6px;
    font-weight: 500;
}
.idx-price {
    font-family: var(--font-mono);
    font-size: 1.45rem;
    font-weight: 500;
    color: var(--white);
    line-height: 1.1;
    letter-spacing: -0.5px;
}
.idx-chg {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    margin-top: 4px;
}
.up   { color: var(--green3) !important; }
.dn   { color: var(--red3) !important; }
.flat { color: var(--gold2) !important; }

/* ════════ METRIC CARDS ════════ */
.m-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
    transition: border-color 0.2s;
}
.m-card:hover { border-color: var(--border3); }
.m-val {
    font-family: var(--font-mono);
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--white);
}
.m-lbl {
    font-size: 0.6rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 3px;
    font-family: var(--font-ui);
    font-weight: 500;
}

/* ════════ SIGNAL BADGES ════════ */
.sig {
    display: inline-block;
    padding: 3px 11px;
    border-radius: 5px;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.5px;
}
.sig-sbuy  { background: rgba(34,197,94,0.15);   color: var(--green3);  border: 1px solid var(--green-border); }
.sig-buy   { background: rgba(34,197,94,0.08);   color: var(--green);   border: 1px solid rgba(34,197,94,0.25); }
.sig-wbuy  { background: rgba(20,184,166,0.08);  color: var(--teal);    border: 1px solid rgba(20,184,166,0.25); }
.sig-ssell { background: rgba(244,63,94,0.15);   color: var(--red3);    border: 1px solid var(--red-border); }
.sig-sell  { background: rgba(244,63,94,0.08);   color: var(--red);     border: 1px solid rgba(244,63,94,0.25); }
.sig-wsell { background: rgba(249,115,22,0.08);  color: var(--orange);  border: 1px solid rgba(249,115,22,0.25); }
.sig-neut  { background: rgba(245,158,11,0.08);  color: var(--gold2);   border: 1px solid rgba(245,158,11,0.25); }

/* ════════ SECTION TITLE ════════ */
.sec-ttl {
    font-family: var(--font-disp);
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 2.5px;
    color: var(--purple4);
    text-transform: uppercase;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 16px;
    margin-top: 8px;
}

/* ════════ TRADE CARDS ════════ */
.tc {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 8px;
    transition: border-color 0.2s;
}
.tc:hover { border-color: var(--border3); }
.tc.win  { border-left: 3px solid var(--green); }
.tc.loss { border-left: 3px solid var(--red); }
.tc.open { border-left: 3px solid var(--purple3); }
.tc-head { font-family: var(--font-disp); font-weight: 600; font-size: 0.95rem; color: var(--white); }
.tc-meta { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text3); margin-top: 3px; }

/* ════════ PROFIT BOOK ROWS ════════ */
.pb {
    background: rgba(34,197,94,0.05);
    border: 1px solid rgba(34,197,94,0.15);
    border-radius: 8px;
    padding: 8px 14px;
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.pb-pct { font-family: var(--font-mono); font-size: 0.78rem; color: var(--green3); font-weight: 500; }
.pb-pr  { font-family: var(--font-mono); font-size: 0.82rem; color: var(--white); }
.pb-lbl { font-size: 0.68rem; color: var(--muted); font-family: var(--font-ui); }

/* ════════ GREEK BOXES ════════ */
.gk {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
    transition: border-color 0.2s;
}
.gk:hover { border-color: var(--purple-border); }
.gk-v { font-family: var(--font-mono); font-size: 0.95rem; font-weight: 500; color: var(--white); }
.gk-l { font-size: 0.58rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.2px; margin-top: 3px; font-family: var(--font-ui); }

/* ════════ SUPPORT / RESISTANCE LEVELS ════════ */
.lvl {
    border-radius: 8px;
    padding: 8px 14px;
    font-family: var(--font-mono);
    font-size: 0.82rem;
    text-align: center;
    font-weight: 500;
}
.lvl-r  { background: var(--red-bg);    border: 1px solid var(--red-border);    color: var(--red3); }
.lvl-s  { background: var(--green-bg);  border: 1px solid var(--green-border);  color: var(--green3); }
.lvl-e  { background: var(--purple-bg); border: 1px solid var(--purple-border); color: var(--purple4); }
.lvl-tg { background: var(--teal-bg);   border: 1px solid rgba(20,184,166,0.3); color: var(--teal); }

/* ════════ STRENGTH BAR ════════ */
.sb-wrap {
    background: var(--bg3);
    border-radius: 3px;
    height: 5px;
    overflow: hidden;
    margin-top: 5px;
}
.sb-fill {
    height: 5px;
    border-radius: 3px;
    transition: width 0.4s ease;
}

/* ════════ INFO / WARN / SUCCESS BOXES ════════ */
.info-b    { background: var(--purple-bg);           border: 1px solid var(--purple-border);        border-radius: 9px; padding: 11px 15px; font-size: 0.82rem; color: var(--purple4); margin: 6px 0; font-family: var(--font-ui); }
.warn-b    { background: rgba(245,158,11,0.07);      border: 1px solid rgba(245,158,11,0.3);        border-radius: 9px; padding: 11px 15px; font-size: 0.82rem; color: var(--gold2);   margin: 6px 0; font-family: var(--font-ui); }
.success-b { background: var(--green-bg);            border: 1px solid var(--green-border);         border-radius: 9px; padding: 11px 15px; font-size: 0.82rem; color: var(--green3);  margin: 6px 0; font-family: var(--font-ui); }
.danger-b  { background: var(--red-bg);              border: 1px solid var(--red-border);           border-radius: 9px; padding: 11px 15px; font-size: 0.82rem; color: var(--red3);    margin: 6px 0; font-family: var(--font-ui); }

/* ════════ CE / PE / ATM CHIPS ════════ */
.ce-chip  { background: rgba(59,130,246,0.1);    border: 1px solid rgba(59,130,246,0.35);    color: #93c5fd; border-radius: 5px; padding: 2px 10px; font-size: 0.7rem; font-family: var(--font-mono); }
.pe-chip  { background: var(--red-bg);           border: 1px solid var(--red-border);        color: var(--red3); border-radius: 5px; padding: 2px 10px; font-size: 0.7rem; font-family: var(--font-mono); }
.atm-chip { background: var(--gold-bg);          border: 1px solid var(--gold-border);       color: var(--gold2); border-radius: 5px; padding: 2px 10px; font-size: 0.7rem; font-family: var(--font-mono); }
.fut-chip { background: var(--purple-bg);        border: 1px solid var(--purple-border);     color: var(--purple4); border-radius: 5px; padding: 2px 10px; font-size: 0.7rem; font-family: var(--font-mono); }

/* ════════ COLOR UTILITIES ════════ */
.purple-color { color: var(--purple4) !important; }
.green-color  { color: var(--green3) !important; }
.red-color    { color: var(--red3) !important; }
.gold-color   { color: var(--gold2) !important; }
.white-color  { color: var(--white) !important; }
.muted-color  { color: var(--muted) !important; }
.pnl-pos  { color: var(--green3); font-family: var(--font-mono); font-weight: 500; }
.pnl-neg  { color: var(--red3);   font-family: var(--font-mono); font-weight: 500; }
.pnl-zero { color: var(--gold2);  font-family: var(--font-mono); font-weight: 500; }
.itm-ce   { background: rgba(59,130,246,0.04); }
.itm-pe   { background: rgba(244,63,94,0.04); }
.ce-color { color: #93c5fd !important; }
.pe-color { color: var(--red3) !important; }

/* ════════ BUTTONS ════════ */
.stButton > button {
    background: var(--purple) !important;
    color: var(--white) !important;
    font-family: var(--font-ui) !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.5px !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 8px 20px !important;
    transition: background 0.2s, box-shadow 0.2s !important;
    text-transform: none !important;
}
.stButton > button:hover {
    background: var(--purple2) !important;
    box-shadow: 0 4px 20px var(--purple-glow) !important;
}
.stButton > button:active { background: var(--purple3) !important; }

/* ════════ TABS ════════ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg2) !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
    color: var(--text3) !important;
    padding: 8px 18px !important;
    background: transparent !important;
    border-radius: 6px 6px 0 0 !important;
}
.stTabs [aria-selected="true"] {
    color: var(--white) !important;
    background: var(--purple-bg) !important;
    border-bottom: 2px solid var(--purple3) !important;
}

/* ════════ DATAFRAME ════════ */
.stDataFrame {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}
.stDataFrame th {
    background: var(--bg2) !important;
    color: var(--text3) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.68rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    border-bottom: 1px solid var(--border) !important;
}
.stDataFrame td {
    font-family: var(--font-mono) !important;
    font-size: 0.78rem !important;
    color: var(--text) !important;
    border-bottom: 1px solid var(--border) !important;
}

/* ════════ SIDEBAR ════════ */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] label {
    color: var(--text2) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.8rem !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: var(--surface) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}
[data-testid="stSidebar"] .stSlider > div > div > div {
    background: var(--purple) !important;
}

/* ════════ INPUT WIDGETS ════════ */
.stSelectbox > div > div,
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.85rem !important;
}
.stSelectbox > div > div:focus-within,
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: var(--purple3) !important;
    box-shadow: 0 0 0 2px var(--purple-bg) !important;
}

/* Checkbox & Radio */
.stCheckbox label, .stRadio label {
    color: var(--text2) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
}
.stCheckbox [data-testid="stCheckbox"] > div > div {
    background: var(--purple) !important;
    border-color: var(--purple) !important;
}

/* Slider */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: var(--purple) !important;
    border-color: var(--purple) !important;
}
.stSlider [data-baseweb="slider"] [data-testid="stTickBar"] {
    background: var(--purple) !important;
}

/* Progress */
.stProgress > div > div { background: var(--purple) !important; }

/* ════════ EXPANDER ════════ */
.streamlit-expanderHeader {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    color: var(--text) !important;
    font-weight: 500 !important;
}
.streamlit-expanderHeader:hover {
    border-color: var(--purple-border) !important;
}
.streamlit-expanderContent {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
}

/* ════════ OPTION CHAIN TABLE ════════ */
.oc-hdr {
    display: grid;
    grid-template-columns: 1.5fr 0.8fr 0.7fr 0.6fr 1fr 1.2fr 1fr 0.6fr 0.7fr 0.8fr 1.5fr;
    padding: 9px 14px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px 10px 0 0;
    font-size: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--muted);
    gap: 4px;
    font-family: var(--font-ui);
    font-weight: 600;
}
.oc-row {
    display: grid;
    grid-template-columns: 1.5fr 0.8fr 0.7fr 0.6fr 1fr 1.2fr 1fr 0.6fr 0.7fr 0.8fr 1.5fr;
    padding: 8px 14px;
    border: 1px solid var(--border);
    border-top: none;
    font-size: 0.77rem;
    gap: 4px;
    align-items: center;
    transition: background 0.15s;
    font-family: var(--font-mono);
}
.oc-row:hover { background: rgba(124,58,237,0.05) !important; }
.oc-row:last-child { border-radius: 0 0 10px 10px; }
.oc-atm {
    background: rgba(245,158,11,0.06) !important;
    border-left: 3px solid var(--gold) !important;
    border-right: 3px solid var(--gold) !important;
}

/* ════════ JOURNAL ROW ════════ */
.jrnl-row {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 9px 14px;
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    transition: border-color 0.15s;
}
.jrnl-row:hover { border-color: var(--border3); }

/* ════════ PURPLE PILL / TAG ════════ */
.pill {
    display: inline-block;
    background: var(--purple-bg);
    border: 1px solid var(--purple-border);
    color: var(--purple4);
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.67rem;
    font-family: var(--font-ui);
    font-weight: 600;
    letter-spacing: 0.3px;
}
.pill-green  { background: var(--green-bg);  border-color: var(--green-border); color: var(--green3); }
.pill-red    { background: var(--red-bg);    border-color: var(--red-border);   color: var(--red3); }
.pill-gold   { background: var(--gold-bg);   border-color: var(--gold-border);  color: var(--gold2); }

/* ════════ RANK BADGE ════════ */
.rank-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 26px; height: 26px;
    background: var(--purple-bg);
    border: 1px solid var(--purple-border);
    border-radius: 50%;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 500;
    color: var(--purple4);
}

/* ════════ DIVIDER ════════ */
.divider {
    height: 1px;
    background: var(--border);
    margin: 12px 0;
}
.divider-purple {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--purple-border), transparent);
    margin: 14px 0;
}

/* ════════ SCROLLABLE TABLE WRAPPER ════════ */
.scroll-table {
    max-height: 420px;
    overflow-y: auto;
    border-radius: 10px;
    border: 1px solid var(--border);
}
.scroll-table::-webkit-scrollbar { width: 4px; }
.scroll-table::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

/* ════════ METRIC HIGHLIGHT BOX ════════ */
.hl-box {
    background: var(--purple-bg);
    border: 1px solid var(--purple-border);
    border-radius: 10px;
    padding: 14px 18px;
    text-align: center;
}
.hl-val {
    font-family: var(--font-mono);
    font-size: 1.4rem;
    font-weight: 500;
    color: var(--purple4);
}
.hl-lbl {
    font-size: 0.6rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 3px;
    font-family: var(--font-ui);
}
</style>
"""

# ─── Helper Rendering Functions ───────────────────────────────────────────────

def sig_badge(rec):
    cls = {
        "STRONG BUY":  "sig-sbuy",
        "BUY":         "sig-buy",
        "WEAK BUY":    "sig-wbuy",
        "STRONG SELL": "sig-ssell",
        "SELL":        "sig-sell",
        "WEAK SELL":   "sig-wsell",
        "NEUTRAL":     "sig-neut",
        "AVOID":       "sig-ssell",
    }.get(rec, "sig-neut")
    return f'<span class="sig {cls}">{rec}</span>'

def strength_bar(pct, color=None):
    if color is None:
        if pct >= 75:   color = "var(--green)"
        elif pct >= 55: color = "var(--purple3)"
        else:           color = "var(--gold2)"
    return (f'<div class="sb-wrap">'
            f'<div class="sb-fill" style="width:{pct}%;background:{color};"></div>'
            f'</div>')

def pnl_fmt(val):
    if val > 0:  return f'<span class="pnl-pos">▲ ₹{val:,.2f}</span>'
    elif val < 0: return f'<span class="pnl-neg">▼ ₹{abs(val):,.2f}</span>'
    return f'<span class="pnl-zero">₹0.00</span>'

def ticker_item(name, price, pct):
    cls   = "t-up" if pct >= 0 else "t-dn"
    arrow = "▲" if pct >= 0 else "▼"
    return (f'<span class="t-item">'
            f'<span class="t-name">{name}</span>'
            f'<span class="{cls}">{price:,.2f} {arrow}{abs(pct):.2f}%</span>'
            f'</span>')

def metric_card(val, lbl, color="var(--purple4)"):
    return (f'<div class="m-card">'
            f'<div class="m-val" style="color:{color};">{val}</div>'
            f'<div class="m-lbl">{lbl}</div>'
            f'</div>')

def level_box(label, val, css_class):
    return (f'<div class="lvl {css_class}">'
            f'<div style="font-size:0.58rem;opacity:0.65;margin-bottom:2px;">{label}</div>'
            f'₹{val:,.2f}'
            f'</div>')

def profit_book_row(pct, price, label, profit_abs):
    return (f'<div class="pb">'
            f'<span class="pb-pct">+{pct}%</span>'
            f'<span class="pb-pr">₹{price:.2f}</span>'
            f'<span class="pb-lbl">{label}</span>'
            f'<span style="font-family:var(--font-mono);font-size:0.78rem;color:var(--teal);">+₹{profit_abs:.0f}</span>'
            f'</div>')

def greek_box(val, label, color="var(--white)"):
    return (f'<div class="gk">'
            f'<div class="gk-v" style="color:{color}">{val}</div>'
            f'<div class="gk-l">{label}</div>'
            f'</div>')

def pill(text, variant="purple"):
    variant_map = {
        "purple": "pill",
        "green":  "pill pill-green",
        "red":    "pill pill-red",
        "gold":   "pill pill-gold",
    }
    cls = variant_map.get(variant, "pill")
    return f'<span class="{cls}">{text}</span>'

def rank_badge(n):
    return f'<span class="rank-badge">#{n}</span>'

def hl_box(val, lbl, color="var(--purple4)"):
    return (f'<div class="hl-box">'
            f'<div class="hl-val" style="color:{color};">{val}</div>'
            f'<div class="hl-lbl">{lbl}</div>'
            f'</div>')
