import requests
import selectorlib
import time

URL = "https://blog.pythonanywhere.com/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["blog"]
    return value


def send_email():
    print("email sent")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    source = scrape(URL)
    extracted = extract(source)
    print(extracted)
    content = read()
    if extracted != "None":
        if extracted not in content:
            store(extracted)
            send_email()
