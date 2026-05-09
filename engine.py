"""
engine.py — Core analysis engine.
Indicators · Signal Scoring · Momentum · Fundamentals · Options Greeks
"""
import numpy as np
import pandas as pd
import yfinance as yf
import math
import time
import concurrent.futures
import warnings
warnings.filterwarnings("ignore")

# ─── NSE/BSE Universe ─────────────────────────────────────────────────────────
NSE_SYMBOLS = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS","SBIN.NS",
    "BAJFINANCE.NS","WIPRO.NS","AXISBANK.NS","KOTAKBANK.NS","LT.NS","HCLTECH.NS",
    "ASIANPAINT.NS","MARUTI.NS","TITAN.NS","SUNPHARMA.NS","BHARTIARTL.NS",
    "NESTLEIND.NS","ULTRACEMCO.NS","POWERGRID.NS","NTPC.NS","ONGC.NS","BPCL.NS",
    "COALINDIA.NS","IOC.NS","GAIL.NS","ADANIENT.NS","ADANIPORTS.NS","ADANIGREEN.NS",
    "TATAMOTORS.NS","TATASTEEL.NS","TATACONSUM.NS","CIPLA.NS","DIVISLAB.NS",
    "DRREDDY.NS","APOLLOHOSP.NS","HINDALCO.NS","JSWSTEEL.NS","TECHM.NS",
    "HDFCLIFE.NS","SBILIFE.NS","BAJAJFINSV.NS","EICHERMOT.NS","HEROMOTOCO.NS",
    "BRITANNIA.NS","PIDILITIND.NS","DABUR.NS","MARICO.NS","COLPAL.NS",
    "HAVELLS.NS","VOLTAS.NS","BERGEPAINT.NS","GODREJCP.NS","GRASIM.NS",
    "INDUSINDBK.NS","BANDHANBNK.NS","FEDERALBNK.NS","IDFCFIRSTB.NS","PNB.NS",
    "BANKBARODA.NS","CANBK.NS","UNIONBANK.NS","SAIL.NS","NMDC.NS",
    "RECLTD.NS","PFC.NS","IRFC.NS","NHPC.NS","SJVN.NS",
    "ZOMATO.NS","NYKAA.NS","PAYTM.NS","IRCTC.NS","HAPPSTMNDS.NS",
    "PERSISTENT.NS","COFORGE.NS","MPHASIS.NS","LTIM.NS","OFSS.NS",
    "KPITTECH.NS","TATAELXSI.NS","DIXON.NS","AMBER.NS","CROMPTON.NS",
    "PAGEIND.NS","TRENT.NS","DMART.NS","ABFRL.NS","INDIGO.NS",
    "CONCOR.NS","HDFCAMC.NS","ASTRAL.NS","POLYCAB.NS","CUMMINSIND.NS",
    "BHEL.NS","ABB.NS","SIEMENS.NS","AMBUJACEM.NS","ACC.NS","SHREECEM.NS",
    "MUTHOOTFIN.NS","CHOLAFIN.NS","SHRIRAMFIN.NS","AUROPHARMA.NS",
    "TORNTPHARM.NS","LUPIN.NS","BIOCON.NS","ALKEM.NS","GLENMARK.NS",
    "ZYDUSLIFE.NS","APOLLOTYRE.NS","MRF.NS","BALKRISIND.NS","EXIDEIND.NS",
    "MOTHERSON.NS","BOSCHLTD.NS","MINDTREE.NS","MCDOWELL-N.NS","UBL.NS",
    "JUBLFOOD.NS","WESTLIFE.NS","DEVYANI.NS","SAPIENT.NS","NAUKRI.NS",
    "JUSTDIAL.NS","INDIGOPNTS.NS","DEEPAKNTR.NS","FINPIPE.NS","FLUOROCHEM.NS",
    "CLEAN.NS","LALPATHLAB.NS","METROPOLIS.NS","THYROCARE.NS","AAVAS.NS",
    "HOMEFIRST.NS","APTUS.NS","EQUITASBNK.NS","SURYODAY.NS","UJJIVANSFB.NS",
    "RBLBANK.NS","DCBBANK.NS","KARNATAKA.NS","SOUTHBANK.NS","CSBBANK.NS",
    "JINDALSAW.NS","JSPL.NS","RATNAMANI.NS","MAHINDCIE.NS","ENDURANCE.NS",
    "SCHAEFFLER.NS","TIMKEN.NS","SKF.NS","GREAVESCOT.NS","BHARAT.NS",
    "KALYANKJIL.NS","SENCO.NS","RAJRATAN.NS","GOLDIAM.NS","THANGAMAYL.NS",
    "ZENTEC.NS","RATEGAIN.NS","CARTRADE.NS","EASEMYTRIP.NS","IXIGO.NS",
    "CAMPUS.NS","BATAINDIA.NS","RELAXO.NS","METRO.NS","PARADEEP.NS",
    "GSPL.NS","PETRONET.NS","GUJGASLTD.NS","IGL.NS","MGL.NS",
    "TORNTPOWER.NS","TATAPOWER.NS","ADANIPOWER.NS","CESC.NS","JPPOWER.NS",
    "IREDA.NS","RVNL.NS","RAILTEL.NS","RITES.NS","IRCON.NS",
    "BEL.NS","HAL.NS","COCHINSHIP.NS","MAZAGON.NS","GRSE.NS",
    "NATIONALUM.NS","VEDL.NS","HINDCOPPER.NS","MOIL.NS","GMRAIRPORT.NS",
    "AIAENG.NS","GRINDWELL.NS","KENNAMETAL.NS","CARBORUNIV.NS","CERA.NS",
    "SUPREMEIND.NS","FINOLEX.NS","BAJAJELEC.NS","ORIENTELEC.NS","VGUARD.NS",
    "SYMPHONY.NS","BLUESTARCO.NS","WHIRLPOOL.NS","HAWKINCOOK.NS","TTK.NS",
    "LAURUSLABS.NS","GRANULES.NS","SOLARA.NS","NATCOPHARM.NS","AJANTPHARM.NS",
    "SUVEN.NS","NEULANDLAB.NS","DIVILAB.NS","SEQUENT.NS","GLAND.NS",
]

BSE_SYMBOLS = [
    "SENSEX.BO","RELIANCE.BO","TCS.BO","INFY.BO","HDFCBANK.BO",
    "ICICIBANK.BO","SBIN.BO","BAJFINANCE.BO","WIPRO.BO","LT.BO",
    "AXISBANK.BO","KOTAKBANK.BO","MARUTI.BO","SUNPHARMA.BO","TATAMOTORS.BO",
    "TATASTEEL.BO","BHARTIARTL.BO","ASIANPAINT.BO","TITAN.BO","HCLTECH.BO",
    "NESTLEIND.BO","ULTRACEMCO.BO","POWERGRID.BO","NTPC.BO","ONGC.BO",
    "ADANIENT.BO","ADANIPORTS.BO","CIPLA.BO","DRREDDY.BO","APOLLOHOSP.BO",
]

INDEX_SYMBOLS = {
    "NIFTY50":    "^NSEI",
    "BANKNIFTY":  "^NSEBANK",
    "NIFTYIT":    "^CNXIT",
    "NIFTYMID":   "^NSMIDCP",
    "SENSEX":     "^BSESN",
    "VIX":        "^INDIAVIX",
    "NIFTYPHARMA":"^CNXPHARMA",
    "NIFTYAUTO":  "^CNXAUTO",
    "NIFTYFMCG":  "^CNXFMCG",
    "NIFTYMETAL":  "^CNXMETAL",
}

FUTURES_SYMBOLS = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
    "SBIN.NS","BAJFINANCE.NS","NIFTY_FUT","BANKNIFTY_FUT",
    "TATAMOTORS.NS","TATASTEEL.NS","AXISBANK.NS","WIPRO.NS","LT.NS",
    "KOTAKBANK.NS","ASIANPAINT.NS","MARUTI.NS","SUNPHARMA.NS",
    "BHARTIARTL.NS","HCLTECH.NS","ADANIENT.NS","ADANIPORTS.NS",
    "JSWSTEEL.NS","HINDALCO.NS","ONGC.NS","NTPC.NS","POWERGRID.NS",
]

# ─── Helpers ──────────────────────────────────────────────────────────────────
def _sf(val, default=0.0):
    try:
        v = float(val.iloc[-1]) if isinstance(val, pd.Series) else float(val)
        return v if np.isfinite(v) else default
    except Exception:
        return default

# ─── Data Fetching ────────────────────────────────────────────────────────────
_price_cache = {}

def get_ohlcv(symbol, period="3mo", interval="1d"):
    cache_key = f"{symbol}_{period}_{interval}"
    cached = _price_cache.get(cache_key)
    if cached and (time.time() - cached["ts"]) < 60:
        return cached["df"]
    try:
        df = yf.Ticker(symbol).history(period=period, interval=interval)
        if not df.empty:
            df.index = pd.to_datetime(df.index)
            _price_cache[cache_key] = {"df": df, "ts": time.time()}
            return df
    except Exception:
        pass
    return None

def get_live_price(symbol):
    try:
        t  = yf.Ticker(symbol)
        lp = t.fast_info.last_price
        return float(lp) if lp and np.isfinite(float(lp)) and float(lp) > 0 else None
    except Exception:
        return None

def get_fundamentals(symbol):
    try:
        info = yf.Ticker(symbol).info
        return {
            "name":        info.get("longName", symbol),
            "sector":      info.get("sector", "N/A"),
            "industry":    info.get("industry", "N/A"),
            "pe":          info.get("trailingPE"),
            "pb":          info.get("priceToBook"),
            "roe":         info.get("returnOnEquity"),
            "de":          info.get("debtToEquity"),
            "eps":         info.get("trailingEps"),
            "beta":        info.get("beta"),
            "mktcap":      info.get("marketCap"),
            "52h":         info.get("fiftyTwoWeekHigh"),
            "52l":         info.get("fiftyTwoWeekLow"),
            "avg_vol":     info.get("averageVolume"),
            "div_yield":   info.get("dividendYield"),
            "earnings_ts": info.get("earningsTimestamp"),
        }
    except Exception:
        return {}

# ─── Indicator Engine ─────────────────────────────────────────────────────────
def compute_indicators(df):
    if df is None or len(df) < 20:
        return {}
    try:
        c = df["Close"].astype(float)
        h = df["High"].astype(float)
        l = df["Low"].astype(float)
        v = df["Volume"].astype(float) if "Volume" in df.columns else pd.Series(np.ones(len(c)), index=c.index)

        # RSI
        d     = c.diff()
        g     = d.clip(lower=0).ewm(span=14, adjust=False).mean()
        ls    = (-d.clip(upper=0)).ewm(span=14, adjust=False).mean()
        rsi   = 100 - 100 / (1 + g / ls.replace(0, np.nan))

        # MACD
        e12   = c.ewm(span=12, adjust=False).mean()
        e26   = c.ewm(span=26, adjust=False).mean()
        macd  = e12 - e26
        msig  = macd.ewm(span=9, adjust=False).mean()
        mhist = macd - msig

        # Bollinger Bands
        s20   = c.rolling(20).mean()
        sd20  = c.rolling(20).std()
        bbu   = s20 + 2*sd20
        bbl   = s20 - 2*sd20
        bbpct = (c - bbl) / (bbu - bbl + 0.001)

        # ATR
        tr    = pd.concat([h-l,(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1)
        atr   = tr.rolling(14).mean()

        # EMAs
        e5    = c.ewm(span=5,   adjust=False).mean()
        e9    = c.ewm(span=9,   adjust=False).mean()
        e13   = c.ewm(span=13,  adjust=False).mean()
        e21   = c.ewm(span=21,  adjust=False).mean()
        e50   = c.ewm(span=50,  adjust=False).mean()
        e200  = c.ewm(span=200, adjust=False).mean()

        # Stochastic
        l14   = l.rolling(14).min()
        h14   = h.rolling(14).max()
        sk    = 100*(c-l14)/(h14-l14+0.001)
        sd    = sk.rolling(3).mean()

        # ADX
        pdm   = (h.diff()).clip(lower=0)
        ndm   = (-l.diff()).clip(lower=0)
        pdi   = 100*pdm.ewm(span=14).mean()/atr.replace(0,np.nan)
        ndi   = 100*ndm.ewm(span=14).mean()/atr.replace(0,np.nan)
        dx    = 100*(pdi-ndi).abs()/(pdi+ndi+0.001)
        adx   = dx.ewm(span=14).mean()

        # Williams %R
        wr    = -100*(h14-c)/(h14-l14+0.001)

        # CCI
        tp    = (h+l+c)/3
        cci   = (tp - tp.rolling(20).mean())/(0.015*tp.rolling(20).std()+0.001)

        # Volume analysis
        vma20 = v.rolling(20).mean().replace(0, np.nan)
        vratio= v/vma20
        obv   = (np.sign(c.diff())*v).cumsum()

        # Pivot / S&R
        pivot = (h.iloc[-1]+l.iloc[-1]+c.iloc[-1])/3
        r1    = 2*pivot - l.iloc[-1]
        s1    = 2*pivot - h.iloc[-1]
        r2    = pivot + (h.iloc[-1]-l.iloc[-1])
        s2    = pivot - (h.iloc[-1]-l.iloc[-1])
        r3    = h.iloc[-1] + 2*(pivot-l.iloc[-1])
        s3    = l.iloc[-1] - 2*(h.iloc[-1]-pivot)

        # Momentum
        m5    = float((c.iloc[-1]-c.iloc[-5])/c.iloc[-5]*100) if len(c)>=5  else 0
        m20   = float((c.iloc[-1]-c.iloc[-20])/c.iloc[-20]*100) if len(c)>=20 else 0
        m60   = float((c.iloc[-1]-c.iloc[-60])/c.iloc[-60]*100) if len(c)>=60 else 0

        # Squeeze Momentum (TTM style)
        kc_u  = s20 + 1.5*atr
        kc_l  = s20 - 1.5*atr
        squeeze = (bbl > kc_l) & (bbu < kc_u)

        # Day change
        prev  = c.shift(1)
        day_chg = ((c-prev)/prev.replace(0,np.nan))*100

        # Supertrend (simplified)
        hl2   = (h+l)/2
        st_up = hl2 - 3*atr
        st_dn = hl2 + 3*atr

        return {
            "rsi": _sf(rsi), "rsi_s": rsi,
            "macd": _sf(macd), "macd_sig": _sf(msig), "macd_hist": _sf(mhist),
            "macd_s": macd, "msig_s": msig,
            "bb_pct": _sf(bbpct), "bb_u": _sf(bbu), "bb_l": _sf(bbl), "bb_mid": _sf(s20),
            "atr": _sf(atr),
            "e5": _sf(e5), "e9": _sf(e9), "e13": _sf(e13),
            "e21": _sf(e21), "e50": _sf(e50), "e200": _sf(e200),
            "sk": _sf(sk), "sd": _sf(sd),
            "adx": _sf(adx), "pdi": _sf(pdi), "ndi": _sf(ndi),
            "wr": _sf(wr), "cci": _sf(cci),
            "vr": _sf(vratio), "obv": _sf(obv),
            "pivot": pivot, "r1": r1, "r2": r2, "r3": r3,
            "s1": s1, "s2": s2, "s3": s3,
            "m5": m5, "m20": m20, "m60": m60,
            "squeeze": bool(squeeze.iloc[-1]),
            "close": _sf(c), "high": _sf(h), "low": _sf(l),
            "volume": _sf(v), "avg_vol_20": _sf(vma20),
            "day_chg": _sf(day_chg),
            "st_up": _sf(st_up), "st_dn": _sf(st_dn),
        }
    except Exception as e:
        return {}

# ─── Candlestick Patterns ─────────────────────────────────────────────────────
def detect_patterns(df):
    if df is None or len(df) < 4:
        return []
    patterns = []
    try:
        o = df["Open"].astype(float)
        h = df["High"].astype(float)
        l = df["Low"].astype(float)
        c = df["Close"].astype(float)
        o1,o2,o3 = o.iloc[-3],o.iloc[-2],o.iloc[-1]
        h1,h2,h3 = h.iloc[-3],h.iloc[-2],h.iloc[-1]
        l1,l2,l3 = l.iloc[-3],l.iloc[-2],l.iloc[-1]
        c1,c2,c3 = c.iloc[-3],c.iloc[-2],c.iloc[-1]
        b3 = abs(c3-o3); r3 = h3-l3 if h3!=l3 else 0.001
        b2 = abs(c2-o2); r2 = h2-l2 if h2!=l2 else 0.001
        lw3 = min(o3,c3)-l3; uw3 = h3-max(o3,c3)
        lw2 = min(o2,c2)-l2; uw2 = h2-max(o2,c2)

        if b3/r3 < 0.1:                                               patterns.append(("Doji","NEUTRAL"))
        if lw3>2*b3 and uw3<b3 and c2<o2:                             patterns.append(("Hammer","BUY"))
        if uw3>2*b3 and lw3<b3 and c2>o2:                             patterns.append(("Shooting Star","SELL"))
        if c2<o2 and c3>o3 and o3<c2 and c3>o2:                       patterns.append(("Bullish Engulfing","BUY"))
        if c2>o2 and c3<o3 and o3>c2 and c3<o2:                       patterns.append(("Bearish Engulfing","SELL"))
        if c1<o1 and b2<r2*0.3 and c3>o3 and c3>(o1+c1)/2:            patterns.append(("Morning Star","BUY"))
        if c1>o1 and b2<r2*0.3 and c3<o3 and c3<(o1+c1)/2:            patterns.append(("Evening Star","SELL"))
        if c3>o3 and b3>b2*2 and lw3<b3*0.3 and uw3<b3*0.3:          patterns.append(("Marubozu Bull","BUY"))
        if c3<o3 and b3>b2*2 and lw3<b3*0.3 and uw3<b3*0.3:          patterns.append(("Marubozu Bear","SELL"))
        if lw3>2*b3 and c3>o3:                                         patterns.append(("Dragonfly Doji","BUY"))
        if uw3>2*b3 and c3<o3:                                         patterns.append(("Gravestone Doji","SELL"))
        if c1>o1 and c2>o2 and c3>o3 and c3>c2>c1:                    patterns.append(("Three White Soldiers","BUY"))
        if c1<o1 and c2<o2 and c3<o3 and c3<c2<c1:                    patterns.append(("Three Black Crows","SELL"))
    except Exception:
        pass
    return patterns

# ─── RSI Divergence ───────────────────────────────────────────────────────────
def detect_divergence(df, ind):
    if df is None or len(df)<15 or not ind:
        return None
    try:
        c   = df["Close"].astype(float).values[-20:]
        rsi = ind.get("rsi_s")
        if rsi is None or len(rsi)<20:
            return None
        rsi = rsi.values[-20:]
        lows  = [i for i in range(1,len(c)-1) if c[i]<c[i-1] and c[i]<c[i+1]]
        highs = [i for i in range(1,len(c)-1) if c[i]>c[i-1] and c[i]>c[i+1]]
        if len(lows)>=2:
            i1,i2 = lows[-2],lows[-1]
            if c[i2]<c[i1] and rsi[i2]>rsi[i1] and rsi[i1]<50:
                return ("BULLISH_DIV","BUY","RSI bullish divergence — higher low while price makes lower low")
        if len(highs)>=2:
            i1,i2 = highs[-2],highs[-1]
            if c[i2]>c[i1] and rsi[i2]<rsi[i1] and rsi[i1]>50:
                return ("BEARISH_DIV","SELL","RSI bearish divergence — lower high while price makes higher high")
    except Exception:
        pass
    return None

# ─── Volume Spike Detection ───────────────────────────────────────────────────
def volume_spike(ind):
    vr = ind.get("vr", 1.0) if ind else 1.0
    if vr >= 3.0:   return "EXTREME", vr
    elif vr >= 2.0: return "HIGH", vr
    elif vr >= 1.5: return "ABOVE_AVG", vr
    return "NORMAL", vr

# ─── Master Signal Scorer ─────────────────────────────────────────────────────
def score_signal(ind, fund, df, market_mood="NEUTRAL", vix=15.0, mode="INTRADAY"):
    """
    Comprehensive signal scorer.
    Returns (recommendation, strength, buy_score, sell_score, reasoning)
    """
    if not ind:
        return "NEUTRAL", 0, 0, 0, ["No data"]

    buy = 0; sell = 0; reasons = []

    def g(k, d=0.0):
        v = ind.get(k, d)
        try: return float(v) if np.isfinite(float(v)) else d
        except: return d

    rsi   = g("rsi", 50)
    macd  = g("macd"); msig  = g("macd_sig"); mhist = g("macd_hist")
    bb    = g("bb_pct", 0.5)
    sk    = g("sk", 50);  sd    = g("sd", 50)
    adx   = g("adx", 20); pdi   = g("pdi"); ndi   = g("ndi")
    wr    = g("wr", -50); cci   = g("cci")
    vr    = g("vr", 1.0)
    close = g("close"); e9=g("e9"); e13=g("e13"); e21=g("e21"); e50=g("e50"); e200=g("e200")
    m5    = g("m5"); m20 = g("m20"); m60 = g("m60")
    atr   = g("atr"); squeeze = ind.get("squeeze", False)
    s1=g("s1"); s2=g("s2"); r1=g("r1"); r2=g("r2")

    # ── Market Mood ───────────────────────────────────────────────────────────
    if market_mood == "BEARISH":
        sell += 2; reasons.append("🔴 Market BEARISH → SELL +2")
    elif market_mood == "BULLISH":
        buy  += 1; reasons.append("🟢 Market BULLISH → BUY +1")
    if vix > 22:
        sell += 1; reasons.append(f"⚠️ VIX={vix:.1f} elevated → caution")
    elif vix < 13:
        buy  += 1; reasons.append(f"🟢 VIX={vix:.1f} low → favourable")

    # ── RSI ───────────────────────────────────────────────────────────────────
    if rsi < 25:   buy  += 4; reasons.append(f"RSI={rsi:.1f} DEEPLY oversold → BUY +4")
    elif rsi < 35: buy  += 3; reasons.append(f"RSI={rsi:.1f} oversold → BUY +3")
    elif rsi < 45: buy  += 1; reasons.append(f"RSI={rsi:.1f} mild oversold → BUY +1")
    elif rsi > 80: sell += 4; reasons.append(f"RSI={rsi:.1f} DEEPLY overbought → SELL +4")
    elif rsi > 70: sell += 3; reasons.append(f"RSI={rsi:.1f} overbought → SELL +3")
    elif rsi > 60: sell += 1; reasons.append(f"RSI={rsi:.1f} elevated → SELL +1")
    else:          reasons.append(f"RSI={rsi:.1f} neutral")

    # ── MACD ──────────────────────────────────────────────────────────────────
    if macd > msig and mhist > 0:
        buy  += 2; reasons.append(f"MACD bullish crossover (hist={mhist:.3f}) → BUY +2")
    elif macd < msig and mhist < 0:
        sell += 2; reasons.append(f"MACD bearish crossover → SELL +2")
    if mhist > 0 and ind.get("macd_s") is not None:
        ms = ind["macd_s"]
        if len(ms)>=2 and float(ms.iloc[-1])>float(ms.iloc[-2]):
            buy += 1; reasons.append("MACD histogram expanding → BUY +1")

    # ── Bollinger Bands ───────────────────────────────────────────────────────
    if bb < 0.05:   buy  += 3; reasons.append(f"Price at lower BB ({bb:.2f}) → BUY +3")
    elif bb < 0.15: buy  += 2; reasons.append(f"Price near lower BB → BUY +2")
    elif bb > 0.95: sell += 3; reasons.append(f"Price at upper BB ({bb:.2f}) → SELL +3")
    elif bb > 0.85: sell += 2; reasons.append(f"Price near upper BB → SELL +2")

    # ── EMA Stack ─────────────────────────────────────────────────────────────
    if close>0 and e9>0 and e13>0 and e21>0 and e50>0:
        if close > e9 > e13 > e21 > e50:
            buy  += 4; reasons.append("Perfect bull EMA stack: price>9>13>21>50 → BUY +4")
        elif close < e9 < e13 < e21 < e50:
            sell += 4; reasons.append("Perfect bear EMA stack: price<9<13<21<50 → SELL +4")
        elif close > e21 > e50:
            buy  += 2; reasons.append("Price above EMA21 & 50 → BUY +2")
        elif close < e21 < e50:
            sell += 2; reasons.append("Price below EMA21 & 50 → SELL +2")
        if e200 > 0:
            if close > e200: buy  += 1; reasons.append("Price above EMA200 (macro uptrend) → BUY +1")
            else:            sell += 1; reasons.append("Price below EMA200 (macro downtrend) → SELL +1")

    # ── Stochastic ────────────────────────────────────────────────────────────
    if sk < 20 and sk > sd:
        buy  += 2; reasons.append(f"Stoch K={sk:.0f} oversold+crossing up → BUY +2")
    elif sk < 15:
        buy  += 1; reasons.append(f"Stoch K={sk:.0f} deep oversold → BUY +1")
    elif sk > 80 and sk < sd:
        sell += 2; reasons.append(f"Stoch K={sk:.0f} overbought+crossing dn → SELL +2")
    elif sk > 85:
        sell += 1; reasons.append(f"Stoch K={sk:.0f} deep overbought → SELL +1")

    # ── ADX ───────────────────────────────────────────────────────────────────
    if adx > 30:
        if pdi > ndi: buy  += 3; reasons.append(f"ADX={adx:.0f} STRONG uptrend → BUY +3")
        else:         sell += 3; reasons.append(f"ADX={adx:.0f} STRONG downtrend → SELL +3")
    elif adx > 20:
        if pdi > ndi: buy  += 1; reasons.append(f"ADX={adx:.0f} moderate uptrend → BUY +1")
        else:         sell += 1; reasons.append(f"ADX={adx:.0f} moderate downtrend → SELL +1")

    # ── Williams %R ───────────────────────────────────────────────────────────
    if wr < -85:  buy  += 2; reasons.append(f"Williams R={wr:.0f} deeply oversold → BUY +2")
    elif wr < -70: buy  += 1; reasons.append(f"Williams R={wr:.0f} oversold → BUY +1")
    elif wr > -10: sell += 2; reasons.append(f"Williams R={wr:.0f} overbought → SELL +2")
    elif wr > -20: sell += 1; reasons.append(f"Williams R={wr:.0f} elevated → SELL +1")

    # ── CCI ───────────────────────────────────────────────────────────────────
    if cci < -150: buy  += 2; reasons.append(f"CCI={cci:.0f} extreme oversold → BUY +2")
    elif cci < -100: buy+= 1; reasons.append(f"CCI={cci:.0f} oversold → BUY +1")
    elif cci > 150: sell+= 2; reasons.append(f"CCI={cci:.0f} extreme overbought → SELL +2")
    elif cci > 100: sell+= 1; reasons.append(f"CCI={cci:.0f} overbought → SELL +1")

    # ── Volume ────────────────────────────────────────────────────────────────
    vs, vr_val = volume_spike(ind)
    if vs in ("EXTREME","HIGH") and buy > sell:
        buy  += 2; reasons.append(f"Volume spike {vr_val:.1f}x confirms bullish → BUY +2")
    elif vs in ("EXTREME","HIGH") and sell > buy:
        sell += 2; reasons.append(f"Volume spike {vr_val:.1f}x confirms bearish → SELL +2")
    elif vs == "ABOVE_AVG":
        if buy > sell:  buy  += 1; reasons.append(f"Above-avg vol {vr_val:.1f}x → BUY +1")
        elif sell > buy: sell += 1; reasons.append(f"Above-avg vol {vr_val:.1f}x → SELL +1")

    # ── Squeeze Momentum ──────────────────────────────────────────────────────
    if squeeze:
        reasons.append("⚡ TTM Squeeze firing — big move imminent!")
        if buy > sell: buy += 2
        else:          sell += 2

    # ── Momentum ──────────────────────────────────────────────────────────────
    if m5 > 3:   buy  += 2; reasons.append(f"5D momentum +{m5:.1f}% → BUY +2")
    elif m5 > 1: buy  += 1; reasons.append(f"5D momentum +{m5:.1f}% → BUY +1")
    elif m5 < -3: sell += 2; reasons.append(f"5D momentum {m5:.1f}% → SELL +2")
    elif m5 < -1: sell += 1; reasons.append(f"5D momentum {m5:.1f}% → SELL +1")
    if m20 > 10: buy  += 1; reasons.append(f"20D momentum +{m20:.1f}% → BUY +1")
    elif m20 < -10: sell += 1; reasons.append(f"20D momentum {m20:.1f}% → SELL +1")

    # ── S/R Proximity ─────────────────────────────────────────────────────────
    if close > 0 and s1 > 0:
        if abs(close-s1)/close < 0.005: buy  += 2; reasons.append(f"Price at Support S1 ₹{s1:.2f} → BUY +2")
        if abs(close-s2)/close < 0.005: buy  += 3; reasons.append(f"Price at Strong Support S2 ₹{s2:.2f} → BUY +3")
        if abs(close-r1)/close < 0.005: sell += 2; reasons.append(f"Price at Resistance R1 ₹{r1:.2f} → SELL +2")
        if abs(close-r2)/close < 0.005: sell += 3; reasons.append(f"Price at Strong Resistance R2 ₹{r2:.2f} → SELL +3")

    # ── Candlestick Patterns ──────────────────────────────────────────────────
    if df is not None:
        for pname, psig in detect_patterns(df):
            if psig == "BUY":   buy  += 2; reasons.append(f"🕯️ {pname} → BUY +2")
            elif psig == "SELL": sell += 2; reasons.append(f"🕯️ {pname} → SELL +2")
            else: reasons.append(f"🕯️ {pname} (Neutral)")

    # ── RSI Divergence ────────────────────────────────────────────────────────
    div = detect_divergence(df, ind)
    if div:
        _, dsig, dmsg = div
        if dsig == "BUY":  buy  += 3; reasons.append(f"📐 {dmsg} → BUY +3")
        else:              sell += 3; reasons.append(f"📐 {dmsg} → SELL +3")

    # ── Fundamentals ──────────────────────────────────────────────────────────
    if fund:
        pe = fund.get("pe")
        pb = fund.get("pb")
        h52 = fund.get("52h"); l52 = fund.get("52l")
        if pe:
            try:
                pe = float(pe)
                if np.isfinite(pe) and pe > 0:
                    if pe < 15:   buy  += 1; reasons.append(f"Low P/E {pe:.1f} — cheap valuation → BUY +1")
                    elif pe > 60: sell += 1; reasons.append(f"High P/E {pe:.1f} — stretched → SELL +1")
            except: pass
        if h52 and l52 and close > 0:
            try:
                rng = float(h52)-float(l52)
                if rng > 0:
                    pos52 = (close-float(l52))/rng
                    if pos52 < 0.15: buy  += 2; reasons.append(f"Near 52W low ({pos52*100:.0f}%) → BUY +2")
                    elif pos52>0.90: sell += 1; reasons.append(f"Near 52W high ({pos52*100:.0f}%) → caution")
            except: pass

    # ── Final classification ──────────────────────────────────────────────────
    total    = max(buy+sell, 1)
    if buy > sell:
        net_str  = min(98, int(buy/total*100))
        if buy >= 15: rec = "STRONG BUY"
        elif buy >= 8: rec = "BUY"
        else:          rec = "WEAK BUY"
    elif sell > buy:
        net_str  = min(98, int(sell/total*100))
        if sell >= 15: rec = "STRONG SELL"
        elif sell >= 8: rec = "SELL"
        else:           rec = "WEAK SELL"
    else:
        rec = "NEUTRAL"; net_str = 50

    # Mode-specific adjustments
    if mode == "INTRADAY" and adx < 18:
        rec = "NEUTRAL"; reasons.append("ADX<18 — no clear trend, skip intraday")
    if mode == "DELIVERY" and net_str < 60:
        rec = "NEUTRAL"; reasons.append("Insufficient conviction for delivery trade")

    return rec, net_str, buy, sell, reasons

# ─── Trade Cost Calculators ────────────────────────────────────────────────────
def equity_cost(price, qty, side="BUY", delivery=False):
    tv = price*qty
    brok = 0 if delivery else min(20.0, tv*0.0003)
    stt  = tv*0.001 if (side=="SELL" or delivery) else (tv*0.001 if delivery else 0)
    exch = tv*0.0000345; sebi = tv*0.000001
    gst  = (brok+exch+sebi)*0.18
    stamp= tv*0.00015 if side=="BUY" else 0
    return round(brok+stt+exch+sebi+gst+stamp, 2)

def options_cost(prem, lots, lot_sz, side="BUY"):
    tv = prem*lots*lot_sz
    brok = min(40.0, tv*0.0003)
    stt  = tv*0.0005 if side=="SELL" else 0
    exch = tv*0.0000495; sebi = tv*0.000001
    gst  = (brok+exch+sebi)*0.18
    stamp= tv*0.00003 if side=="BUY" else 0
    return round(brok+stt+exch+sebi+gst+stamp, 2)

def futures_cost(price, lots, lot_sz, side="BUY"):
    tv = price*lots*lot_sz
    brok = min(40.0, tv*0.0003)
    stt  = tv*0.0001
    exch = tv*0.000019; sebi = tv*0.000001
    gst  = (brok+exch+sebi)*0.18
    stamp= tv*0.00002 if side=="BUY" else 0
    return round(brok+stt+exch+sebi+gst+stamp, 2)

# ─── Kelly Position Sizing ────────────────────────────────────────────────────
def kelly_size(capital, win_rate, rr_ratio, strength):
    try:
        f = win_rate - (1-win_rate)/max(rr_ratio,0.1)
        f = max(0.02, min(0.25, f))
        s = 0.4 + (strength/100)*0.6
        return round(capital*f*s, 2)
    except:
        return capital*0.05

# ─── Black-Scholes Greeks ─────────────────────────────────────────────────────
def _ncdf(x):
    return 0.5*(1+math.erf(x/math.sqrt(2)))

def bs_greeks(S, K, T, r, sigma, opt_type="CE"):
    try:
        if T<=0 or sigma<=0 or S<=0 or K<=0:
            return dict(price=0,delta=0,gamma=0,theta=0,vega=0,iv=sigma)
        d1 = (math.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*math.sqrt(T))
        d2 = d1 - sigma*math.sqrt(T)
        nd1= math.exp(-d1**2/2)/math.sqrt(2*math.pi)
        if opt_type=="CE":
            price = S*_ncdf(d1) - K*math.exp(-r*T)*_ncdf(d2)
            delta = _ncdf(d1)
            theta = (-(S*sigma*nd1)/(2*math.sqrt(T)) - r*K*math.exp(-r*T)*_ncdf(d2))/365
        else:
            price = K*math.exp(-r*T)*_ncdf(-d2) - S*_ncdf(-d1)
            delta = _ncdf(d1)-1
            theta = (-(S*sigma*nd1)/(2*math.sqrt(T)) + r*K*math.exp(-r*T)*_ncdf(-d2))/365
        gamma = nd1/(S*sigma*math.sqrt(T))
        vega  = S*math.sqrt(T)*nd1*0.01
        return dict(price=round(price,2),delta=round(delta,4),
                    gamma=round(gamma,6),theta=round(theta,2),
                    vega=round(vega,2),iv=round(sigma*100,1))
    except:
        return dict(price=0,delta=0,gamma=0,theta=0,vega=0,iv=0)

# ─── Option Chain Builder ─────────────────────────────────────────────────────
def build_chain(index_name, spot, expiry_date, vix, n_strikes=12):
    from datetime import datetime
    tick  = 100 if index_name=="BANKNIFTY" else 50
    lot   = 15  if index_name=="BANKNIFTY" else 25
    atm   = round(spot/tick)*tick
    dte   = max(1,(expiry_date-datetime.now().date()).days)
    T     = dte/365; r = 0.065
    iv    = max(0.08, vix/100*(1+0.05*math.sqrt(dte/365)))
    strikes = [atm+(i-n_strikes)*tick for i in range(2*n_strikes+1)]

    # Underlying data for signal
    sym = "^NSEBANK" if index_name=="BANKNIFTY" else "^NSEI"
    df  = get_ohlcv(sym, "1mo","1d")
    ind_u = compute_indicators(df)

    chain = []
    for K in strikes:
        ce = bs_greeks(spot,K,T,r,iv,"CE")
        pe = bs_greeks(spot,K,T,r,iv,"PE")
        # Signal scoring per option
        ce_sig = _option_signal(spot,K,atm,ind_u,df,"CE",ce["delta"],dte,vix)
        pe_sig = _option_signal(spot,K,atm,ind_u,df,"PE",pe["delta"],dte,vix)
        typ = "ATM" if K==atm else ("ITM-CE/OTM-PE" if K<atm else "OTM-CE/ITM-PE")
        chain.append({
            "strike":K,"type":typ,"is_atm":K==atm,"lot":lot,"dte":dte,"iv":ce["iv"],
            "ce_price":ce["price"],"ce_delta":ce["delta"],"ce_gamma":ce["gamma"],
            "ce_theta":ce["theta"],"ce_vega":ce["vega"],
            "ce_sl":round(ce["price"]*0.5,2),
            "ce_t1":round(ce["price"]*1.30,2),"ce_t2":round(ce["price"]*1.60,2),
            "ce_t3":round(ce["price"]*2.00,2),"ce_signal":ce_sig,
            "pe_price":pe["price"],"pe_delta":pe["delta"],"pe_gamma":pe["gamma"],
            "pe_theta":pe["theta"],"pe_vega":pe["vega"],
            "pe_sl":round(pe["price"]*0.5,2),
            "pe_t1":round(pe["price"]*1.30,2),"pe_t2":round(pe["price"]*1.60,2),
            "pe_t3":round(pe["price"]*2.00,2),"pe_signal":pe_sig,
        })
    return chain

def _option_signal(spot,K,atm,ind_u,df_u,otype,delta,dte,vix):
    score=0; reasons=[]
    # Underlying trend
    if ind_u:
        rsi=ind_u.get("rsi",50); m5=ind_u.get("m5",0)
        e13=ind_u.get("e13",0); e21=ind_u.get("e21",0); close=ind_u.get("close",0)
        bull = close>e13>e21 if (close and e13 and e21) else False
        bear = close<e13<e21 if (close and e13 and e21) else False
        if otype=="CE":
            if bull: score+=3; reasons.append("Underlying bullish EMA stack → +3")
            if bear: score-=2; reasons.append("Underlying bearish → -2")
            if rsi<40: score+=1; reasons.append(f"RSI {rsi:.0f} oversold, bounce likely → +1")
            if m5>1.5: score+=2; reasons.append(f"5D momentum +{m5:.1f}% → +2")
        else:
            if bear: score+=3; reasons.append("Underlying bearish EMA stack → +3")
            if bull: score-=2; reasons.append("Underlying bullish → -2")
            if rsi>60: score+=1; reasons.append(f"RSI {rsi:.0f} elevated, fall likely → +1")
            if m5<-1.5: score+=2; reasons.append(f"5D momentum {m5:.1f}% → +2")
    # Delta sweet spot
    ad = abs(delta)
    if 0.35<=ad<=0.65: score+=2; reasons.append(f"|Δ|={ad:.2f} optimal → +2")
    elif 0.20<=ad<0.35: score+=1; reasons.append(f"|Δ|={ad:.2f} tradeable OTM → +1")
    elif ad<0.15: score-=2; reasons.append(f"|Δ|={ad:.2f} too far OTM → -2")
    # DTE
    if dte<=2: score-=3; reasons.append("⚠️ ≤2 DTE — theta burn extreme → -3")
    elif dte<=5: score-=1; reasons.append(f"{dte}D to expiry — theta elevated → -1")
    else: score+=1; reasons.append(f"{dte}D expiry — time value adequate → +1")
    # VIX
    if vix>20: score+=1; reasons.append(f"VIX {vix:.1f} high — IV elevated, use momentum plays → +1")
    elif vix<13: score+=1; reasons.append(f"VIX {vix:.1f} low — cheap options, buy → +1")
    # Strike position
    pct = (K-spot)/spot*100 if otype=="CE" else (spot-K)/spot*100
    if 0<=pct<=0.5: score+=2; reasons.append("Near-ATM best liquidity → +2")
    elif 0.5<pct<=1.5: score+=1; reasons.append("Slightly OTM good R/R → +1")
    elif pct>3: score-=2; reasons.append("Far OTM — low prob → -2")
    # Final
    if score>=7:   sig="STRONG BUY"; str_=min(95,60+score*3)
    elif score>=4: sig="BUY";        str_=min(80,50+score*5)
    elif score<=-3: sig="AVOID";     str_=max(10,50+score*5)
    else:           sig="NEUTRAL";   str_=45
    return {"signal":sig,"score":score,"strength":str_,"reasons":reasons}

# ─── Parallel Scanner ─────────────────────────────────────────────────────────
def scan_parallel(symbols, mode="INTRADAY", market_mood="NEUTRAL", vix=15.0,
                  max_workers=40, min_strength=55):
    results = []
    def _scan_one(sym):
        try:
            period = "1mo" if mode=="INTRADAY" else "6mo"
            interval = "1d"
            df   = get_ohlcv(sym, period, interval)
            ind  = compute_indicators(df)
            fund = {}
            if not ind: return None
            rec, strength, bs, ss, reasons = score_signal(
                ind, fund, df, market_mood, vix, mode
            )
            if rec == "NEUTRAL" and strength < min_strength: return None
            price = ind.get("close",0)
            atr   = ind.get("atr",price*0.02)
            if rec in ("BUY","STRONG BUY","WEAK BUY"):
                target = round(price*(1+0.015*(bs/5)),2)
                sl     = round(price-1.5*atr, 2)
            elif rec in ("SELL","STRONG SELL","WEAK SELL"):
                target = round(price*(1-0.015*(ss/5)),2)
                sl     = round(price+1.5*atr, 2)
            else:
                target = price; sl = price
            rr = abs(target-price)/abs(price-sl) if abs(price-sl)>0 else 1.5
            patterns = detect_patterns(df)
            div = detect_divergence(df, ind)
            return {
                "symbol":sym,"rec":rec,"strength":strength,
                "buy_score":bs,"sell_score":ss,
                "price":price,"target":target,"sl":sl,"rr":rr,
                "atr":atr,"day_chg":ind.get("day_chg",0),
                "m5":ind.get("m5",0),"m20":ind.get("m20",0),
                "vr":ind.get("vr",1),"adx":ind.get("adx",0),
                "rsi":ind.get("rsi",50),"macd":ind.get("macd",0),
                "indicators":ind,"reasons":reasons,
                "patterns":[(p[0],p[1]) for p in patterns],
                "divergence":div,
                "s1":ind.get("s1",0),"r1":ind.get("r1",0),
            }
        except Exception:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        for r in ex.map(_scan_one, symbols):
            if r and r["strength"] >= min_strength:
                results.append(r)
    results.sort(key=lambda x: (0 if "BUY" in x["rec"] else 1, -x["strength"]))
    return results
