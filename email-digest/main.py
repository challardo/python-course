import requests
import os
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-04-20&sortBy=publishedAt&apiKey={weather_api_key}"

req = requests.get(url)
content = req.json()

for article in content["articles"]:
    print(article["title"])
