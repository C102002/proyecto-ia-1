import streamlit as st

class Footer:
    def __init__(self):
        pass

    def display(self):
        st.markdown("---")
        st.markdown(
            "<p style='text-align: center; font-size: 14px;'>Creado por <strong>Daniel Bortot, Hualong Chiang, Alfredo Fung, Gabrierla Martines y Juan Perdomo</strong>&mdash; &copy; 2025</p>",
            unsafe_allow_html=True
        )