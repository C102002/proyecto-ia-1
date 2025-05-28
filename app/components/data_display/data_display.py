import streamlit as st
import pandas as pd

class DataDisplay:
    def __init__(self, title: str, data: pd.DataFrame):
        self.title = title
        self.data = data

    def display(self):
        st.subheader(f'📊 {self.title} Data Analysis')
        if st.checkbox(f'👀 Show raw {self.title.capitalize()} data'):
            st.subheader(f'🗃️ Raw {self.title.capitalize()} data')
            st.write(self.data)