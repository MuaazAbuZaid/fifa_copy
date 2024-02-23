import streamlit as st 
import pandas as pd

df = pd.read_csv('./Sources/fifa_eda.csv')

st.markdown('<h1> <center> Data </center> </h1>',unsafe_allow_html= True)
st.markdown('<a href= "https://www.kaggle.com/datasets"> <center> Link to DataSet </center> </a>',unsafe_allow_html= True)
st.write(df)