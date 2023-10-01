"""
Docstring

Home of the GPT Class

each instance of the GPT class is a conversation thread

"""
import openai
import json
from typing import Generator

from dotenv import load_dotenv
import os

class GPT():
    gpt_models = ("gpt-3.5-turbo", "gpt-4")

    def __init__(
            self,
            model: str = gpt_models[0],
            temperature: float = 0.7,
            system_message: str = "You are a helpful assistant"
        ):
        """Docstring"""
        self._model = model
        self.temperature = temperature
        self.system_message = [
            {"role": "system", "content": system_message}
        ]
        self.messages = []

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    @staticmethod
    def zero_shot(query: str, mode = 0, model = gpt_models[0], temperature = .7):
        gpt_instance = GPT(model, temperature)
        
        if mode == 0:
            answer = gpt_instance._conversation(query)
        
        return answer["choices"][0]["message"]["content"]

    def run(self, query: str, mode: int = 0) -> str:
        """Input to get access to all of the various response types within the GPT model
        mode 0: typical access to the GPT model aka conversational
        
        Returns a string."""
        
        if mode == 0:
            response = self._conversation(query)
            
        return response["choices"][0]["message"]["content"]
    
    def srun(self, query: str, mode: int = 0) -> Generator:
        """Essentially the same as the self.run method, but streams responses.
        
        Returns a Generator. Proper use: `for i in self.run_stream(input): print(i, end='')`"""

        self._add_message(role="user", content=query)


        response = openai.ChatCompletion.create(
            model = self._model,
            temperature = self.temperature,
            messages = self.system_message + self.messages,
            stream = True
        )

        total_response = ''
        for chunk in response:
            yield chunk["choices"][0]["delta"].get("content", '\n') # * maybe change later

            total_response += chunk["choices"][0]["delta"].get("content", '')

        self._add_message(role='assistant', content=total_response)
            
    
    def _add_message(self, role: str, content: str):
        """Adds a new message to self.messages"""
        self.messages.append({"role": role, "content": content})


    def update_model(self, new_model: str):
        """Updates the model that your GPT class instance is currently running on"""
        self._model = new_model

    def __str__(self):
        return f"Model: {self._model} | Temperature: {self.temperature}, Message Length: {len(self.messages)}"

    def _call_openai_api(self):
        """Docstring"""

        response = openai.ChatCompletion.create(
            model = self._model,
            temperature = self.temperature,
            messages = self.system_message + self.messages
        )

        return response
    
    def _conversation(self, query: str):
        """Basic Running of AI system, with simple memory (appends new messages) returns information 
        in the form response["choices"][0]["message"]["content"]"""
        
        self._add_message(role="user", content=query)

        response = self._call_openai_api()

        self._add_message(
            role = response["choices"][0]["message"]["role"],
            content = response["choices"][0]["message"]["content"]
        )
    
        return response
    
    def set_system_message(self, message: str):
        """reads in a json file and will set system message as whatever your string corresponds"""
        filepath = "./system_message.json"
        with open(filepath, "r") as json_file:
            system_messages = json.load(json_file)
        self.system_message = [{"role": "system", "content": system_messages[message]}]

if __name__ == "__main__":
    ai = GPT(model = "gpt-4")
    ai.set_system_message("CSTutor")
    user_input = input(f"Chatting with {ai._model} | (q to quit):\n")
    while user_input != "q" or user_input == "Q":
        for token in ai.srun(user_input):
            print(token, end='')
        print()
        user_input = input()
