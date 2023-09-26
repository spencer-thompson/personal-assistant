#anything
# from gtts import gTTS
import os

from gpt import GPT

ai = GPT(system_message="You are a friendly robot, you always bring up python programming in conversation.")

for i in range(3):
    user_input = input()
    for i in ai.srun(user_input):
        print(i, end='[]')
        # try: # ! This creates a ton of files on your computer
        #     gTTS(text=i, lang='en', slow=False).save(f'{i}.mp3')
        #     os.system(f'{i}.mp3')
        # except AssertionError:
        #     pass

# for mes in ai.messages:
#     print(mes)T