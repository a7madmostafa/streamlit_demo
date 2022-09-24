import streamlit as st
import pandas as pd

st.title("About")

st.info("This is a test")

st.success("This is a test")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age")

height = st.slider("Enter your height", min_value=0,
                   max_value=200, value=100, step=10)
