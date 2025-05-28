import streamlit as st
import numpy as np
import pandas as pd

class Histogram:
    def __init__(self,histogram_title ,column_name: str, bins: int = 30):
        self.histogram_title=histogram_title
        self.column_name = column_name
        self.bins = bins

    def display(self, data: pd.Series):
        """
        Displays a histogram for a given pandas Series.

        Args:
            data (pd.Series): The data to create the histogram from.
        """
        st.subheader(self.histogram_title)
        hist_values, _ = np.histogram(data[self.column_name], bins=self.bins)
        st.bar_chart(hist_values)