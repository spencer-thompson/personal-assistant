from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live

import argparse

from gpt import GPT

parser = argparse.ArgumentParser(description="A Simple CLI for gpt-4")
parser.add_argument('-m', '--model',
                    type=str,
                    help='gpt-4 or gpt-3.5-turbo',
                    default='gpt-4')

parser.add_argument('-sys', '--system_message',
                    type=str,
                    help='System Message to guide GPT-4',
                    default="You are a capable and helpful assistant. If you don't know the answer to a question, tell the user. Format responses in markdown.")

parser.add_argument('-t', '--temperature',
                    type=float,
                    help='Creativity or "Randomness" of GPT, 0 is boring, 1.0 is wild.',
                    default=0.7)

console = Console()

args = parser.parse_args()

def generate_panel(message: Markdown) -> Panel:
    """Cool red box"""
    return Panel(
        message,
        box=box.HEAVY,
        title=args.model,
        border_style="red",
        # padding=1,
        expand=True,
        highlight=True
    )

def main():
    """Main execution loop"""


    ai = GPT(
        model = args.model,
        temperature = args.temperature,
        system_message = args.system_message
    )

    user_input = console.input(f"Chatting with {ai._model} | (q to quit):\nUser: ")
    # --- Conversation Loop ---
    while user_input != "q" or user_input != "Q":
        whole_message = ''

        with Live(generate_panel(message=whole_message), refresh_per_second=4) as live:

            for token in ai.srun(user_input):

                whole_message += token
                live.update(generate_panel(Markdown(whole_message)))

        print()
        user_input = console.input("User: ")
        if user_input == "c" or user_input == "C":
            ai.clear_messages()

if __name__ == "__main__":
    main()