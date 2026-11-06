import streamlit as st
from logic import greet, add

st.title("Hello App")

name = st.text_input("Enter your name")

if name:
    st.write(greet(name))

st.subheader("Addition")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    result = add(num1, num2)
    st.write("Result:", result)