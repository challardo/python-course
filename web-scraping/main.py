import requests
import selectorlib
import sqlite3

URL = "https://blog.pythonanywhere.com/"

connection = sqlite3.connect("test.db")


class Event:
    def scrape(self, url):
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["blog"]
        return value


class Email:
    def send():
        print("email sent")


def store(extracted):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts VALUES (?,?)", (None, extracted))
    connection.commit()


def read(extracted):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM posts WHERE title='{extracted}'")
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    event = Event()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)

    if extracted != "None":
        row = read(extracted)
        print("row", row)
        if not row:
            store(extracted)
            email = Email()
            email.send()
