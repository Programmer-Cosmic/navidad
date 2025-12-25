import streamlit as st
import random
import time

st.set_page_config(
    page_title="Feliz Navidad 2025",
    page_icon="🎄",
    layout="centered"
)

NOMBRE = "Alejandro Luque"

# =========================
# FONDO ANIMADO CON NIEVE
# =========================
st.markdown("""
<style>
/* Fondo */
body {
    background: linear-gradient(to bottom, #0b1d3a, #020409);
    overflow: hidden;
}

/* Capa de nieve */
.snow {
    position: fixed;
    top: -10px;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image:
        radial-gradient(white 1px, transparent 1px),
        radial-gradient(white 1.5px, transparent 1.5px),
        radial-gradient(white 2px, transparent 2px);
    background-size: 60px 60px, 120px 120px, 200px 200px;
    animation: snow 20s linear infinite;
    opacity: 0.8;
    z-index: 0;
}

@keyframes snow {
    0% { background-position: 0 0, 0 0, 0 0; }
    100% { background-position: 0 1000px, 0 800px, 0 600px; }
}

/* Contenedor principal */
.card {
    position: relative;
    z-index: 1;
    background: rgba(0, 0, 0, 0.65);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 0 40px rgba(255,255,255,0.15);
    text-align: center;
}

.tree {
    font-family: monospace;
    white-space: pre;
    line-height: 1.1;
    font-size: 18px;
}
</style>

<div class="snow"></div>
""", unsafe_allow_html=True)

# =========================
# ÁRBOL CON LUCES
# =========================
LIGHTS = ["🔴", "🟡", "🟢", "🔵", "🟣"]

def arbol_navidad(altura=14):
    lineas = []
    lineas.append(" " * altura + "⭐")
    for i in range(altura):
        ancho = 1 + i * 2
        relleno = " " * (altura - i)
        fila = ""
        for _ in range(ancho):
            fila += random.choice(LIGHTS) if random.random() < 0.25 else "🌲"
        lineas.append(relleno + fila)
    tronco = " " * altura + "🟫🟫🟫"
    lineas.append(tronco)
    lineas.append(tronco)
    return "\n".join(lineas)

# =========================
# CONTENIDO
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("## 🎄 Feliz Navidad 2025 🎄")
st.markdown(f"### ✨ Les desea **{NOMBRE}** ✨")
st.markdown("Que esta noche esté llena de paz, amor y buenos momentos. 🎁")

arbol_container = st.empty()

if st.toggle("Animar luces ✨", value=True):
    while True:
        arbol_container.markdown(
            f'<div class="tree">{arbol_navidad()}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.5)
else:
    arbol_container.markdown(
        f'<div class="tree">{arbol_navidad()}</div>',
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)