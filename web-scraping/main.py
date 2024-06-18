import requests
import selectorlib
import sqlite3

URL = "https://blog.pythonanywhere.com/"


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
    def send(self):
        print("email sent")


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def store(self, extracted):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO posts VALUES (?,?)", (None, extracted))
        self.connection.commit()

    def read(self, extracted):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM posts WHERE title='{extracted}'")
        rows = cursor.fetchall()
        return rows


if __name__ == "__main__":
    event = Event()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)

    if extracted != "None":
        database = Database(database_path="test.db")
        row = database.read(extracted)
        print("row", row)
        if not row:
            database.store(extracted)
            email = Email()
            email.send()
