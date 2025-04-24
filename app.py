import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Mi tablero de dibujo")
with st.sidebar:
  st.subheader("Propiedades")
  drawing_mode = st.sidebar.selectbox(
    "formas para dibujar",
  ("freedraw","line","rect","circle","transform","polygon","point"),
  )
  stroke_width= st.slider('Selecciona el ancho', 1,30,15)
  stroke_color= st.color_picker("color de trazo","#ffffff")
  bg_color= st.color_picker("color de trazo","#0000000")

canvas_result = st_canvas(
  fill_color="rgba(255,165,0,0.3)", #fixed fill color with some opacity
  stroke_width= stroke_width,
  stroke_color=stroke_color,
  background_color=bg_color,
  height=300,
  width=500,
  drawing_mode=drawing_mode,
  key="canvas",
)
