import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from tkinter import Image

from components.data_display.data_display import DataDisplay
from components.pie_chart.pie_chart import PieChart
from components.histogram.histogram import Histogram
from components.data_loader.data_loader import DataLoader
from components.footer.footer import Footer
from PIL import Image


# Define el título de la página y el favicon
PAGE_TITLE = "White Wine Quality Prediction"
PAGE_ICON = "🥂"  # Puedes usar un emoji o la ruta a una imagen .png

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.title("🥂 White Wine Quality Prediction")
st.write("Here you will find functionalities to predict the quality of white wine (not yet implemented).")

image = Image.open("public/images/photos/white-wine.webp")
st.image(image, caption="White Wine examples", use_container_width=True)

DATA_URL_WHITE: str = r'public/data/wine+quality/winequality-white.csv'

white_wine_data_loader = DataLoader(DATA_URL_WHITE,)
white_wine_data=white_wine_data_loader.display()

datadisplay=DataDisplay("White Wine",white_wine_data)
datadisplay.display()

# Histogram
historgram=Histogram('Histogram of Fixed Acidity (White Wine) 📊',"fixed acidity",30)
historgram.display(white_wine_data)

# PieChart of White wine quality

piechart=PieChart("White Wine Quality Distribution - Pie Chart","Quality","Count",px.colors.qualitative.Set2,0.3)

quality_counts_white = white_wine_data['quality'].value_counts().sort_index()
quality_df_white = pd.DataFrame({
    'Quality': quality_counts_white.index,
    'Count': quality_counts_white.values
})

piechart.display(quality_df_white)

if st.button("Back to main page"):
    st.session_state.page = "main"
    st.rerun()

footer= Footer()

footer.display()