import streamlit as st

st.title('Add two numbers')
a = st.number_input('Enter first number')
b = st.number_input('Enter second number')

result= a+b
st.write('The sum of the two numbers: ', result)