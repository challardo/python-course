import smtplib, ssl
import os
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()


def send_email(image_path):
    host = os.getenv("EMAIL_HOST")
    port = os.getenv("EMAIL_PORT")
    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    receiver = os.getenv("EMAIL_RECIEVER")
    context = ssl.create_default_context()

    email_message = EmailMessage()
    email_message["subject"] = "Subject showd up!"
    email_message.set_content("we saw a new subject")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(
        content, maintype="image", subtype=imghdr.what(None, content)
    )

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())


if __name__ == "__main__":
    send_email(image_path="images/21.png")
