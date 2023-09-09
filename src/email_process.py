# Import the receive_email module
import receive_email
import gpt
import os
from dotenv import load_dotenv

# Email server settings
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Directory to save .txt files
SAVE_DIR = os.getenv("SAVE_DIR")

# Contact email address to filter by
SPECIFIC_CONTACT = os.getenv("SPECIFIC_CONTACT")

txt_content = receive_email.extract_text_from_email(EMAIL_ADDRESS, EMAIL_PASSWORD, SPECIFIC_CONTACT)


if txt_content == "Empty" or txt_content is None:
    pass
else:
    from gpt import GPT

    ai = GPT()


    user_input = txt_content
    print(ai.run(txt_content))

    for mes in ai.messages:
        print(mes)
    