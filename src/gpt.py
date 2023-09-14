"""
Docstring

Home of the GPT Class

each instance of the GPT class is a conversation thread

"""
import openai

from typing import Generator

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
        self._model = model
        self.temperature = temperature
        self.system_message = [
            {"role": "system", "content": system_message}
        ]
        self.messages = []

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    @staticmethod
    def zero_shot(query: str, mode = 0, gpt_model = "gpt-3.5-turbo"):
        return string

    def run(self, query: str, mode = 0, gpt_model = "gpt-3.5-turbo") -> str:
        """Input to get access to all of the various response types within the GPT model
        mode 0: typical access to the GPT model
        
        Returns a string."""
        
        self._update_model(gpt_model)
        
        if mode == 0:
            response = self._conversation(query)
            
        return response["choices"][0]["message"]["content"]
    
    def srun(self, query: str) -> Generator:
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


    def _update_model(self, new_model: str):
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
        """Basic Running of AI system, with simple memory (appends new messages)"""
        self._add_message(role="user", content=query)

        response = self._call_openai_api()

        self._add_message(
            role = response["choices"][0]["message"]["role"],
            content = response["choices"][0]["message"]["content"]
        )
    
        return response["choices"][0]["message"]["content"]
    
    # --- Notes ---
    # We can start "remodeling" Because we are on a new branch.
    # You're welcome to go crazy haha.
    # Maybe you can show me what you want to implement in this new branch,
    # and then we can start moving together on this.