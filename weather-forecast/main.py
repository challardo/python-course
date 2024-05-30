import streamlit as st

st.title("Weather Forecast for the next days")

place = st.text_input("Place: ")
days = st.slider(
    "Forecast days", min_value=1, max_value=5, help="Select number of days to forecast"
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} of the next {days} days in {place}")
