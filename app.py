import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from time import sleep

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Ventas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos
@st.cache_data  # Cache para mejor rendimiento
def load_data():
    return pd.read_csv('datos_ventas.csv')

df = load_data()
df_count = df.groupby("Producto").count().reset_index()

# Efectos visuales
with st.spinner('Cargando datos...'):
    sleep(1)  # Simular carga

# Barra de progreso
progress_bar = st.progress(0)
for i in range(100):
    sleep(0.01)
    progress_bar.progress(i + 1)

# Título con efecto
st.title("📈 Dashboard de Ventas Interactivo")
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.fade-in {
    animation: fadeIn 1.5s;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="fade-in">Visualización avanzada de datos de ventas</p>', unsafe_allow_html=True)

# Sidebar con controles
with st.sidebar:
    st.header("Filtros")
    producto_seleccionado = st.multiselect(
        "Seleccione productos:",
        options=df['Producto'].unique(),
        default=df['Producto'].unique()[0:3]
    )
    
    animar_graficos = st.checkbox("Activar animaciones", value=True)
    tema = st.selectbox("Tema del gráfico", ["plotly", "ggplot2", "seaborn"])

# Filtrado de datos
df_filtrado = df[df['Producto'].isin(producto_seleccionado)] if producto_seleccionado else df

# Mostrar datos con pestañas
tab1, tab2, tab3, tab4 = st.tabs(["📊 Datos", "📈 Gráficos", "🗺 Mapa", "🔍 Análisis"])

with tab1:
    st.header("Datos de Ventas")
    st.write(f"Mostrando {len(df_filtrado)} de {len(df)} registros")
    
    # DataFrame con estilo
    st.dataframe(
        df_filtrado.style.highlight_max(axis=0, color='lightgreen')
        .highlight_min(axis=0, color='#ffcccb'),
        height=400,
        use_container_width=True
    )
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Ventas Totales", f"${df_filtrado['Precio_Unitario'].sum():,.2f}")
    col2.metric("Productos Únicos", len(df_filtrado['Producto'].unique()))
    col3.metric("Transacciones", len(df_filtrado))

with tab2:
    st.header("Visualizaciones Interactivas")
    
    # Gráfico de pastel con efecto
    with st.expander("Distribución por Producto", expanded=True):
        fig_pie = px.pie(
            df_filtrado, 
            names="Producto", 
            title="Distribución de Ventas por Producto",
            template=tema
        )
        if animar_graficos:
            fig_pie.update_traces(pull=[0.1]*len(df_filtrado))
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Gráfico de barras
    with st.expander("Ventas por Región"):
        fig_bar = px.bar(
            df_filtrado.groupby('Region')['Precio_Unitario'].sum().reset_index(),
            x='Region',
            y='Precio_Unitario',
            color='Region',
            title='Ventas Totales por Región',
            template=tema,
            animation_frame='Region' if animar_graficos else None
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Gráfico de líneas temporal
    if 'Fecha' in df_filtrado.columns:
        with st.expander("Tendencia de Ventas"):
            try:
                df_filtrado['Fecha'] = pd.to_datetime(df_filtrado['Fecha'])
                df_temporal = df_filtrado.set_index('Fecha').resample('M')['Precio_Unitario'].sum().reset_index()
                
                fig_line = px.line(
                    df_temporal,
                    x='Fecha',
                    y='Precio_Unitario',
                    title='Tendencia Mensual de Ventas',
                    template=tema,
                    markers=True
                )
                if animar_graficos:
                    fig_line.update_layout(
                        xaxis=dict(
                            rangeslider=dict(visible=True),
                            type="date"
                        )
                    )
                st.plotly_chart(fig_line, use_container_width=True)
            except:
                st.warning("No se pudo generar la tendencia temporal")

with tab3:
    st.header("Visualización Geográfica")
    if 'Latitud' in df_filtrado.columns and 'Longitud' in df_filtrado.columns:
        fig_map = px.scatter_geo(
            df_filtrado,
            lat='Latitud',
            lon='Longitud',
            color='Producto',
            size='Precio_Unitario',
            projection='natural earth',
            title='Distribución Geográfica de Ventas',
            template=tema
        )
        st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.warning("Datos geográficos no disponibles")

with tab4:
    st.header("Análisis Detallado")
    
    # Heatmap de correlación
    st.subheader("Matriz de Correlación")
    numeric_df = df_filtrado.select_dtypes(include=[np.number])
    if len(numeric_df.columns) > 1:
        corr = numeric_df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No hay suficientes columnas numéricas para el análisis de correlación")
    
    # Histograma interactivo
    st.subheader("Distribución de Precios")
    col = st.selectbox("Seleccione columna para histograma", numeric_df.columns)
    fig_hist = px.histogram(
        df_filtrado, 
        x=col, 
        nbins=20, 
        title=f'Distribución de {col}',
        template=tema
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Efecto de confeti al final
if st.button('🎉 Celebrar!'):
    st.balloons()

# Notas finales
st.markdown("---")
st.caption("Dashboard creado con Streamlit | © 2023")