import streamlit as st
import pandas as pd

st.title("Fund Data Chatbot")

holdings = pd.read_csv("holdings.csv")
trades = pd.read_csv("trades.csv")

st.subheader("Holdings Data")
st.dataframe(holdings)

st.subheader("Trades Data")
st.dataframe(trades)

question = st.text_input("Ask question about fund data")

if question:
    st.write("You asked:", question)
