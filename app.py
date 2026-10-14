import streamlit as st

st.set_page_config(
    page_title="Januario & Collen",
    page_icon="❤️",
    layout="centered",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
      .stApp {
        background: radial-gradient(ellipse at 50% 20%, #fff2f4 0%, #fff9f7 48%, #fff 100%);
        color: #421d2c;
      }
      [data-testid="stHeader"] { background: transparent; }
      .block-container { max-width: 760px; padding-top: 4rem; padding-bottom: 3rem; }
      .eyebrow {
        text-align: center; text-transform: uppercase; letter-spacing: .22em;
        font: 700 .78rem 'DM Sans', sans-serif; color: #c04b69; margin-bottom: 1rem;
      }
      .headline {
        text-align: center; font: 800 clamp(2.2rem, 7vw, 4rem)/1.08 'Playfair Display', Georgia, serif;
        color: #572237; margin: 0 auto .75rem; max-width: 680px;
      }
      .subtitle {
        text-align: center; font: 400 1.12rem/1.65 'DM Sans', sans-serif;
        color: #805566; margin: 0 auto 2rem; max-width: 520px;
      }
      .heart-wrap { display: flex; justify-content: center; margin: 0 auto; }
      .heart-svg { width: min(100%, 480px); height: auto; overflow: visible; filter: drop-shadow(0 18px 28px #bd48602b); }
      .heart-label { font: 800 25px 'DM Sans', sans-serif; fill: white; text-anchor: middle; }
      .heart-small { font: 600 13px 'DM Sans', sans-serif; fill: #ffe6eb; text-anchor: middle; letter-spacing: 2px; }
      .note {
        margin: 1.5rem auto 0; max-width: 430px; text-align: center; padding: 1rem 1.2rem;
        border: 1px solid #f5d4dc; border-radius: 18px; background: #ffffffb8;
        font: 600 .98rem/1.6 'DM Sans', sans-serif; color: #875268;
      }
      .footer { text-align: center; color: #bd8b9a; font: 400 .8rem 'DM Sans', sans-serif; margin-top: 2.3rem; }
      @media (max-width: 600px) { .block-container { padding-top: 2.5rem; } .heart-label { font-size: 21px; } }
    </style>
    <div class="eyebrow">Uma amizade especial</div>
    <h1 class="headline">Collen e januario amiguinhos fofos</h1>
    <p class="subtitle">eu te gosto muitao collen amiguinha fofa <3 </p>
    <div class="heart-wrap">
      <svg class="heart-svg" viewBox="0 0 500 430" role="img" aria-label="Coração com os nomes Januario e Collen">
        <defs>
          <linearGradient id="heartGradient" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ff7b91"/><stop offset="100%" stop-color="#d92f61"/>
          </linearGradient>
        </defs>
        <path fill="url(#heartGradient)" d="M250 402 57 218C-20 140 33 26 131 26c54 0 94 32 119 75 25-43 65-75 119-75 98 0 151 114 74 192L250 402Z"/>
        <text class="heart-small" x="250" y="184">AMIZADE</text>
        <text class="heart-label" x="250" y="224">Januario</text>
        <text class="heart-label" x="250" y="264">X</text>
        <text class="heart-label" x="250" y="304">Collen</text>
      </svg>
    </div>
    <div class="note">💖 Januario cuti cuti X Collen cuti cuti 💖<br/>voce e muito legal e fofinha collen bjs </div>
    <div class="footer">Feito com amor e carinho by januario ❤️</div>
    """,
    unsafe_allow_html=True,
)
