import streamlit as st
from PIL import Image

from components.footer.footer import Footer

st.title('🍷 Wine Quality Prediction Application 🖥️')
st.write("Welcome to the Wine Quality Prediction Application.")

image = Image.open("public/images/photos/Vino-para-quedarse-Foto-destacada.png")
st.image(image, caption="Wine examples", use_container_width=True)

st.subheader("Select the type of wine for prediction in the sidebar.")
st.write("Navigate using the sidebar on the left to access the prediction pages.")

footer= Footer()
footer.display()