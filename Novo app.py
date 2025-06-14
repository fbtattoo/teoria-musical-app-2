import streamlit as st

st.title("🎼 Teoria Musical - Escalas e Notas")

notas = ['C', 'C#', 'D', 'D#', 'E', 'F',
         'F#', 'G', 'G#', 'A', 'A#', 'B']

escala_maior = [0, 2, 4, 5, 7, 9, 11]
escala_menor = [0, 2, 3, 5, 7, 8, 10]

# Seleção da tônica e tipo de escala
tonica = st.selectbox("Escolha a tônica:", notas)
tipo = st.selectbox("Escolha o tipo da escala:", ["Maior", "Menor"])

# Calcula a escala
pos = notas.index(tonica)
intervalos = escala_maior if tipo == "Maior" else escala_menor
escala = [(pos + i) % 12 for i in intervalos]
notas_escala = [notas[i] for i in escala]

st.write(f"Escala {tipo} de {tonica}: ", ", ".join(notas_escala))

# Mostrar teclado virtual simples
st.write("### Teclado virtual:")

cols = st.columns(12)
for i, nota in enumerate(notas):
    if i in escala:
        cols[i].button(nota, key=f"nota_{i}", disabled=False)
    else:
        cols[i].button(nota, key=f"nota_off_{i}", disabled=True)
