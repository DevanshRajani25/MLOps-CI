import streamlit as st

st.title("Simple Calculator")
st.write('Enter any number to calculate square,cube or fifth power')

n = st.number_input('Enter any number',step=1,value=1)

st.write(f'Square of {n} is : {n**2}')
st.write(f'Cube of {n} is : {n**3}')
st.write(f'Fifth power of {n} is : {n**5}')
