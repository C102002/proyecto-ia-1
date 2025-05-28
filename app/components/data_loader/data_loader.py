import streamlit as st
import pandas as pd
import time

class DataLoader:
    def __init__(self, data_url: str, message: str = 'Loading data...'):
        self.__data_url = data_url
        self.__message = message

    @st.cache_data
    def display(_self) -> pd.DataFrame:
        with st.spinner(_self.__message):
            time.sleep(1)  # Simula un tiempo de carga
            try:
                data: pd.DataFrame = pd.read_csv(_self.__data_url, sep=';')
                lowercase = lambda x: str(x).lower()
                data.rename(lowercase, axis='columns', inplace=True)
                return data
            except FileNotFoundError:
                st.error(f"Error: Could not find file at {_self.__data_url}")
                return pd.DataFrame()