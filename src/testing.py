#anything

from gpt import GPT

ai = GPT(system_message="You are a friendly robot, you always bring up python programming in conversation.")


for i in range(3):
    user_input = input()
    print(ai.run(user_input))

for mes in ai.messages:
    print(mes)