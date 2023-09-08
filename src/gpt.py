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

    def run(self, query: str):
        """Basic Running of AI system"""
        self.add_message(role="user", content=query)

        response = self.call_openai_api()

        self.add_message(
            role = response["choices"][0]["message"]["role"],
            content = response["choices"][0]["message"]["content"]
        )
    
        return response["choices"][0]["message"]["content"]
    
    def add_message(self, role: str, content: str):
        """Adds a new message to self.messages"""
        self.messages.append({"role": role, "content": content})


    def call_openai_api(self):
        """Docstring"""



        response = openai.ChatCompletion.create(
            model = self.model,
            temperature = self.temperature,
            messages = self.system_message + self.messages
        )

        return response
    