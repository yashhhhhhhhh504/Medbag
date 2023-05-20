import streamlit as st
import random

# Set page title and layout
st.set_page_config(page_title="Random Number Generator", page_layout="wide")

# Define the UI elements
st.title("Random Number Generator")
message = st.text_input("Enter a message:")
button = st.button("Generate Random Number")

# Define the callback function for the button
if button:
    random_number = random.randint(1, 10)
    st.write(f"Message: {message}")
    st.write(f"Random Number: {random_number}")
