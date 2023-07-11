import streamlit as st
import numpy as np
import pandas as pd
st.markdown("#  Free Training for those all who interested#🎈")
x="Welcome all those interested to learn Python, Rstudio, Machine learning"
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
  'CGPA':[3.6, 4.0, 3.6, 3.8],
  'BPlace': ["hawasa", "AA","XX", "hs"],
  'gender': ["m","f","m","f"]
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
option = st.selectbox(
    'cgpa',
     df['gender'])

'you selected gender:', option

st.write("Are you ready to learn?")
st.write("would you tell me your address?")
st.write("Are you from ethiopia?")


st.write("my forloop")
for i in range(5):
	st.write(i)

st.write("my while")
	
count=5

while  count<10:
	st.write(count)
	count +=1

x=12

if x>20:

 st.write("you are old")

else:

 st.write("you are child")
