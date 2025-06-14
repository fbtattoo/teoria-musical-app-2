
import streamlit as st
import base64

# Estilização moderna com CSS embutido
st.markdown("""
<style>
    body { background-color: #0f0f0f; }
    .stApp {
        background-color: #141414;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }
    div[data-testid="stColumn"] {
        padding: 4px;
    }
    .note-key {
        border-radius: 6px;
        padding: 8px 12px;
        text-align: center;
        margin: 2px;
        background-color: #222;
        color: #ddd;
        font-weight: bold;
        box-shadow: 0 0 6px #00f5d4;
    }
    .note-key.active {
        background-color: #00f5d4;
        color: #000;
        box-shadow: 0 0 10px #00f5d4;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🎼 Teoria Musical Interativa")
st.markdown("**Escolha uma tônica e veja sua escala no piano visual.**")

# Dados musicais
notas = ['C', 'C#', 'D', 'D#', 'E', 'F',
         'F#', 'G', 'G#', 'A', 'A#', 'B']

escala_maior = [0, 2, 4, 5, 7, 9, 11]
escala_menor = [0, 2, 3, 5, 7, 8, 10]

# Interface de escolha
col1, col2 = st.columns(2)
with col1:
    tonica = st.selectbox("🎵 Tônica", notas)
with col2:
    tipo = st.selectbox("🎼 Tipo de Escala", ["Maior", "Menor"])

# Lógica de escala
pos = notas.index(tonica)
intervalos = escala_maior if tipo == "Maior" else escala_menor
escala = [(pos + i) % 12 for i in intervalos]
notas_escala = [notas[i] for i in escala]

# Resultado textual
st.markdown(f"### 🎶 Escala {tipo} de **{tonica}**: " +
            ", ".join([f"`{n}`" for n in notas_escala]))

st.markdown("---")

# Teclado visual (linha horizontal de botões coloridos)
st.markdown("### 🎹 Teclado virtual:")

cols = st.columns(12)
for i, nota in enumerate(notas):
    key_class = "note-key active" if nota in notas_escala else "note-key"
    with cols[i]:
        st.markdown(f'<div class="{key_class}">{nota}</div>', unsafe_allow_html=True)
