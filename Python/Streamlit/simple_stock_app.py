import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Below are the *closing* stock price and Volume of *Esty* and *Shopify*.)

""")

ticker1 = 'ETSY'
ticker2 = 'SHOP'


Esty_Data = yf.Ticker(ticker1)
Etsy_Df = Esty_Data.history(period='1d', start = '2015-5-31', end='2020-5-31')

Shop_Data = yf.Ticker(ticker2)
Shop_df = Shop_Data.history(period='1d', start = '2015-5-31', end='2020-5-31')

st.write("""
## Closing Prices
""")
st.write("""
### Etsy
""")
st.line_chart(Etsy_Df.Close)

st.write("""
### Shopify
""")
st.line_chart(Shop_df.Close)

st.write("""
## Volume
""")
st.write("""
### Etsy
""")
st.line_chart(Etsy_Df.Volume)
st.write("""
### Shopify
""")
st.line_chart(Shop_df.Volume)

