import streamlit as st
import pandas as pd
import numpy as np

st.header("Credit card Fraud Detection")
df = pd.read_csv('creditcard.csv')
st.dataframe(df)

legit = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]

st.subheader("Legit Transactions")
st.dataframe(legit)
st.dataframe(legit.describe())
st.subheader("Fraudulent Transactions")
st.dataframe(fraud)
st.dataframe(fraud.describe())
