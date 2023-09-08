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
            model: str = "gpt-3.5-turbo"
        ):
        """Docstring"""
        self.model = model

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
