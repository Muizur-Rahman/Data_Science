import streamlit as st
from logic import greet

st.title("Hello App")

name = st.text_input("Enter your name")

if name:
    st.write(greet(name))