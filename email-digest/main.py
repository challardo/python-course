import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-04-20&sortBy=publishedAt&apiKey={weather_api_key}"

req = requests.get(url)
content = req.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body += str(article["title"]) + "\n" + str(article["description"]) + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
