import streamlit as st


st.set_page_config(
    page_title="Januario & Collen | Amizade fofa",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
      :root { --berry:#8b3155; --rose:#e95f7f; --pink:#fff0f3; --ink:#51263a; }
      .stApp {
        background:
          radial-gradient(ellipse at 12% 8%, #ffe2e9 0, transparent 31%),
          radial-gradient(ellipse at 88% 25%, #ffe8d8 0, transparent 27%),
          linear-gradient(160deg, #fff9f7 0%, #fff1f4 52%, #fffaf8 100%);
        color:var(--ink); font-family:'DM Sans',sans-serif;
      }
      [data-testid="stHeader"] { background:transparent; }
      .block-container { max-width:820px; padding:3.2rem 1.2rem 2.5rem; }
      .topline { display:flex; align-items:center; justify-content:center; gap:.55rem; color:#b4516b;
        text-transform:uppercase; letter-spacing:.2em; font-size:.72rem; font-weight:800; }
      .topline span { width:25px; height:1px; background:#e8a7b5; }
      .title { text-align:center; color:#642c45; font:800 clamp(2.3rem,7vw,4.25rem)/1.04 'Playfair Display',Georgia,serif;
        margin:.9rem auto .8rem; max-width:700px; letter-spacing:-.035em; }
      .intro { text-align:center; margin:0 auto 1.6rem; max-width:540px; color:#86566a;
        font-size:1.08rem; line-height:1.75; }
      .hero-card { position:relative; overflow:hidden; max-width:610px; margin:1.4rem auto 1.1rem;
        padding:1.3rem 1rem 1.15rem; border:1px solid #f8d4de; border-radius:30px;
        background:linear-gradient(145deg,#ffffffd9,#fff7f8e8); box-shadow:0 22px 65px #a23c5c17; }
      .hero-card:before,.hero-card:after { content:'✦'; position:absolute; color:#f1b8c5; font-size:1.2rem; }
      .hero-card:before { top:24px; left:27px; } .hero-card:after { right:29px; bottom:28px; }
      .heart-wrap { display:flex; justify-content:center; }
      .heart-svg { width:min(100%,430px); height:auto; overflow:visible; filter:drop-shadow(0 16px 22px #bf36502b); animation:heartbeat 2.8s ease-in-out infinite; }
      .heart-title { font:800 23px 'DM Sans',sans-serif; fill:white; text-anchor:middle; }
      .heart-sub { font:700 11px 'DM Sans',sans-serif; fill:#ffe5eb; text-anchor:middle; letter-spacing:3px; }
      @keyframes heartbeat { 0%,100%{transform:scale(1)} 7%{transform:scale(1.025)} 14%{transform:scale(1)} 21%{transform:scale(1.018)} 30%{transform:scale(1)} }
      .message { text-align:center; color:#75455b; font-size:1.02rem; line-height:1.75; margin:.5rem auto 1.2rem; max-width:520px; }
      .message strong { color:#bd4565; }
      .tag-row { display:flex; flex-wrap:wrap; justify-content:center; gap:.55rem; margin:1rem auto 1.35rem; }
      .tag { border:1px solid #f4cbd5; border-radius:999px; padding:.5rem .85rem; background:#fff9fa;
        color:#a04966; font-size:.83rem; font-weight:700; }
      div.stButton { display:flex; justify-content:center; }
      div.stButton > button { border:0; border-radius:999px; padding:.78rem 1.5rem; min-height:3rem;
        color:white; font-weight:800; letter-spacing:.01em; background:linear-gradient(115deg,#ef7890,#d94d71);
        box-shadow:0 10px 24px #db587444; transition:transform .18s ease, box-shadow .18s ease; }
      div.stButton > button:hover { color:white; transform:translateY(-2px); box-shadow:0 14px 28px #db587455; }
      div.stButton > button:focus { color:white; border:2px solid #a9385b; }
      .footer { text-align:center; color:#b17b8c; font-size:.78rem; margin-top:1.8rem; }
      @media(max-width:600px) { .block-container{padding-top:2.3rem}.hero-card{border-radius:23px;padding:.9rem .5rem}.heart-title{font-size:20px}.intro{font-size:1rem} }
      @media(prefers-reduced-motion:reduce) { .heart-svg{animation:none} *{scroll-behavior:auto!important} }
    </style>
    <div class="topline"><span></span>Uma amizade muito especial<span></span></div>
    <h1 class="title">Collen e Januario,<br>amiguinhos fofos</h1>
    <p class="intro">Tem gente que deixa qualquer dia mais bonito só por estar por perto. ✨</p>
    <section class="hero-card">
      <div class="heart-wrap">
        <svg class="heart-svg" viewBox="0 0 500 430" role="img" aria-label="Um coração rosa com Januario e Collen">
          <defs>
            <linearGradient id="heartGradient" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#ff91a5"/><stop offset="52%" stop-color="#ed5c7b"/><stop offset="100%" stop-color="#c93260"/>
            </linearGradient>
            <radialGradient id="heartShine" cx="30%" cy="18%" r="80%">
              <stop offset="0%" stop-color="#ffffff" stop-opacity=".28"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <path fill="url(#heartGradient)" d="M250 402 57 218C-20 140 33 26 131 26c54 0 94 32 119 75 25-43 65-75 119-75 98 0 151 114 74 192L250 402Z"/>
          <path fill="url(#heartShine)" d="M250 402 57 218C-20 140 33 26 131 26c54 0 94 32 119 75 25-43 65-75 119-75 98 0 151 114 74 192L250 402Z"/>
          <text class="heart-sub" x="250" y="178">AMIZADE PRA SEMPRE</text>
          <text class="heart-title" x="250" y="222">Januario</text>
          <text class="heart-title" x="250" y="261">×</text>
          <text class="heart-title" x="250" y="300">Collen</text>
        </svg>
      </div>
    </section>
    <p class="message">Eu gosto <strong>muitão de você, Collen</strong>, minha amiguinha fofa!<br>
      Você é muito legal, querida e merece um montão de carinho. 💌</p>
    <div class="tag-row">
      <span class="tag">🌷 amizade</span><span class="tag">🍓 fofura</span><span class="tag">💖 carinho</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Mandar um abraço virtual 💌", use_container_width=False):
    st.balloons()
    st.success("Abraço enviado para a Collen! 💖")

st.markdown(
    '<div class="footer">Feito com muito amor e carinho pelo Januario ❤️</div>',
    unsafe_allow_html=True,
)
