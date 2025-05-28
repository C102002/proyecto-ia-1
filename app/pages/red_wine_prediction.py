import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from components.data_display.data_display import DataDisplay
from components.pie_chart.pie_chart import PieChart
from components.histogram.histogram import Histogram
from components.data_loader.data_loader import DataLoader
from components.footer.footer import Footer

st.title("🍷 Red Wine Quality Prediction")
st.write("Here you will find functionalities to predict the quality of red wine (not yet implemented).")

DATA_URL_RED: str = r'public/data/wine+quality/winequality-red.csv'

red_wine_data_loader = DataLoader(DATA_URL_RED,)
red_wine_data=red_wine_data_loader.display()

# Data display
datadisplay=DataDisplay("Red Wine",red_wine_data)
datadisplay.display()


# Histogram of fixed acidity
historgram=Histogram('Histogram of Fixed Acidity (Red Wine) 📊',"fixed acidity",30)
historgram.display(red_wine_data)

# Red Wine Quality Distribution - Pie Chart 
piechart=PieChart("Red Wine Quality Distribution - Pie Chart","Quality","Count",px.colors.qualitative.Set1,0.3)

quality_counts_red = red_wine_data['quality'].value_counts().sort_index()

quality_df_red = pd.DataFrame({
    'Quality': quality_counts_red.index,
    'Count': quality_counts_red.values
})
piechart.display(quality_df_red)

if st.button("Back to main page"):
    st.session_state.page = "main"
    st.rerun()

footer= Footer()

footer.display()
