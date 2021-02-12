import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The EDA App**
Credit: This App is based on the tutorial of [Chanin Nantasenamat](https://www.youtube.com/watch?v=p4uohebPuCg&list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE&index=19) (aka Data Professor)

''')

# Upload CSV data
with st.sidebar.header('1. Upload your data in CSV file format'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file")
    st.sidebar.markdown("""
    [Example CSV input file](insert_link)
    """)
