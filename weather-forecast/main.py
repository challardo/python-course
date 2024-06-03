import streamlit as st
import plotly.express as px
from api import get_data

st.title("Weather Forecast for the next days")

place = st.text_input("Place: ")
days = st.slider(
    "Forecast days", min_value=1, max_value=5, help="Select number of days to forecast"
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} of the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [data["main"]["temp"] / 10 for data in filtered_data]
            dates = [data["dt_txt"] for data in filtered_data]
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"}
            )
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [data["weather"][0]["main"] for data in filtered_data]
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
            }
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=150)
    except KeyError:
        st.write("That place does not exist.")
