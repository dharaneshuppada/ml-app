import streamlit as st
import pandas as pd

st.title("F1")

df = pd.read_csv(r"C:\Users\uppad\Desktop\sample_project-1\Car Sales Dataset - Car details v3.csv")

col = st.sidebar.multiselect("Select any column",df.columns) 

prg = st.progress(0) 

for i in range(100): 
	prg.progress(i+1) 
st.dataframe(df[col])

