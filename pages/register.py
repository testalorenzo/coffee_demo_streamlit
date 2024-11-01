#
# Register your coffee
#

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title('Register your coffee')

df = pd.read_csv('coffee_consumption - Sheet1.csv')
df['Date'] = pd.to_datetime(df['Date'])

with st.form("register_form"):
   st.write("Fill out the form below to register your coffee")
   name = st.text_input('Name')
   submitted = st.form_submit_button('Submit my coffee')

   if submitted:
      new_row = {'Name': name, 'Date': pd.Timestamp.now(), 'Count': 1}
      df = df.append(new_row, ignore_index=True)
      df.to_csv('coffee_consumption - Sheet1.csv', index=False) # <-- Remember the data flow!!! 
      st.write('Your coffee has been registered!')
   
st.dataframe(df)