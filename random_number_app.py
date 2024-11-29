import streamlit as st
import random

# Title of the app
st.title("Random Number Generator")

# User inputs for the range and count of random numbers
min_value = st.number_input("Enter the minimum value:", value=0)
max_value = st.number_input("Enter the maximum value:", value=100)
count = st.number_input("Enter the number of random numbers to generate:", min_value=1, step=1, value=10)

# Generate and display random numbers
if st.button("Generate"):
    if min_value > max_value:
        st.error("Minimum value cannot be greater than the maximum value!")
    else:
        random_numbers = [random.randint(min_value, max_value) for _ in range(int(count))]
        for num in random_numbers:
            st.write(num)
