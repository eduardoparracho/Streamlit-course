import streamlit as st 

st.title("Hello world")

color = st.text_input("Enter your favorite color:")
animal = st.text_input("Enter your favorite animal:")
num = st.number_input("Enter your lucky number:", step=1)
power = st.selectbox("Select your superpower:", ["flying", "invisibility", "strenght"])

st.write(f"{color} {animal} of {num} with the power of {power}!")

