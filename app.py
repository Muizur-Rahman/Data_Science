import streamlit as st
from logic import greet

st.title("Hello App")

st.write(greet())