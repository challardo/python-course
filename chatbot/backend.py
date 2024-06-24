import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


class Chatbot:
    def __init__(self):
        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = (
            openai.completions.create(
                model="gpt-3.5-turbo-0125",
                prompt=user_input,
                max_tokens=4000,
                temperature=0.5,
            )
            .choices[0]
            .text
        )

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about dogs.")
    print(response)
