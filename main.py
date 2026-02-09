import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Optimizar - IA para tu empresa", page_icon="🔄", layout="wide", initial_sidebar_state="collapsed")

GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQMUYj1IYNlmhIzFoMsDXXB4uTXyWGOaJFhyVaEvw1QoYMjLkxr9ehkp10iIm-hOhvcm_ppSM9ORPHX/pub?gid=0&single=true&output=csv"

LOGO_SVG = '''<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20,90 L20,50 Q20,42 28,42 L72,42 Q80,42 80,50 L80,90 Q80,96 74,96 L26,96 Q20,96 20,90 Z" stroke="white" stroke-width="5" fill="none" stroke-linejoin="round"/><line x1="38" y1="42" x2="38" y2="22" stroke="white" stroke-width="5" stroke-linecap="round"/><circle cx="38" cy="18" r="5" fill="white"/><line x1="55" y1="42" x2="55" y2="14" stroke="white" stroke-width="5" stroke-linecap="round"/><circle cx="55" cy="10" r="5" fill="white"/><line x1="72" y1="42" x2="72" y2="8" stroke="white" stroke-width="5" stroke-linecap="round"/><polyline points="64,16 72,6 80,16" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="38" cy="68" r="4.5" fill="white"/><circle cx="62" cy="68" r="4.5" fill="white"/><line x1="38" y1="68" x2="62" y2="68" stroke="white" stroke-width="3" stroke-linecap="round"/></svg>'''

URL_AGENTE_EXTERNO = "https://t.me/sonner_ext2_bot"
URL_AGENTE_INTERNO = "https://t.me/sonner_INT_BOT"
URL_CRM_CLIENTES   = "https://app.mazefunnels.com/v2/location/Eux2vH92r7lqysmb2put/opportunities/list"
URL_DASHBOARD      = "https://app.mazefunnels.com/v2/location/Eux2vH92r7lqysmb2put/dashboard"
URL_SOPORTE        = "https://wa.link/3vq49h"

# CSS
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
#MainMenu,footer,header,.stDeployButton,[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"]{display:none!important;visibility:hidden!important;}
.block-container{padding-top:0!important;padding-bottom:0!important;max-width:100%!important;}
.stApp{background:linear-gradient(125deg,#c044e0 0%,#a855f7 20%,#7c3aed 40%,#6366f1 60%,#4f86f7 80%,#38bdf8 100%);font-family:'Poppins',sans-serif;overflow-x:hidden;min-height:100vh;}
.main .block-container{padding:0!important;max-width:100%!important;}
.geo-background{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;}
.particles{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:1;pointer-events:none;}
.particle{position:absolute;border-radius:50%;background:rgba(255,255,255,.5);animation:pFloat 15s infinite ease-in-out;}
.particle:nth-child(1){width:4px;height:4px;top:12%;left:8%;animation-delay:0s;animation-duration:18s;}
.particle:nth-child(2){width:3px;height:3px;top:25%;left:22%;animation-delay:2s;animation-duration:14s;}
.particle:nth-child(3){width:5px;height:5px;top:45%;left:12%;animation-delay:4s;animation-duration:20s;}
.particle:nth-child(4){width:3px;height:3px;top:65%;left:5%;animation-delay:1s;animation-duration:16s;}
.particle:nth-child(5){width:4px;height:4px;top:18%;right:15%;animation-delay:3s;animation-duration:19s;}
.particle:nth-child(6){width:6px;height:6px;top:55%;right:8%;animation-delay:5s;animation-duration:17s;}
.particle:nth-child(7){width:3px;height:3px;top:78%;right:20%;animation-delay:2.5s;animation-duration:15s;}
.particle:nth-child(8){width:4px;height:4px;top:8%;left:45%;animation-delay:4.5s;animation-duration:21s;}
.corner-circle{position:absolute;border-radius:50%;border:1.5px solid rgba(255,255,255,.35);background:transparent;}
.corner-circle.bl{width:14px;height:14px;bottom:25px;left:25px;}
.corner-circle.rm{width:14px;height:14px;top:78%;right:35px;}
@keyframes pFloat{0%,100%{transform:translate(0,0);opacity:.4;}25%{transform:translate(8px,-15px);opacity:.7;}50%{transform:translate(-5px,-25px);opacity:.5;}75%{transform:translate(12px,-10px);opacity:.8;}}
.nav-header{position:relative;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:22px 50px;}
.logo-area{display:flex;align-items:center;gap:14px;}.logo-area svg{width:38px;height:38px;}
.logo-text{font-size:22px;font-weight:700;color:white;letter-spacing:1px;}
.nav-menu{display:flex;gap:20px;align-items:center;}
.nav-link{color:white;text-decoration:none;font-size:15px;font-weight:500;cursor:pointer;transition:all .3s;padding:10px 24px;border-radius:6px;border:1.5px solid rgba(255,255,255,.3);background:rgba(255,255,255,.06);backdrop-filter:blur(8px);display:inline-flex;align-items:center;gap:8px;}
.nav-link:hover{background:rgba(255,255,255,.18);border-color:rgba(255,255,255,.5);transform:translateY(-2px);}
.center-buttons{position:relative;z-index:10;display:flex;flex-wrap:wrap;justify-content:center;gap:30px;padding:70px 40px 50px;}
.center-btn{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.25);border-radius:16px;padding:45px 40px;min-width:250px;text-align:center;backdrop-filter:blur(12px);cursor:pointer;transition:all .35s ease;text-decoration:none;display:block;}
.center-btn:hover{background:rgba(255,255,255,.18);transform:translateY(-8px);box-shadow:0 15px 40px rgba(0,0,0,.18);border-color:rgba(255,255,255,.45);}
.center-btn-icon{font-size:38px;margin-bottom:16px;}.center-btn-label{font-size:19px;font-weight:600;color:white;}
.center-btn-sub{font-size:13px;font-weight:300;color:rgba(255,255,255,.7);margin-top:8px;}
.stats-row{position:relative;z-index:10;display:flex;justify-content:center;gap:20px;max-width:1100px;margin:0 auto 25px;padding:0 40px;flex-wrap:wrap;}
.stat-card{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.18);border-radius:14px;padding:22px 28px;backdrop-filter:blur(12px);flex:1;min-width:200px;max-width:320px;text-align:center;}
.stat-value{font-size:36px;font-weight:800;line-height:1;}.stat-label{font-size:12px;font-weight:400;color:rgba(255,255,255,.65);margin-top:6px;text-transform:uppercase;letter-spacing:.5px;}
.stat-pink .stat-value{color:#f472b6;}.stat-purple .stat-value{color:#a78bfa;}.stat-blue .stat-value{color:#38bdf8;}
.chart-section{position:relative;z-index:10;max-width:1100px;margin:0 auto 60px;padding:0 40px;}
.chart-container{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18);border-radius:18px;padding:30px;backdrop-filter:blur(14px);}
.chart-title{font-size:22px;font-weight:600;color:white;margin-bottom:4px;}
.chart-subtitle{font-size:13px;font-weight:300;color:rgba(255,255,255,.6);margin-bottom:15px;}
.live-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(52,211,153,.15);border:1px solid rgba(52,211,153,.3);border-radius:20px;padding:4px 14px;font-size:11px;color:#6ee7b7;font-weight:500;margin-left:10px;}
.live-dot{width:7px;height:7px;border-radius:50%;background:#34d399;animation:livePulse 1.5s infinite;}
@keyframes livePulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}
.stTabs [data-baseweb="tab-list"]{gap:8px;background:transparent;}
.stTabs [data-baseweb="tab"]{background:rgba(255,255,255,.08)!important;border-radius:8px!important;color:white!important;border:1px solid rgba(255,255,255,.15)!important;font-family:'Poppins',sans-serif!important;padding:8px 20px!important;}
.stTabs [aria-selected="true"]{background:rgba(255,255,255,.2)!important;border-color:rgba(255,255,255,.4)!important;}
.stTabs [data-baseweb="tab-panel"]{background:transparent!important;padding-top:15px!important;}
.stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"]{display:none;}
.stDateInput>div>div>input{background:rgba(255,255,255,.08)!important;color:white!important;border-color:rgba(255,255,255,.2)!important;border-radius:8px!important;}
.stMultiSelect>div{background:rgba(255,255,255,.08)!important;border-color:rgba(255,255,255,.2)!important;border-radius:8px!important;color:white!important;}
.stRadio>div{flex-direction:row!important;gap:12px!important;}
.stRadio label{color:white!important;}
@media(max-width:768px){.nav-header{padding:15px 20px;flex-direction:column;gap:15px;}.center-buttons{padding:40px 20px 30px;gap:18px;flex-direction:column;align-items:center;}.center-btn{min-width:200px;padding:32px 28px;}.chart-section,.stats-row{padding:0 20px;}}
</style>""", unsafe_allow_html=True)

# Fondo + Partículas
st.markdown("""<div class="geo-background"><svg viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
<polygon points="0,400 300,100 650,350 400,600" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
<polygon points="200,200 500,50 700,250 550,450 250,400" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.06)" stroke-width=".8"/>
<polygon points="600,150 900,50 1050,300 800,400" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.09)" stroke-width="1"/>
<polygon points="300,300 700,200 950,450 750,650 400,550" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)" stroke-width="1.2"/>
<polygon points="700,250 1050,180 1250,400 1000,550 750,400" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.11)" stroke-width="1"/>
<polygon points="0,600 250,450 500,600 350,800 50,750" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
<polygon points="600,500 900,400 1100,600 900,750 650,650" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
<circle cx="300" cy="300" r="2.5" fill="rgba(255,255,255,0.25)"/><circle cx="700" cy="200" r="2" fill="rgba(255,255,255,0.2)"/>
<circle cx="1050" cy="180" r="2.5" fill="rgba(255,255,255,0.22)"/><circle cx="950" cy="450" r="3" fill="rgba(255,255,255,0.15)"/>
</svg></div>
<div class="particles"><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="corner-circle bl"></div><div class="corner-circle rm"></div></div>""", unsafe_allow_html=True)

# Header
st.markdown(f"""<div class="nav-header"><div class="logo-area">{LOGO_SVG}<span class="logo-text">optimizar</span></div>
<div class="nav-menu"><a class="nav-link" href="#" onclick="window.open('{URL_DASHBOARD}','D','width=1300,height=850,scrollbars=yes,resizable=yes');return false;">📊 Dashboard</a>
<a class="nav-link" href="#" onclick="window.open('{URL_SOPORTE}','S','width=1000,height=700,scrollbars=yes,resizable=yes');return false;">💬 Soporte</a></div></div>""", unsafe_allow_html=True)

# 3 Botones
st.markdown(f"""<div class="center-buttons">
<a class="center-btn" href="#" onclick="window.open('{URL_AGENTE_EXTERNO}','AE','width=1200,height=800,scrollbars=yes,resizable=yes');return false;"><div class="center-btn-icon">🌐</div><div class="center-btn-label">Agente Externo</div><div class="center-btn-sub">Atención al cliente automatizada</div></a>
<a class="center-btn" href="#" onclick="window.open('{URL_AGENTE_INTERNO}','AI','width=1200,height=800,scrollbars=yes,resizable=yes');return false;"><div class="center-btn-icon">🏢</div><div class="center-btn-label">Agente Interno</div><div class="center-btn-sub">Asistente para tu equipo</div></a>
<a class="center-btn" href="#" onclick="window.open('{URL_CRM_CLIENTES}','CRM','width=1200,height=800,scrollbars=yes,resizable=yes');return false;"><div class="center-btn-icon">👥</div><div class="center-btn-label">CRM de Clientes</div><div class="center-btn-sub">Gestión y seguimiento</div></a>
</div>""", unsafe_allow_html=True)

# ============================================
# CARGAR DATOS
# ============================================
@st.cache_data(ttl=300)
def cargar_datos():
    try:
        df = pd.read_csv(GOOGLE_SHEET_CSV_URL)
        df.columns = df.columns.str.strip()
        return df, True
    except:
        return pd.DataFrame({"Fecha":["07/02/2026"],"Consultas":[15],"Prespuestos Enviados":[5],"Contratos Enviados":[1]}), False

df, desde_sheets = cargar_datos()

def find_col(df, keywords):
    for c in df.columns:
        cl = c.lower()
        if any(k in cl for k in keywords):
            return c
    return None

col_fecha = find_col(df, ['fecha']) or df.columns[0]
col_c = find_col(df, ['consult']) or 'Consultas'
col_p = find_col(df, ['presupuest','prespuest']) or 'Prespuestos Enviados'
col_t = find_col(df, ['contrat']) or 'Contratos Enviados'

for col in [col_c, col_p, col_t]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Parsear fechas
if col_fecha in df.columns:
    df['_fecha_parsed'] = pd.to_datetime(df[col_fecha], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['_fecha_parsed']).sort_values('_fecha_parsed')

# ============================================
# FILTROS (Streamlit widgets)
# ============================================
st.markdown("""<div class="chart-section"><div class="chart-container">
<div class="chart-title">📈 Métricas del Negocio <span class="live-badge"><span class="live-dot"></span>En vivo</span></div>
<div class="chart-subtitle">Datos desde Google Sheets · Filtros interactivos</div></div></div>""", unsafe_allow_html=True)

col_l, col_filters, col_r = st.columns([1, 8, 1])
with col_filters:
    # Fila 1: Período rápido
    periodo = st.radio(
        "⏱ Período rápido",
        ["Todo", "Hoy", "7 días", "15 días", "30 días", "90 días", "Este mes", "Mes anterior", "Este año"],
        horizontal=True,
        index=0
    )

    # Fila 2: Rango personalizado
    col_from, col_to = st.columns(2)
    with col_from:
        fecha_desde = st.date_input("📅 Desde", value=None, format="DD/MM/YYYY")
    with col_to:
        fecha_hasta = st.date_input("📅 Hasta", value=None, format="DD/MM/YYYY")

    # Fila 3: Métricas
    metricas_nombres = {col_c: "Consultas", col_p: "Presupuestos Enviados", col_t: "Contratos Enviados"}
    metricas_disponibles = [c for c in [col_c, col_p, col_t] if c in df.columns]
    metricas_seleccionadas = st.multiselect(
        "📊 Métricas a mostrar",
        options=metricas_disponibles,
        default=metricas_disponibles,
        format_func=lambda x: metricas_nombres.get(x, x)
    )

# Aplicar filtro de período
filtered = df.copy()
if '_fecha_parsed' in filtered.columns:
    hoy = pd.Timestamp.now().normalize()
    
    if fecha_desde and fecha_hasta:
        filtered = filtered[(filtered['_fecha_parsed'] >= pd.Timestamp(fecha_desde)) & (filtered['_fecha_parsed'] <= pd.Timestamp(fecha_hasta))]
    elif periodo != "Todo":
        if periodo == "Hoy":
            filtered = filtered[filtered['_fecha_parsed'] == hoy]
        elif periodo == "7 días":
            filtered = filtered[filtered['_fecha_parsed'] >= hoy - timedelta(days=6)]
        elif periodo == "15 días":
            filtered = filtered[filtered['_fecha_parsed'] >= hoy - timedelta(days=14)]
        elif periodo == "30 días":
            filtered = filtered[filtered['_fecha_parsed'] >= hoy - timedelta(days=29)]
        elif periodo == "90 días":
            filtered = filtered[filtered['_fecha_parsed'] >= hoy - timedelta(days=89)]
        elif periodo == "Este mes":
            filtered = filtered[(filtered['_fecha_parsed'].dt.month == hoy.month) & (filtered['_fecha_parsed'].dt.year == hoy.year)]
        elif periodo == "Mes anterior":
            mes_ant = hoy.replace(day=1) - timedelta(days=1)
            filtered = filtered[(filtered['_fecha_parsed'].dt.month == mes_ant.month) & (filtered['_fecha_parsed'].dt.year == mes_ant.year)]
        elif periodo == "Este año":
            filtered = filtered[filtered['_fecha_parsed'].dt.year == hoy.year]

# Tarjetas con datos filtrados
total_c = int(filtered[col_c].sum()) if col_c in filtered.columns else 0
total_p = int(filtered[col_p].sum()) if col_p in filtered.columns else 0
total_t = int(filtered[col_t].sum()) if col_t in filtered.columns else 0

st.markdown(f"""<div class="stats-row">
<div class="stat-card stat-pink"><div class="stat-value">{total_c}</div><div class="stat-label">Consultas</div></div>
<div class="stat-card stat-purple"><div class="stat-value">{total_p}</div><div class="stat-label">Presupuestos Enviados</div></div>
<div class="stat-card stat-blue"><div class="stat-value">{total_t}</div><div class="stat-label">Contratos Enviados</div></div>
</div>""", unsafe_allow_html=True)

# Gráfico
col_l2, col_chart, col_r2 = st.columns([1, 8, 1])
with col_chart:
    if metricas_seleccionadas and len(filtered) > 0:
        if '_fecha_parsed' in filtered.columns:
            chart_df = filtered.set_index(filtered['_fecha_parsed'].dt.strftime('%d/%m'))[metricas_seleccionadas]
        else:
            chart_df = filtered[metricas_seleccionadas]
        
        chart_df.columns = [metricas_nombres.get(c, c) for c in chart_df.columns]
        
        tab1, tab2, tab3 = st.tabs(["📈 Líneas", "📊 Barras", "📋 Tabla"])
        with tab1:
            st.line_chart(chart_df, use_container_width=True)
        with tab2:
            st.bar_chart(chart_df, use_container_width=True)
        with tab3:
            display_df = filtered[[col_fecha] + metricas_seleccionadas].copy()
            display_df.columns = ["Fecha"] + [metricas_nombres.get(c, c) for c in metricas_seleccionadas]
            st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.info("Seleccioná al menos una métrica para ver el gráfico")

st.markdown("<br><br>", unsafe_allow_html=True)
