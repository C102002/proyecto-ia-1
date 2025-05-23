import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image

image = Image.open("public\images\photos\Vino-para-quedarse-Foto-destacada.png")

# Mostrar la imagen con un caption y ajustarla al ancho de la columna
st.title('🍷 Wine Quality Prediction Application 🖥️')

st.image(image, caption="Wines examples", use_container_width=True)


FIXED_COLUMN: str = 'fixed acidity'
DATA_URL: str = r'public\data\wine+quality\winequality-red.csv'  # Usa una cadena "raw" para evitar problemas con los backslashes

@st.cache_data
def load_data(nrows: int) -> pd.DataFrame:
    # Agrega el parámetro sep=';' para separar correctamente las columnas
    data: pd.DataFrame = pd.read_csv(DATA_URL, sep=';')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('📥 Loading data...')
data = load_data(10000)
data_load_state.text("✅ Done! (using st.cache_data)")

if st.checkbox('👀 Show raw data'):
    st.subheader('🗃️ Raw data')
    st.write(data)

# Título y descripción para el histograma de fixed acidity
st.subheader('Histograma de Fixed Acidity 📊')

# Calcula el histograma con 30 bins (puedes ajustar este número)
hist_values, bin_edges = np.histogram(data['fixed acidity'], bins=30)

# Muestra el gráfico de barras
st.bar_chart(hist_values)

st.subheader("Distribución de Calidad de Vinos - Gráfico de Torta")

# Calcular la frecuencia de cada valor en la columna 'quality'
quality_counts = data['quality'].value_counts().sort_index()

# Crear un DataFrame para alimentar el gráfico
quality_df = pd.DataFrame({
    'Quality': quality_counts.index,
    'Count': quality_counts.values
})

# Crear el gráfico de torta utilizando Plotly Express
fig = px.pie(
    quality_df,
    values='Count',
    names='Quality',
    title='Distribución de Calidad de Vinos',
    color_discrete_sequence=px.colors.qualitative.Set3,
    hole=0.3  # Opcional: crea un "donut chart"
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)


# Agrega un separador para delimitar el final del contenido principal
st.markdown("---")

# Opción 1: Usando st.markdown con HTML sencillo (para centrar y dar algo de estilo)
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>Creado por <strong>Daniel Bortot, Hualong Chiang, Alfredo Fung, Gabrierla Martines y Juan Perdomo</strong>&mdash; &copy; 2025</p>",
    unsafe_allow_html=True
)