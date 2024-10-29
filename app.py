import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

st.title("Leitor de Códigos de Barras")

st.write("Envie uma imagem para detectar e decodificar os códigos de barras nela.")

# Upload da imagem pelo usuário
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abre a imagem e exibe na interface
    img = Image.open(uploaded_file)
    st.image(img, caption="Imagem enviada", use_column_width=True)
    
    # Decodifica os códigos de barras
    barcodes = decode(img)
    
    # Exibe o resultado
    if barcodes:
        st.write("Códigos de barras detectados:")
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            st.write(f"**Tipo:** {barcode_type} | **Código:** {barcode_data}")
    else:
        st.write("Nenhum código de barras foi detectado.")
