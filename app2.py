import streamlit as st
from PIL import Image

st.title("Calculator App")

col1, col2, col3 = st.columns(3)

def add(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

def mul(a,b):
    c = a*b
    return c

x = st.number_input("Input your first number")
y = st.number_input("Input your second number")

with col1:
    if st.button("Add"):
        st.write(add(x,y))

with col2:
    if st.button("Substract"):
        st.write(sub(x,y))
        
with col3:
    if st.button("Multiply"):
        st.write(mul(x,y))
