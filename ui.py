"""
ui.py — Upstox-Inspired UI System for ProTrader Terminal v3
Clean, modern, professional trading UI with purple/violet accent system.
"""

TERMINAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@300;400;500&family=Sora:wght@300;400;500;600;700;800&display=swap');

:root {
    /* ── Base Surfaces ── */
    --bg:       #0b0c10;
    --bg2:      #0f1117;
    --bg3:      #13151c;
    --surface:  #16181f;
    --card:     #1a1d27;
    --card2:    #1e2130;
    --overlay:  #232636;

    /* ── Borders ── */
    --border:   #252836;
    --border2:  #2d3148;
    --border3:  #363a52;

    /* ── Upstox Purple Accent System ── */
    --purple:   #6c63ff;
    --purple2:  #8b84ff;
    --purple3:  #4a43d4;
    --purple-bg: rgba(108,99,255,0.1);
    --purple-glow: rgba(108,99,255,0.25);

    /* ── Semantic Colors ── */
    --green:    #22c55e;
    --green2:   #16a34a;
    --green-bg: rgba(34,197,94,0.1);
    --red:      #ef4444;
    --red2:     #dc2626;
    --red-bg:   rgba(239,68,68,0.1);
    --gold:     #f59e0b;
    --gold-bg:  rgba(245,158,11,0.1);
    --blue:     #3b82f6;
    --blue-bg:  rgba(59,130,246,0.1);
    --teal:     #14b8a6;
    --teal-bg:  rgba(20,184,166,0.1);
    --orange:   #f97316;

    /* ── Text ── */
    --text:     #e2e4ef;
    --text2:    #9599b3;
    --text3:    #5c6180;
    --white:    #f8f9ff;

    /* ── Fonts ── */
    --font-ui:   'DM Sans', sans-serif;
    --font-mono: 'DM Mono', monospace;
    --font-disp: 'Sora', sans-serif;
}

/* ════════════════════════════════════════════
   BASE RESET
════════════════════════════════════════════ */
html, body, [class*="css"] {
    font-family: var(--font-ui);
    background: var(--bg);
    color: var(--text);
    font-size: 13px;
    line-height: 1.5;
}

.stApp { background: var(--bg); }

::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--purple); }

/* ════════════════════════════════════════════
   TOP HEADER BAR — Upstox Style
════════════════════════════════════════════ */
.upx-header {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 0 24px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
    position: relative;
}
.upx-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}
.upx-logo-mark {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, var(--purple), var(--purple2));
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-disp);
    font-weight: 800;
    font-size: 0.85rem;
    color: #fff;
    letter-spacing: -1px;
}
.upx-logo-text {
    font-family: var(--font-disp);
    font-size: 1rem;
    font-weight: 700;
    color: var(--white);
    letter-spacing: -0.3px;
}
.upx-logo-sub {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--purple2);
    letter-spacing: 2px;
    text-transform: uppercase;
}
.upx-status-row {
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--text3);
}
.upx-live-dot {
    width: 6px;
    height: 6px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(0.8); }
}

/* ════════════════════════════════════════════
   TICKER STRIP — slim Upstox style
════════════════════════════════════════════ */
.upx-ticker-wrap {
    background: var(--bg3);
    border-bottom: 1px solid var(--border);
    overflow: hidden;
    padding: 0;
    height: 32px;
    display: flex;
    align-items: center;
    margin-bottom: 16px;
}
.upx-ticker-inner {
    display: flex;
    gap: 0;
    animation: ticker-scroll 60s linear infinite;
    white-space: nowrap;
    align-items: center;
    height: 100%;
}
@keyframes ticker-scroll {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.upx-tick {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    padding: 0 18px;
    border-right: 1px solid var(--border);
    height: 32px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}
.upx-tick-name { color: var(--text2); font-weight: 500; }
.upx-tick-price { color: var(--text); font-weight: 500; }
.upx-tick-up    { color: var(--green); }
.upx-tick-dn    { color: var(--red); }

/* ════════════════════════════════════════════
   INDEX CARDS — Upstox pill style
════════════════════════════════════════════ */
.upx-idx {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.15s;
    cursor: default;
}
.upx-idx:hover {
    border-color: var(--border3);
    transform: translateY(-1px);
}
.upx-idx-tag {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text3);
    margin-bottom: 6px;
}
.upx-idx-price {
    font-family: var(--font-mono);
    font-size: 1.3rem;
    font-weight: 600;
    line-height: 1;
    color: var(--white);
    margin-bottom: 4px;
}
.upx-idx-chg {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 500;
}
.upx-idx-bar {
    position: absolute;
    bottom: 0; left: 0;
    height: 2px;
    width: 100%;
}
/* Per-index accent bars */
.upx-idx.bn .upx-idx-bar { background: var(--purple); }
.upx-idx.nf .upx-idx-bar { background: var(--blue); }
.upx-idx.sx .upx-idx-bar { background: var(--teal); }
.upx-idx.vx .upx-idx-bar { background: var(--gold); }
.upx-idx.it .upx-idx-bar { background: var(--orange); }
.upx-idx.mid .upx-idx-bar { background: var(--green); }

/* ════════════════════════════════════════════
   SECTION TITLES
════════════════════════════════════════════ */
.upx-sec {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
    margin-top: 4px;
}
.upx-sec-line {
    width: 3px;
    height: 18px;
    background: var(--purple);
    border-radius: 2px;
    flex-shrink: 0;
}
.upx-sec-title {
    font-family: var(--font-disp);
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--white);
    letter-spacing: 0.3px;
    text-transform: uppercase;
}
.upx-sec-badge {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    background: var(--purple-bg);
    color: var(--purple2);
    border: 1px solid var(--purple-glow);
    border-radius: 4px;
    padding: 2px 8px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ════════════════════════════════════════════
   METRIC CARDS — Upstox dashboard style
════════════════════════════════════════════ */
.upx-metric {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    position: relative;
    overflow: hidden;
}
.upx-metric::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 1px;
    background: linear-gradient(90deg, var(--purple) 0%, transparent 60%);
}
.upx-metric-val {
    font-family: var(--font-mono);
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--white);
    line-height: 1.1;
    margin-bottom: 4px;
}
.upx-metric-lbl {
    font-size: 0.68rem;
    font-weight: 500;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* ════════════════════════════════════════════
   SIGNAL CHIPS
════════════════════════════════════════════ */
.upx-sig {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.upx-sig::before { content: ''; width: 5px; height: 5px; border-radius: 50%; }

.upx-sbuy  { background: rgba(34,197,94,0.12);   color: var(--green);  border: 1px solid rgba(34,197,94,0.3);  }
.upx-sbuy::before  { background: var(--green); }
.upx-buy   { background: rgba(34,197,94,0.07);   color: #4ade80;       border: 1px solid rgba(34,197,94,0.2);  }
.upx-buy::before   { background: #4ade80; }
.upx-wbuy  { background: rgba(20,184,166,0.07);  color: var(--teal);   border: 1px solid rgba(20,184,166,0.2); }
.upx-wbuy::before  { background: var(--teal); }
.upx-ssell { background: rgba(239,68,68,0.12);   color: var(--red);    border: 1px solid rgba(239,68,68,0.3);  }
.upx-ssell::before { background: var(--red); }
.upx-sell  { background: rgba(239,68,68,0.07);   color: #f87171;       border: 1px solid rgba(239,68,68,0.2);  }
.upx-sell::before  { background: #f87171; }
.upx-wsell { background: rgba(249,115,22,0.07);  color: var(--orange); border: 1px solid rgba(249,115,22,0.2); }
.upx-wsell::before { background: var(--orange); }
.upx-neut  { background: rgba(245,158,11,0.07);  color: var(--gold);   border: 1px solid rgba(245,158,11,0.2); }
.upx-neut::before  { background: var(--gold); }

/* ════════════════════════════════════════════
   TRADE CARDS — position view
════════════════════════════════════════════ */
.upx-trade {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 8px;
    transition: border-color 0.15s;
}
.upx-trade:hover { border-color: var(--border3); }
.upx-trade.win  { border-left: 2px solid var(--green2); }
.upx-trade.loss { border-left: 2px solid var(--red2);   }
.upx-trade.open { border-left: 2px solid var(--purple); }

.upx-trade-head {
    font-family: var(--font-ui);
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--white);
}
.upx-trade-meta {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    color: var(--text3);
}

/* ════════════════════════════════════════════
   PROFIT BOOK ROWS
════════════════════════════════════════════ */
.upx-pb {
    background: rgba(34,197,94,0.05);
    border: 1px solid rgba(34,197,94,0.12);
    border-radius: 8px;
    padding: 7px 12px;
    margin: 3px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
}
.upx-pb-pct  { font-family: var(--font-mono); font-size: 0.78rem; color: var(--green); font-weight: 600; }
.upx-pb-pr   { font-family: var(--font-mono); font-size: 0.82rem; color: var(--white); }
.upx-pb-lbl  { font-size: 0.7rem; color: var(--text3); }
.upx-pb-abs  { font-family: var(--font-mono); font-size: 0.75rem; color: var(--teal); }

/* ════════════════════════════════════════════
   LEVEL BOXES — S/R/Target
════════════════════════════════════════════ */
.upx-lvl {
    border-radius: 8px;
    padding: 7px 12px;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 600;
    text-align: center;
}
.upx-lvl-r  { background: var(--red-bg);  border: 1px solid rgba(239,68,68,0.2);   color: var(--red);    }
.upx-lvl-s  { background: var(--green-bg);border: 1px solid rgba(34,197,94,0.2);   color: var(--green);  }
.upx-lvl-e  { background: var(--purple-bg);border:1px solid var(--purple-glow);    color: var(--purple2);}
.upx-lvl-tg { background: var(--teal-bg); border: 1px solid rgba(20,184,166,0.2);  color: var(--teal);   }

/* ════════════════════════════════════════════
   STRENGTH / PROGRESS BAR
════════════════════════════════════════════ */
.upx-bar-wrap {
    background: var(--bg2);
    border-radius: 99px;
    height: 4px;
    overflow: hidden;
    margin-top: 6px;
}
.upx-bar-fill {
    height: 4px;
    border-radius: 99px;
    transition: width 0.5s ease;
}

/* ════════════════════════════════════════════
   STATUS / ALERT BOXES
════════════════════════════════════════════ */
.upx-info    { background: var(--blue-bg);   border: 1px solid rgba(59,130,246,0.2);  border-radius: 10px; padding: 10px 14px; font-size: 0.78rem; color: #93c5fd; margin: 6px 0; }
.upx-warn    { background: var(--gold-bg);   border: 1px solid rgba(245,158,11,0.2);  border-radius: 10px; padding: 10px 14px; font-size: 0.78rem; color: #fcd34d; margin: 6px 0; }
.upx-success { background: var(--green-bg);  border: 1px solid rgba(34,197,94,0.2);   border-radius: 10px; padding: 10px 14px; font-size: 0.78rem; color: #86efac; margin: 6px 0; }
.upx-danger  { background: var(--red-bg);    border: 1px solid rgba(239,68,68,0.2);   border-radius: 10px; padding: 10px 14px; font-size: 0.78rem; color: #fca5a5; margin: 6px 0; }
.upx-purple  { background: var(--purple-bg); border: 1px solid var(--purple-glow);    border-radius: 10px; padding: 10px 14px; font-size: 0.78rem; color: var(--purple2); margin: 6px 0; }

/* ════════════════════════════════════════════
   OPTION CHAIN CHIPS
════════════════════════════════════════════ */
.upx-ce  { background: var(--blue-bg);   border: 1px solid rgba(59,130,246,0.25);  color: #60a5fa; border-radius: 5px; padding: 2px 9px; font-size: 0.68rem; font-family: var(--font-mono); font-weight: 600; }
.upx-pe  { background: var(--red-bg);    border: 1px solid rgba(239,68,68,0.25);   color: #f87171; border-radius: 5px; padding: 2px 9px; font-size: 0.68rem; font-family: var(--font-mono); font-weight: 600; }
.upx-atm { background: var(--gold-bg);   border: 1px solid rgba(245,158,11,0.3);   color: var(--gold); border-radius: 5px; padding: 2px 9px; font-size: 0.68rem; font-family: var(--font-mono); font-weight: 600; }
.upx-fut { background: var(--purple-bg); border: 1px solid var(--purple-glow);     color: var(--purple2); border-radius: 5px; padding: 2px 9px; font-size: 0.68rem; font-family: var(--font-mono); font-weight: 600; }

/* ════════════════════════════════════════════
   GREEK BOX
════════════════════════════════════════════ */
.upx-gk {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px;
    text-align: center;
}
.upx-gk-v { font-family: var(--font-mono); font-size: 0.95rem; font-weight: 600; color: var(--white); }
.upx-gk-l { font-size: 0.6rem; color: var(--text3); text-transform: uppercase; letter-spacing: 0.8px; margin-top: 2px; }

/* ════════════════════════════════════════════
   JOURNAL ROWS
════════════════════════════════════════════ */
.upx-jrow {
    background: var(--card);
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
.upx-jrow:hover { border-color: var(--border3); }

/* ════════════════════════════════════════════
   PNL FORMATTING
════════════════════════════════════════════ */
.upx-pnl-pos  { color: var(--green);  font-family: var(--font-mono); font-weight: 600; }
.upx-pnl-neg  { color: var(--red);    font-family: var(--font-mono); font-weight: 600; }
.upx-pnl-zero { color: var(--gold);   font-family: var(--font-mono); font-weight: 600; }

/* ════════════════════════════════════════════
   OPTION CHAIN TABLE
════════════════════════════════════════════ */
.upx-oc-hdr {
    display: grid;
    grid-template-columns: 1.4fr 0.7fr 0.6fr 0.55fr 1fr 1.1fr 1fr 0.55fr 0.6fr 0.7fr 1.4fr;
    padding: 8px 14px;
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 10px 10px 0 0;
    font-size: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text3);
    gap: 4px;
    font-family: var(--font-mono);
}
.upx-oc-row {
    display: grid;
    grid-template-columns: 1.4fr 0.7fr 0.6fr 0.55fr 1fr 1.1fr 1fr 0.55fr 0.6fr 0.7fr 1.4fr;
    padding: 7px 14px;
    border: 1px solid var(--border);
    border-top: none;
    font-size: 0.75rem;
    gap: 4px;
    align-items: center;
    transition: background 0.1s;
    font-family: var(--font-mono);
}
.upx-oc-row:hover { background: rgba(108,99,255,0.04); }
.upx-oc-row:last-child { border-radius: 0 0 10px 10px; }
.upx-oc-atm {
    background: rgba(245,158,11,0.06) !important;
    border-left: 2px solid var(--gold) !important;
    border-right: 2px solid var(--gold) !important;
}

/* ════════════════════════════════════════════
   STREAMLIT COMPONENT OVERRIDES
════════════════════════════════════════════ */

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] .stMarkdown { color: var(--text2) !important; }
[data-testid="stSidebar"] label { color: var(--text2) !important; font-family: var(--font-ui) !important; font-size: 0.78rem !important; }
[data-testid="stSidebar"] .stNumberInput input,
[data-testid="stSidebar"] .stTextInput input,
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.78rem !important;
}

/* Main inputs */
.stNumberInput input, .stTextInput input, .stTextAreaInput textarea {
    background: var(--surface) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.8rem !important;
}
.stNumberInput input:focus, .stTextInput input:focus {
    border-color: var(--purple) !important;
    box-shadow: 0 0 0 2px var(--purple-glow) !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}

/* Multiselect */
.stMultiSelect > div { background: var(--surface) !important; border: 1px solid var(--border2) !important; border-radius: 8px !important; }
.stMultiSelect span[data-baseweb="tag"] { background: var(--purple-bg) !important; border: 1px solid var(--purple-glow) !important; color: var(--purple2) !important; border-radius: 6px !important; }

/* Radio */
.stRadio label { color: var(--text2) !important; font-size: 0.8rem !important; }
.stRadio [data-baseweb="radio"] div[role="radio"][aria-checked="true"] { background: var(--purple) !important; border-color: var(--purple) !important; }

/* Checkbox */
.stCheckbox label { color: var(--text2) !important; font-size: 0.78rem !important; }
.stCheckbox [data-baseweb="checkbox"] div[data-checked="true"] { background: var(--purple) !important; border-color: var(--purple) !important; }

/* Slider */
.stSlider [data-baseweb="slider"] div[data-testid="stSliderThumb"] { background: var(--purple) !important; border: 2px solid var(--purple2) !important; }
.stSlider [data-baseweb="slider"] [role="progressbar"] { background: var(--purple) !important; }
.stSlider [data-baseweb="slider"] div[class*="track"] { background: var(--border2) !important; }

/* Buttons */
.stButton > button {
    background: var(--purple) !important;
    color: #fff !important;
    font-family: var(--font-ui) !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.3px !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 8px 18px !important;
    transition: background 0.15s, transform 0.1s !important;
}
.stButton > button:hover {
    background: var(--purple2) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
    background: var(--purple3) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--font-ui) !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
    color: var(--text3) !important;
    padding: 10px 18px !important;
    border-bottom: 2px solid transparent !important;
    background: transparent !important;
    transition: color 0.15s !important;
}
.stTabs [aria-selected="true"] {
    color: var(--purple2) !important;
    border-bottom-color: var(--purple) !important;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--text) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 16px !important; }

/* Progress */
.stProgress > div > div { background: linear-gradient(90deg, var(--purple3), var(--purple)) !important; }
.stProgress > div { background: var(--bg3) !important; border-radius: 99px !important; height: 4px !important; }

/* Dataframe */
.stDataFrame {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}
.stDataFrame table { background: var(--card) !important; color: var(--text) !important; }
.stDataFrame thead th { background: var(--bg3) !important; color: var(--text3) !important; font-family: var(--font-mono) !important; font-size: 0.68rem !important; border-bottom: 1px solid var(--border) !important; }
.stDataFrame tbody td { font-family: var(--font-mono) !important; font-size: 0.75rem !important; border-bottom: 1px solid var(--border) !important; }

/* Expander */
.streamlit-expanderHeader {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.78rem !important;
    color: var(--text) !important;
}
.streamlit-expanderContent {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    padding: 12px 14px !important;
}
[data-testid="metric-container"] label { color: var(--text3) !important; font-size: 0.68rem !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: var(--white) !important; font-family: var(--font-mono) !important; font-size: 1.1rem !important; }
[data-testid="metric-container"] [data-testid="stMetricDelta"] { font-family: var(--font-mono) !important; font-size: 0.72rem !important; }

/* Info / Warning / Success / Error messages */
.stAlert { border-radius: 10px !important; border-width: 1px !important; font-family: var(--font-ui) !important; font-size: 0.8rem !important; }

/* Spinner */
.stSpinner > div { border-top-color: var(--purple) !important; }

/* Download button */
.stDownloadButton > button {
    background: var(--surface) !important;
    border: 1px solid var(--border2) !important;
    color: var(--text2) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.78rem !important;
    border-radius: 8px !important;
}
.stDownloadButton > button:hover {
    background: var(--card2) !important;
    border-color: var(--border3) !important;
    color: var(--text) !important;
}

/* ════════════════════════════════════════════
   UTILITY CLASSES
════════════════════════════════════════════ */
.up    { color: var(--green) !important; }
.dn    { color: var(--red) !important; }
.flat  { color: var(--gold) !important; }
.muted { color: var(--text3) !important; }
.mono  { font-family: var(--font-mono) !important; }

/* ════════════════════════════════════════════
   WATCHLIST / SCANNER ROWS
════════════════════════════════════════════ */
.upx-stock-row {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 14px;
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    transition: border-color 0.15s, background 0.15s;
    cursor: pointer;
}
.upx-stock-row:hover { border-color: var(--purple-glow); background: var(--card2); }
.upx-stock-sym { font-family: var(--font-ui); font-weight: 600; font-size: 0.85rem; color: var(--white); }
.upx-stock-name { font-size: 0.68rem; color: var(--text3); margin-top: 1px; }
.upx-stock-price { font-family: var(--font-mono); font-size: 0.9rem; font-weight: 600; color: var(--white); text-align: right; }
.upx-stock-chg   { font-family: var(--font-mono); font-size: 0.7rem; text-align: right; }

/* ════════════════════════════════════════════
   AUTO-TRADER STATUS PANEL
════════════════════════════════════════════ */
.upx-auto-panel {
    background: var(--card);
    border: 1px solid var(--purple-glow);
    border-radius: 14px;
    padding: 24px;
    text-align: center;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
}
.upx-auto-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--purple), transparent);
}
.upx-auto-title {
    font-family: var(--font-disp);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--white);
    letter-spacing: -0.3px;
    margin-bottom: 6px;
}
.upx-auto-sub {
    font-size: 0.75rem;
    color: var(--text3);
    line-height: 1.6;
}

/* ════════════════════════════════════════════
   AI BADGE
════════════════════════════════════════════ */
.upx-ai-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--purple-bg);
    border: 1px solid var(--purple-glow);
    border-radius: 99px;
    padding: 3px 10px;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--purple2);
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.upx-ai-dot {
    width: 5px; height: 5px;
    background: var(--purple);
    border-radius: 50%;
    animation: pulse-dot 1.5s ease-in-out infinite;
}

/* ════════════════════════════════════════════
   FOOTER
════════════════════════════════════════════ */
.upx-footer {
    background: var(--bg2);
    border-top: 1px solid var(--border);
    padding: 12px 24px;
    text-align: center;
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--text3);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}
.upx-footer-dot { color: var(--border3); }
.upx-footer-warn { color: #f87171; }

/* ════════════════════════════════════════════
   SPARKLINE MINI CHART PLACEHOLDER
════════════════════════════════════════════ */
.upx-spark {
    height: 28px;
    display: flex;
    align-items: flex-end;
    gap: 1px;
    opacity: 0.7;
}
.upx-spark span {
    flex: 1;
    border-radius: 1px 1px 0 0;
    min-width: 3px;
}

</style>
"""

# ══════════════════════════════════════════════════════════════════
# HELPER RENDER FUNCTIONS — Drop-in replacements, same API
# ══════════════════════════════════════════════════════════════════

def sig_badge(rec):
    """Returns Upstox-styled signal badge HTML."""
    cls = {
        "STRONG BUY":  "upx-sbuy",
        "BUY":         "upx-buy",
        "WEAK BUY":    "upx-wbuy",
        "STRONG SELL": "upx-ssell",
        "SELL":        "upx-sell",
        "WEAK SELL":   "upx-wsell",
        "NEUTRAL":     "upx-neut",
        "AVOID":       "upx-ssell",
    }.get(rec, "upx-neut")
    return f'<span class="upx-sig {cls}">{rec}</span>'


def strength_bar(pct, color="#6c63ff"):
    """Upstox-style thin progress bar."""
    return (
        f'<div class="upx-bar-wrap">'
        f'<div class="upx-bar-fill" style="width:{pct}%;background:{color};"></div>'
        f'</div>'
    )


def pnl_fmt(val):
    """Color-coded P&L display."""
    if val > 0:
        return f'<span class="upx-pnl-pos">▲ ₹{val:,.2f}</span>'
    elif val < 0:
        return f'<span class="upx-pnl-neg">▼ ₹{abs(val):,.2f}</span>'
    return f'<span class="upx-pnl-zero">₹0.00</span>'


def ticker_item(name, price, pct):
    """Single ticker strip item."""
    cls   = "upx-tick-up" if pct >= 0 else "upx-tick-dn"
    arrow = "▲" if pct >= 0 else "▼"
    return (
        f'<span class="upx-tick">'
        f'<span class="upx-tick-name">{name}</span>'
        f'<span class="upx-tick-price">{price:,.2f}</span>'
        f'<span class="{cls}">{arrow}{abs(pct):.2f}%</span>'
        f'</span>'
    )


def metric_card(val, lbl, color="var(--purple2)"):
    """Upstox-style metric card."""
    return (
        f'<div class="upx-metric">'
        f'<div class="upx-metric-val" style="color:{color};">{val}</div>'
        f'<div class="upx-metric-lbl">{lbl}</div>'
        f'</div>'
    )


def level_box(label, val, css_class):
    """S/R/Target level display box."""
    # Map old class names → new ones
    cls_map = {
        "lvl-r": "upx-lvl-r", "lvl-s": "upx-lvl-s",
        "lvl-e": "upx-lvl-e", "lvl-tg": "upx-lvl-tg",
    }
    c = cls_map.get(css_class, css_class)
    return (
        f'<div class="upx-lvl {c}">'
        f'<div style="font-size:0.58rem;opacity:0.65;margin-bottom:2px;">{label}</div>'
        f'₹{val:,.2f}'
        f'</div>'
    )


def profit_book_row(pct, price, label, profit_abs):
    """Profit booking target row."""
    return (
        f'<div class="upx-pb">'
        f'<span class="upx-pb-pct">+{pct}%</span>'
        f'<span class="upx-pb-pr">₹{price:.2f}</span>'
        f'<span class="upx-pb-lbl">{label}</span>'
        f'<span class="upx-pb-abs">+₹{profit_abs:.0f}</span>'
        f'</div>'
    )


def greek_box(val, label, color="var(--text)"):
    """Options Greek display box."""
    return (
        f'<div class="upx-gk">'
        f'<div class="upx-gk-v" style="color:{color}">{val}</div>'
        f'<div class="upx-gk-l">{label}</div>'
        f'</div>'
    )


def section_title(text, badge=None):
    """Upstox-style section header with vertical accent bar."""
    badge_html = f'<span class="upx-sec-badge">{badge}</span>' if badge else ""
    return (
        f'<div class="upx-sec">'
        f'<div class="upx-sec-line"></div>'
        f'<div class="upx-sec-title">{text}</div>'
        f'{badge_html}'
        f'</div>'
    )


def ai_badge(text="AI ACTIVE"):
    """Pulsing AI indicator badge."""
    return (
        f'<span class="upx-ai-badge">'
        f'<span class="upx-ai-dot"></span>{text}'
        f'</span>'
    )


def stock_row(symbol, name, price, chg_pct, signal=None):
    """Watchlist/scanner stock row."""
    chg_cls = "up" if chg_pct >= 0 else "dn"
    arrow   = "▲" if chg_pct >= 0 else "▼"
    sig_html = sig_badge(signal) if signal else ""
    return (
        f'<div class="upx-stock-row">'
        f'<div>'
        f'<div class="upx-stock-sym">{symbol.replace(".NS","").replace(".BO","")}</div>'
        f'<div class="upx-stock-name">{name}</div>'
        f'</div>'
        f'{sig_html}'
        f'<div>'
        f'<div class="upx-stock-price">₹{price:,.2f}</div>'
        f'<div class="upx-stock-chg {chg_cls}">{arrow}{abs(chg_pct):.2f}%</div>'
        f'</div>'
        f'</div>'
    )
