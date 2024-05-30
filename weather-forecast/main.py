import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next days")

place = st.text_input("Place: ")
days = st.slider(
    "Forecast days", min_value=1, max_value=5, help="Select number of days to forecast"
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} of the next {days} days in {place}")


def get_date(days):
    dates = ["2022", "2023", "2024"]
    temperatures = [0, 10, 30]
    temperatures = [days * i for i in temperatures]

    return dates, temperatures


d, t = get_date(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
