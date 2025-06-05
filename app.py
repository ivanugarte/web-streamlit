import streamlit as st
from PIL import Image

# st.set_page_config(page_title="pagina web", pag_icon=" ICON", layout="wide")

st.title("Cargar imagen con Pillow")
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Imagen procesada", use_container_width=True) 
    
# introduccion 

with st.container():
    st.header("creando la pagina web")
    st.title("este es el titulo este es el tituloeste es el titulo")
    st.write("[Saber más >](https://google.com/")
    
    
# about 

with st.container():
    st.write("---")
    text_colum, text_animation_colum = st.columns(2)
    with text_colum:
        st.header("sobre nosotros") 
        st.write( 
                """
           Nuestro xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxte puedo ayudarxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
           - asi xxxxxxxxxxxxxxxxxxxxxxx      
           - asi xxxxxxxxxxxxxxxxxxxxxxx      
           - asi xxxxxxxxxxxxxxxxxxxxxxx      
           - asi xxxxxxxxxxxxxxxxxxxxxxx      
           - asi xxxxxxxxxxxxxxxxxxxxxxx      
                 """
                 )
        st.write("somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi ")
        st.write("[más sobre nosotros](/https://linesoft.cl/)")
        
                 
    

