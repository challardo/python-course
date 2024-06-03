import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_data(place, days=1):
    print(API_KEY)
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)

    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[: 8 * days]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
