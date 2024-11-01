#
# Visualize data
#

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title('Explore data')

st.header('Interacting with secrets')

st.write('It is time to reveal my secret!')
st.secrets['MY_SECRET']

st.header('Example of online data connection')
# Establish a connection to Google Sheets.
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from Google Sheets.
df = conn.read()
df['Date'] = pd.to_datetime(df['Date'])

st.dataframe(df)

# Plot data.
st.bar_chart(data=df, x='Name', y='Count')
st.line_chart(data=df.groupby('Date').sum().reset_index(), x='Date', y='Count')


st.header('Example of offline data connection')
# Read data from a local CSV file.
df = pd.read_csv('coffee_consumption - Sheet1.csv')
df['Date'] = pd.to_datetime(df['Date'])

st.dataframe(df)
st.bar_chart(data=df, x='Name', y='Count')
st.line_chart(data=df.groupby('Date').sum().reset_index(), x='Date', y='Count')
