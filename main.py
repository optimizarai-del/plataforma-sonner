import streamlit as st

st.set_page_config(
    page_title="Optimizar - IA para tu empresa",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    [data-testid="stStatusWidget"] {display: none;}
    .block-container {padding-top: 0 !important; padding-bottom: 0 !important; max-width: 100% !important;}
    
    .stApp {
        background: linear-gradient(125deg, #c044e0 0%, #a855f7 20%, #7c3aed 40%, #6366f1 60%, #4f86f7 80%, #38bdf8 100%);
        font-family: 'Poppins', sans-serif;
        overflow-x: hidden;
        min-height: 100vh;
    }
    .main .block-container { padding: 0 !important; max-width: 100% !important; }
    
    .geo-background { position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:0; pointer-events:none; }
    
    .particles { position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:1; pointer-events:none; }
    .particle { position:absolute; border-radius:50%; background:rgba(255,255,255,.5); animation:pFloat 15s infinite ease-in-out; }
    .particle:nth-child(1)  { width:4px; height:4px; top:12%; left:8%;   animation-delay:0s;   animation-duration:18s; }
    .particle:nth-child(2)  { width:3px; height:3px; top:25%; left:22%;  animation-delay:2s;   animation-duration:14s; }
    .particle:nth-child(3)  { width:5px; height:5px; top:45%; left:12%;  animation-delay:4s;   animation-duration:20s; }
    .particle:nth-child(4)  { width:3px; height:3px; top:65%; left:5%;   animation-delay:1s;   animation-duration:16s; }
    .particle:nth-child(5)  { width:4px; height:4px; top:18%; right:15%; animation-delay:3s;   animation-duration:19s; }
    .particle:nth-child(6)  { width:6px; height:6px; top:55%; right:8%;  animation-delay:5s;   animation-duration:17s; }
    .particle:nth-child(7)  { width:3px; height:3px; top:78%; right:20%; animation-delay:2.5s; animation-duration:15s; }
    .particle:nth-child(8)  { width:4px; height:4px; top:8%;  left:45%;  animation-delay:4.5s; animation-duration:21s; }
    .particle:nth-child(9)  { width:5px; height:5px; top:35%; right:30%; animation-delay:1.5s; animation-duration:13s; }
    .particle:nth-child(10) { width:3px; height:3px; top:85%; left:35%;  animation-delay:3.5s; animation-duration:18s; }
    .particle:nth-child(11) { width:4px; height:4px; top:50%; left:60%;  animation-delay:.5s;  animation-duration:16s; }
    .particle:nth-child(12) { width:3px; height:3px; top:70%; left:75%;  animation-delay:6s;   animation-duration:22s; }
    .corner-circle { position:absolute; border-radius:50%; border:1.5px solid rgba(255,255,255,.35); background:transparent; }
    .corner-circle.bl { width:14px; height:14px; bottom:25px; left:25px; }
    .corner-circle.rm { width:14px; height:14px; top:78%; right:35px; }
    @keyframes pFloat {
        0%,100% { transform:translate(0,0); opacity:.4; }
        25%     { transform:translate(8px,-15px); opacity:.7; }
        50%     { transform:translate(-5px,-25px); opacity:.5; }
        75%     { transform:translate(12px,-10px); opacity:.8; }
    }

    .nav-header { position:relative; z-index:100; display:flex; justify-content:space-between; align-items:center; padding:22px 50px; }
    .logo-area { display:flex; align-items:center; gap:12px; }
    .logo-area svg { width:40px; height:44px; }
    .logo-text { font-size:22px; font-weight:700; color:white; letter-spacing:1px; }
    .nav-menu { display:flex; gap:32px; align-items:center; }
    .nav-item { color:white; text-decoration:underline; text-underline-offset:4px; font-size:15px; font-weight:400; cursor:pointer; transition:all .3s; }
    .nav-item:hover { font-weight:500; text-decoration-thickness:2px; }
    .nav-btn { background:transparent; color:white; padding:10px 22px; border-radius:4px; font-weight:500; font-size:14px; border:1.5px solid white; cursor:pointer; transition:all .3s; font-family:'Poppins',sans-serif; }
    .nav-btn:hover { background:rgba(255,255,255,.15); }

    .center-buttons {
        position: relative;
        z-index: 10;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 30px;
        margin-top: 28vh;
        padding: 0 40px;
    }
    .center-btn {
        background: rgba(255,255,255,.08);
        border: 1.5px solid rgba(255,255,255,.25);
        border-radius: 16px;
        padding: 45px 40px;
        min-width: 250px;
        text-align: center;
        backdrop-filter: blur(12px);
        cursor: pointer;
        transition: all .35s ease;
        text-decoration: none;
        display: block;
    }
    .center-btn:hover {
        background: rgba(255,255,255,.18);
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(0,0,0,.18);
        border-color: rgba(255,255,255,.45);
    }
    .center-btn:active {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,.12);
    }
    .center-btn-icon { font-size: 38px; margin-bottom: 16px; }
    .center-btn-label { font-size: 19px; font-weight: 600; color: white; font-family:'Poppins',sans-serif; }
    .center-btn-sub { font-size: 13px; font-weight: 300; color: rgba(255,255,255,.7); margin-top: 8px; font-family:'Poppins',sans-serif; }

    @media (max-width:768px) {
        .nav-header { padding:15px 20px; flex-direction:column; gap:15px; }
        .nav-menu { flex-wrap:wrap; justify-content:center; gap:15px; }
        .center-buttons { margin-top:15vh; gap:18px; flex-direction:column; align-items:center; }
        .center-btn { min-width:200px; padding:32px 28px; }
    }
    </style>
""", unsafe_allow_html=True)

# Fondo geométrico
st.markdown("""
    <div class="geo-background">
        <svg viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
            <polygon points="0,400 300,100 650,350 400,600" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <polygon points="200,200 500,50 700,250 550,450 250,400" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.06)" stroke-width=".8"/>
            <polygon points="600,150 900,50 1050,300 800,400" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.09)" stroke-width="1"/>
            <polygon points="850,100 1150,0 1300,250 1100,350 900,200" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="1100,150 1400,50 1550,300 1350,400" fill="rgba(255,255,255,0.035)" stroke="rgba(255,255,255,0.065)" stroke-width="1"/>
            <polygon points="1400,100 1700,0 1920,200 1750,350 1500,250" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="300,300 700,200 950,450 750,650 400,550" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)" stroke-width="1.2"/>
            <polygon points="700,250 1050,180 1250,400 1000,550 750,400" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.11)" stroke-width="1"/>
            <polygon points="1000,200 1350,150 1500,380 1300,520 1050,400" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.09)" stroke-width="1"/>
            <polygon points="1250,300 1600,200 1750,450 1550,580 1300,480" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width=".8"/>
            <polygon points="0,600 250,450 500,600 350,800 50,750" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="300,550 600,400 800,600 650,800 350,700" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <polygon points="600,500 900,400 1100,600 900,750 650,650" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
            <polygon points="900,500 1200,400 1400,600 1200,780 950,650" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.08)" stroke-width=".8"/>
            <polygon points="1200,550 1500,400 1700,600 1550,800 1250,700" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.09)" stroke-width="1"/>
            <polygon points="1500,500 1800,400 1920,600 1920,800 1600,750" fill="rgba(255,255,255,0.035)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="0,750 200,650 400,800 300,950 50,900" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.06)" stroke-width=".7"/>
            <polygon points="400,700 700,600 850,800 700,1000 450,850" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="800,700 1100,600 1300,800 1100,1000 850,850" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.06)" stroke-width=".7"/>
            <polygon points="1200,700 1500,600 1700,800 1500,1000 1250,850" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.07)" stroke-width=".8"/>
            <polygon points="1600,700 1920,600 1920,1000 1700,950 1650,800" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.06)" stroke-width=".7"/>
            <line x1="300" y1="300" x2="700" y2="200" stroke="rgba(255,255,255,0.06)" stroke-width=".5"/>
            <line x1="700" y1="200" x2="1050" y2="180" stroke="rgba(255,255,255,0.05)" stroke-width=".5"/>
            <line x1="1050" y1="180" x2="1350" y2="150" stroke="rgba(255,255,255,0.04)" stroke-width=".5"/>
            <circle cx="300" cy="300" r="2.5" fill="rgba(255,255,255,0.25)"/>
            <circle cx="700" cy="200" r="2" fill="rgba(255,255,255,0.2)"/>
            <circle cx="1050" cy="180" r="2.5" fill="rgba(255,255,255,0.22)"/>
            <circle cx="1350" cy="150" r="2" fill="rgba(255,255,255,0.18)"/>
            <circle cx="950" cy="450" r="3" fill="rgba(255,255,255,0.15)"/>
        </svg>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="particles">
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="corner-circle bl"></div>
        <div class="corner-circle rm"></div>
    </div>
""", unsafe_allow_html=True)

LOGO_SVG = '''<svg viewBox="0 0 120 130" fill="none" xmlns="http://www.w3.org/2000/svg">
    <line x1="60" y1="25" x2="60" y2="95" stroke="white" stroke-width="5" stroke-linecap="round"/>
    <line x1="60" y1="65" x2="30" y2="40" stroke="white" stroke-width="5" stroke-linecap="round"/>
    <line x1="60" y1="55" x2="90" y2="35" stroke="white" stroke-width="5" stroke-linecap="round"/>
    <line x1="60" y1="80" x2="88" y2="70" stroke="white" stroke-width="5" stroke-linecap="round"/>
    <circle cx="60" cy="18" r="10" stroke="white" stroke-width="5" fill="none"/>
    <circle cx="60" cy="8" r="5" fill="white"/>
    <circle cx="27" cy="36" r="7" fill="white"/>
    <circle cx="93" cy="32" r="7" fill="white"/>
    <circle cx="92" cy="70" r="7" fill="white"/>
    <circle cx="60" cy="98" r="7" fill="white"/>
    <rect x="45" y="108" width="30" height="10" rx="4" fill="white"/>
</svg>'''

# URLs reales
URL_AGENTE_EXTERNO = "https://t.me/sonner_ext2_bot"
URL_AGENTE_INTERNO = "https://t.me/sonner_INT_BOT"
URL_CRM_CLIENTES   = "https://app.mazefunnels.com/v2/location/Eux2vH92r7lqysmb2put/opportunities/list"

# Header
st.markdown(f"""
    <div class="nav-header">
        <div class="logo-area">
            {LOGO_SVG}
            <span class="logo-text">optimizar</span>
        </div>
        <div class="nav-menu">
            <span class="nav-item">Inicio</span>
            <span class="nav-item">Soluciones</span>
            <span class="nav-item">Áreas de aplicación</span>
            <span class="nav-item">Casos de éxito</span>
            <span class="nav-item">Contacto</span>
            <button class="nav-btn">Solicitar auditoría gratuita</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3 Botones centrales — ventana emergente (popup)
st.markdown(f"""
    <div class="center-buttons">
        <a class="center-btn" href="#" onclick="window.open('{URL_AGENTE_EXTERNO}', 'AgenteExterno', 'width=1200,height=800,scrollbars=yes,resizable=yes'); return false;">
            <div class="center-btn-icon">🌐</div>
            <div class="center-btn-label">Agente Externo</div>
            <div class="center-btn-sub">Atención al cliente automatizada</div>
        </a>
        <a class="center-btn" href="#" onclick="window.open('{URL_AGENTE_INTERNO}', 'AgenteInterno', 'width=1200,height=800,scrollbars=yes,resizable=yes'); return false;">
            <div class="center-btn-icon">🏢</div>
            <div class="center-btn-label">Agente Interno</div>
            <div class="center-btn-sub">Asistente para tu equipo</div>
        </a>
        <a class="center-btn" href="#" onclick="window.open('{URL_CRM_CLIENTES}', 'CRMClientes', 'width=1200,height=800,scrollbars=yes,resizable=yes'); return false;">
            <div class="center-btn-icon">👥</div>
            <div class="center-btn-label">CRM de Clientes</div>
            <div class="center-btn-sub">Gestión y seguimiento</div>
        </a>
    </div>
""", unsafe_allow_html=True)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Inicio'
