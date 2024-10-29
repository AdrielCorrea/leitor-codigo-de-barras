import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image
import imageio

st.title("Leitor de Códigos de Barras")

st.write("Envie uma imagem para detectar e decodificar os códigos de barras nela.")

# Upload da imagem pelo usuário
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abre a imagem
    img = Image.open(uploaded_file)
    
    # Converte a imagem para um formato que o pyzbar pode ler
    img = img.convert('RGB')
    img_array = imageio.imread(uploaded_file)

    # Decodifica os códigos de barras
    barcodes = decode(img_array)

    # Exibe a imagem na interface
    st.image(img, caption="Imagem enviada", use_column_width=True)

    # Exibe os códigos de barras detectados
    if barcodes:
        st.write("Códigos de barras detectados:")
        for barcode in barcodes:
            st.write(f"**Código:** {barcode.data.decode('utf-8')}")
    else:
        st.write("Nenhum código de barras foi detectado.")
