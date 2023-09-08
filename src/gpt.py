"""
Docstring

Home of the GPT Class

"""
import openai

from dotenv import load_dotenv
import os

class GPT():

    def __init__(
            self,
            model: str = "gpt-3.5-turbo",
            temperature: float = 0.7,
            system_message: str = "You are a helpful assistant"
        ):
        """Docstring"""
        self.model = model
        self.temperature = temperature
        self.system_message = [
            {"role": "system", "content": system_message}
        ]
        self.messages = []

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def call_openai_api(self, query: str):
        """Docstring"""



        response = openai.ChatCompletion.create(
            model = self.model,
            temperature = self.temperature,
            messages = self.messages + [{"role": "user", "content": query}]
        )

        return response["choices"][0]["message"]["content"]
    
    def run(self, query):
        return self.call_openai_api(query)