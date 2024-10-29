import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Leitor de Códigos de Barras")

st.write("Envie uma imagem para detectar e decodificar os códigos de barras nela.")

# Upload da imagem pelo usuário
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abre a imagem com PIL
    img = Image.open(uploaded_file)
    
    # Converte a imagem para um array do OpenCV
    img_array = np.array(img)

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Exibe a imagem na interface
    st.image(img, caption="Imagem enviada", use_column_width=True)

    st.write("Como o OpenCV não suporta decodificação de códigos de barras diretamente, você pode considerar integrar uma API externa ou usar outra biblioteca.")

