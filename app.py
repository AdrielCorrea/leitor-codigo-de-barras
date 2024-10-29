import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Leitor de Códigos de Barras")

st.write("Envie uma imagem para detectar e decodificar os códigos de barras nela.")

# Upload da imagem pelo usuário
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abre a imagem
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # Inicializa o detector de códigos de barras
    detector = cv2.BarcodeDetector()

    # Detecta códigos de barras na imagem
    barcodes, _ = detector(gray)

    # Exibe a imagem na interface
    st.image(img, caption="Imagem enviada", use_column_width=True)

    # Exibe os códigos de barras detectados
    if barcodes:
        st.write("Códigos de barras detectados:")
        for barcode in barcodes:
            st.write(f"**Código:** {barcode.data.decode('utf-8')}")
    else:
        st.write("Nenhum código de barras foi detectado.")

