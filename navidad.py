import streamlit as st
import random
import time

st.set_page_config(page_title="Feliz Navidad 2025", page_icon="🎄", layout="centered")

NOMBRE = "Alejandro Luque"

# ========= FONDO NIEVE + ESTILO =========
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #0b1d3a, #020409);
    overflow: hidden;
}
.snow {
    position: fixed;
    top: -10px; left: 0;
    width: 100%; height: 100%;
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

/* Card */
.card {
    position: relative;
    z-index: 1;
    background: rgba(0, 0, 0, 0.65);
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 0 40px rgba(255,255,255,0.12);
    text-align: center;
}

/* Contenedor del árbol: centrado como bloque */
.tree-wrap {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

/* Code block: fuerza monospace estable */
pre code {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace !important;
    font-variant-ligatures: none !important;
    letter-spacing: 0px !important;
    line-height: 1.05 !important;
    font-size: 16px !important;
}

/* Para que el code block no quede enorme de ancho */
div[data-testid="stCodeBlock"] {
    max-width: 100%;
}
</style>

<div class="snow"></div>
""", unsafe_allow_html=True)

# ========= GENERADOR DE ÁRBOL (sin “drift”) =========
LIGHTS = ["🔴", "🟡", "🟢", "🔵", "🟣", "🟠"]

def arbol_navidad(altura=14, densidad=0.25):
    lines = []
    # estrella centrada (usamos padding fijo)
    lines.append(" " * (altura + 1) + "⭐")

    for i in range(altura):
        width = 1 + 2 * i
        left_pad = altura - i

        row = []
        for _ in range(width):
            row.append(random.choice(LIGHTS) if random.random() < densidad else "🌲")

        lines.append((" " * left_pad) + "".join(row))

    trunk_pad = " " * (altura)
    lines.append(trunk_pad + "🟫🟫🟫")
    lines.append(trunk_pad + "🟫🟫🟫")
    return "\n".join(lines)

# ========= UI =========
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("## 🎄 Feliz Navidad 2025 🎄")
st.markdown(f"### ✨ Les desea **{NOMBRE}** ✨")
st.markdown("Que esta noche esté llena de paz, amor y buenos momentos. 🎁")

tree_box = st.empty()

auto = st.toggle("Animar luces ✨", value=True)

st.markdown("</div>", unsafe_allow_html=True)

# ========= RENDER =========
def render_tree(text: str):
    st.markdown('<div class="tree-wrap">', unsafe_allow_html=True)
    st.code(text)  # st.code suele respetar mejor monospace en móviles
    st.markdown("</div>", unsafe_allow_html=True)

if auto:
    while True:
        tree_box.empty()
        with tree_box.container():
            render_tree(arbol_navidad(altura=14, densidad=0.27))
        time.sleep(0.45)
else:
    with tree_box.container():
        render_tree(arbol_navidad(altura=14, densidad=0.27))
    if st.button("Cambiar luces ✨"):
        tree_box.empty()
        with tree_box.container():
            render_tree(arbol_navidad(altura=14, densidad=0.27))
