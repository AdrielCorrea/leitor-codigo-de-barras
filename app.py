import streamlit as st
import requests
from PIL import Image
import io

st.title("Leitor de Códigos de Barras")

st.write("Envie uma imagem para detectar e decodificar os códigos de barras nela.")

# Upload da imagem pelo usuário
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abre a imagem com PIL
    img = Image.open(uploaded_file)
    
    # Exibe a imagem na interface
    st.image(img, caption="Imagem enviada", use_column_width=True)

    # Converte a imagem para bytes
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Faz o upload da imagem para a API ZXing
    response = requests.post(
        "https://api.qrserver.com/v1/read-qr-code/",
        files={"file": ("image.png", img_bytes, "image/png")}
    )

    # Verifica se a chamada foi bem-sucedida
    if response.ok:
        result = response.json()
        if result and isinstance(result, list) and result[0]['symbol'] and result[0]['symbol'][0]['data']:
            st.write("Códigos de barras detectados:")
            for barcode in result[0]['symbol']:
                st.write(f"**Código:** {barcode['data']}")
        else:
            st.write("Nenhum código de barras foi detectado.")
    else:
        st.write("Erro ao processar a imagem. Tente novamente.")
