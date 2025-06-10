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
          Somos [Nombre de la Empresa], una compañía especializada en desarrollo de software a medida, dedicada a transformar ideas en soluciones tecnológicas innovadoras y escalables.
          Desde [año de fundación], ayudamos a empresas y emprendedores a digitalizar sus procesos, optimizar operaciones y alcanzar sus objetivos mediante software de alta calidad.

          Nuestra Misión
          Creemos en el poder de la tecnología para impulsar el crecimiento. Nos enfocamos en desarrollar aplicaciones web, móviles y sistemas empresariales que no solo resuelvan problemas,
          sino que también generen valor a largo plazo para nuestros clientes.

          Nuestro Enfoque

          Tecnologías de vanguardia: Trabajamos con los últimos lenguajes, frameworks y metodologías ágiles.

          Soluciones personalizadas: Adaptamos cada proyecto a las necesidades específicas de tu negocio.

          Calidad y seguridad: Priorizamos código limpio, pruebas rigurosas y estándares de ciberseguridad.

          El Equipo
          Somos un equipo de desarrolladores, diseñadores UX/UI y expertos en TI apasionados por la innovación. Combinamos creatividad con expertise técnico para entregar productos que marquen la diferencia.

          Nuestro Compromiso
          Más que proveedores, somos socios tecnológicos. Nos enorgullece acompañar a nuestros clientes desde el concepto inicial hasta el despliegue y soporte continuo, garantizando resultados que impulsan su éxito.

          ¿Listo para llevar tu proyecto al siguiente nivel? [Contactános/Cotiza aquí] y construyamos juntos el software que tu negocio necesita.
                 """
                 )
        st.write("somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi somos asi ")
        st.write("[más sobre nosotros](/https://linesoft.cl/)")   
        animation_column = st.container()
    with animation_column:
        st.empty()
    
    #Servicios
    
    with st.container():    
        st.write("---") 
        st.header("""Servicios""")
        st.write("---") 
        imagen_column, text_column = st.columns ((1, 2))
        with text_column:imagen_column = st.columns(1)[0]  # Si es una sola columna
        with imagen_column:  # Esto funciona porque Streamlit columns SÍ son context managers
            st.image("imagenes/apps.png")
            st.subheader("Diseño de aplicaciones")
            st.write("el proceso el proceso el proceso el proceso el proceso el proceso el proceso el proceso ")
            st.write("[Ver Servicios >](https://valerapp.com/services)") 
        with imagen_column:  # Esto funciona porque Streamlit columns SÍ son context managers
            st.image("imagenes/apps.png")
            st.subheader("Diseño de aplicaciones")
            st.write("el proceso el proceso el proceso el proceso el proceso el proceso el proceso el proceso ")
            st.write("[Ver Servicios >](https://valerapp.com/services)") 
        