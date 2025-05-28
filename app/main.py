import streamlit as st
from PIL import Image

from components.footer.footer import Footer

# Define el título de la página y el favicon
PAGE_TITLE = "Wine Quality App"
PAGE_ICON = "🍷"  # Puedes usar un emoji o la ruta a una imagen .png

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title('🍷 Wine Quality Prediction Application 🖥️')
st.write("Welcome to the Wine Quality Prediction Application.")

image = Image.open("public/images/photos/red-wine-vs-white-wine.jpg")
st.image(image, caption="Wine examples", use_container_width=True)

st.subheader("Select the type of wine for prediction in the sidebar.")
st.write("Navigate using the sidebar on the left to access the prediction pages.")

footer= Footer()
footer.display()