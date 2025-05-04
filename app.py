import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título principal
st.title("🎨 Mi Tablero de Dibujo")

# Panel lateral con opciones
with st.sidebar:
    st.header("🛠️ Propiedades del Dibujo")

    drawing_mode = st.selectbox(
        "Selecciona una forma para dibujar:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )

    stroke_width = st.slider("Ancho del trazo", 1, 30, 15)
    stroke_color = st.color_picker("🎨 Color del trazo", "#000000")
    bg_color = st.color_picker("🖼️ Color de fondo", "#ffffff")

# Lienzo de dibujo
st.markdown("## ✏️ Lienzo")
canvas_result = st_canvas(
    fill_color="rgba(255,165,0,0.3)",  # color de relleno con opacidad
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas",
)


