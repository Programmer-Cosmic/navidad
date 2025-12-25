import streamlit as st
import random
import time
import math

from PIL import Image, ImageDraw

st.set_page_config(page_title="Feliz Navidad 2025", page_icon="🎄", layout="centered")

NOMBRE = "Alejandro Luque"

# ========= FONDO NIEVE (CSS) =========
st.markdown("""
<style>
body { background: linear-gradient(to bottom, #0b1d3a, #020409); overflow: hidden; }
.snow {
    position: fixed; top: -10px; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    background-image:
        radial-gradient(white 1px, transparent 1px),
        radial-gradient(white 1.5px, transparent 1.5px),
        radial-gradient(white 2px, transparent 2px);
    background-size: 60px 60px, 120px 120px, 200px 200px;
    animation: snow 18s linear infinite;
    opacity: 0.85;
    z-index: 0;
}
@keyframes snow {
    0%   { background-position: 0 0,   0 0,   0 0; }
    100% { background-position: 0 900px, 0 700px, 0 500px; }
}
.card {
    position: relative; z-index: 1;
    background: rgba(0,0,0,0.65);
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 0 40px rgba(255,255,255,0.12);
    text-align: center;
}
</style>
<div class="snow"></div>
""", unsafe_allow_html=True)

# ========= DIBUJO DEL ÁRBOL (IMAGEN) =========
def draw_tree_png(
    w=900, h=600,
    layers=12,
    seed=None,
    twinkle=False
):
    if seed is not None:
        random.seed(seed)

    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Centro del árbol
    cx = w // 2
    top_y = 70
    base_y = h - 120

    # Estrella
    star_r = 18
    d.ellipse((cx-star_r, top_y-star_r, cx+star_r, top_y+star_r), fill=(255, 220, 80, 255))
    d.ellipse((cx-7, top_y-7, cx+7, top_y+7), fill=(255, 245, 180, 255))

    # Colores
    green1 = (20, 140, 70, 255)
    green2 = (18, 110, 60, 255)
    trunk = (120, 80, 45, 255)

    lights = [
        (255, 60, 60, 255),   # rojo
        (255, 220, 60, 255),  # amarillo
        (80, 220, 120, 255),  # verde
        (80, 160, 255, 255),  # azul
        (200, 120, 255, 255), # violeta
        (255, 160, 60, 255),  # naranja
    ]

    # Árbol (triángulo por capas)
    for i in range(layers):
        t = i / (layers - 1)  # 0..1
        y = int(top_y + 35 + t * (base_y - (top_y + 35)))
        half = int(40 + t * 280)  # ancho creciente
        # capa verde
        d.polygon(
            [(cx - half, y), (cx + half, y), (cx, y - 55)],
            fill=green1 if i % 2 == 0 else green2
        )

        # Luces sobre la capa
        n_lights = int(4 + t * 12)
        for _ in range(n_lights):
            lx = random.randint(cx - half + 20, cx + half - 20)
            ly = random.randint(y - 45, y - 5)

            # efecto titilar: cambia brillo al azar
            col = random.choice(lights)
            if twinkle and random.random() < 0.45:
                col = (min(col[0] + 40, 255), min(col[1] + 40, 255), min(col[2] + 40, 255), 255)

            r = random.randint(6, 10)
            d.ellipse((lx-r, ly-r, lx+r, ly+r), fill=col)

            # brillo suave
            glow_r = r + 6
            glow = (col[0], col[1], col[2], 50)
            d.ellipse((lx-glow_r, ly-glow_r, lx+glow_r, ly+glow_r), fill=glow)

    # Tronco
    tw, th = 110, 90
    d.rounded_rectangle(
        (cx - tw//2, base_y + 10, cx + tw//2, base_y + 10 + th),
        radius=18, fill=trunk
    )

    # Suelo nieve leve
    d.ellipse((cx-340, base_y+70, cx+340, base_y+170), fill=(255, 255, 255, 30))

    return img

# ========= UI =========
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("## 🎄 Feliz Navidad 2025 🎄")
st.markdown(f"### ✨ Les desea **{NOMBRE}** ✨")
st.markdown("Que esta noche esté llena de paz, amor y buenos momentos. 🎁")
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    speed = st.select_slider("Velocidad luces", options=[0.2, 0.35, 0.5, 0.7, 1.0], value=0.35)
with col2:
    auto = st.toggle("Animar luces ✨", value=True)

img_box = st.empty()

if auto:
    k = 0
    while True:
        # seed cambia en cada frame para que titilen distinto
        img = draw_tree_png(seed=1000 + k, twinkle=True)
        img_box.image(img, use_container_width=True)
        time.sleep(speed)
        k += 1
else:
    img = draw_tree_png(seed=123, twinkle=False)
    img_box.image(img, use_container_width=True)
    if st.button("Cambiar luces ✨"):
        img = draw_tree_png(seed=random.randint(1, 99999), twinkle=True)
        img_box.image(img, use_container_width=True)
