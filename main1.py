import streamlit as st
st.markdown("# Main page 🎈")
x="Welcome to this great learning, all those interested to learn Python,  Machine learning"
st.sidebar.markdown(x)
x = st.slider('x')  # 👈 this is a widget
st.write(x, "Select your best contast level" ,x * x)
st.title("welcome to my streamlit tought")
st.write("   what is you name ")
for x in range(100):
	pass 
	x=x+40
st.write("your_age is \n")
st.write(x)
st.subheader("My 2023 Objectives")
st.write(" What are them?")

import pandas as pd
df = pd.DataFrame({
   
  'ID': [1, 2, 3, 4],
  'name of cl':["abe","kabe","alem", "Andu"],
  'Age': [10, 20, 30, 40],
  'Acyear':[2020, 2022, 2021, 2023],
  'CGPA':[3.6, 4.0, 3.6, 3.8]
})
df
option = st.selectbox(
    'Which column data do you fit for your_info select? \n Age',

     df['Age'])

'you selected Age:', option
option = st.selectbox(
	'ID',
     df['ID'])

'you selected GPA:', option
option = st.selectbox(
    'cgpa',
     df['CGPA'])

'you selected:', option
