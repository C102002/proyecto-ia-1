import streamlit as st
import pandas as pd
import plotly.express as px

class PieChart:
    def __init__(self, title: str, names_column: str, values_column: str, color_sequence=None, hole: float = 0):
        self.title = title
        self.names_column = names_column
        self.values_column = values_column
        self.color_sequence = color_sequence
        self.hole = hole

    def display(self, df: pd.DataFrame):
        """
        Displays a pie chart using Plotly Express.

        Args:
            df (pd.DataFrame): The DataFrame containing the data.
        """
        st.subheader(self.title)
        fig = px.pie(
            df,
            values=self.values_column,
            names=self.names_column.capitalize(),
            title=self.title,
            color_discrete_sequence=self.color_sequence,
            hole=self.hole
        )
        st.plotly_chart(fig)