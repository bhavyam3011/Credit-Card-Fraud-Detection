import streamlit as st
import pandas as pd
# import matplotlib as plt

# st.header("Startup Funding Dashboard")
df = pd.read_csv('startup_cleaned.csv')
# st.dataframe(df)
# df['Investors Name'] = df['Investors Name'].fillna("undisclosed")
# df['month'] = df['Date'].dt.month
# df['year'] = df['Date'].dt.year

def load_investor_details(investor):
    # names
    st.header(investor)
    # recent events
    last5=df[df['Investors Name'].str.contains(investor)].head()[['Date','Startup','Vertical','City','Amount']] 
    st.subheader("Recent Events")
    st.dataframe(last5)

    # biggest investment 
    big=df[df['Investors Name'].str.contains('DG Ventures')].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head(3) 
    st.subheader("Biggest Investments")
    st.dataframe(big)
    #
    # general invests 

# st.sidebar.title("Startup funding analysis")
option=st.sidebar.selectbox("select one: ",['OverAll','StartUp','Investor'])

if option == 'OverAll':
    st.title('OverAll')


elif option == 'StartUp':
    select1=st.sidebar.selectbox("Select StartUp", set(df['Startup'].str.split(",").sum()))
    btn1=st.sidebar.button("find details")
    st.title('StartUp')

elif option == 'Investor':
    select2=st.sidebar.selectbox("Select investor", set(df['Investors Name'].str.split(",").sum()))
    btn2=st.sidebar.button("find details")
    st.title("Investor Analysis")

    if btn2:
        load_investor_details(select2)

    