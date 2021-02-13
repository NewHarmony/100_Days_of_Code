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
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type =["csv"])
    # st.sidebar.markdown("""
    # [Example CSV input file](https://raw.githubusercontent.com/NewHarmony/100_Days_of_Code/data/master/Data_Science/Streamlit/percent_bachelors_degrees_women_usa.csv)
    # """)

#Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('--')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Waiting for CSV file to be uploaded.')
    if st.button('Click to use Example Dataset'):
        #Example data
        @st.cache
        def load_data():
            csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")
            return csv
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write("**Percentage Of Bachelors Degrees For Women In The USA **")
        st.write("Pandas example dataset")
        st.write(df)
        st.write('---')
        st.header('**Pandas_Profiling_Report**')
        st_profile_report(pr)

