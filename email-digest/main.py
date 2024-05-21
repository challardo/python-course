import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

topic = "tesla"

weather_api_key = os.getenv("WEATHER_API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={weather_api_key}&language=en"

req = requests.get(url)
content = req.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += (
            "Subject: Today's news "
            + "\n"
            + str(article["title"])
            + "\n"
            + str(article["description"])
            + "\n"
            + str(article["url"])
            + "\n\n"
        )

body = body.encode("utf-8")
send_email(message=body)
