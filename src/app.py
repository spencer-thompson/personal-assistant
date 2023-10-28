"""
Usage:

streamlit run app.py
"""

import streamlit as st

from gpt import GPT

ST_SYSTEM_MSG = """
You are a helpful assistant.
Your output is formatted as github flavored markdown.
If output is mathematical ALWAYS use LaTeX wrapped in "$"s
LaTeX expressions must by wrapped in "$" or "$$" (the "$$" must be on their own lines).
Colored text, using the syntax :color[text to be colored],
where color needs to be replaced with any of the following
supported colors: blue, green, orange, red, violet, gray/grey, rainbow.
"""
# CSTutor
# --- Page Config ---
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Initialize GPT() Object into Streamlit ---
if "ai" not in st.session_state:
    st.session_state["ai"] = GPT(model="gpt-4", system_message="ST_SYSTEM_MSG")

# --- Select AI Options ---
with st.container():

    st.title("AI Chat")

    col1, col2 = st.columns([1,1])

    with col1:
        st.write("Configure your chat:")

        col1, col2 = st.columns([1,1])
        with col1:

            model = st.radio(
                "Which model would you like to use?",
                [":rainbow[GPT-4]", "GPT-3.5"],
                captions = ["Smartest Model | More Expensive", "Base ChatGPT | Faster Generations"]
            )

    with col2:
        option = st.text_input("System Message", value="You are a helpful Assistant.")

    st.write("---")

# --- Change Model ---
if model == ":rainbow[GPT-4]":
    st.session_state["ai"].update_model("gpt-4")
    gpt_model = "gpt-4"
else:
    st.session_state["ai"].update_model("gpt-3.5-turbo")
    gpt_model = "gpt-3.5-turbo"

# --- Change System Message/Tutor ---
if option != "Assistant":
    st.session_state["ai"].system_message = [
            {"role": "system", "content": option}
        ]

# --- Chat Area ---
user_input = st.chat_input("Send a message")

if user_input:

    print(st.session_state["ai"]) # Testing
    

    for message in st.session_state["ai"].messages:
        with st.chat_message(message["role"]):
            st.empty().markdown(message["content"])

    st.chat_message("user").markdown(user_input)

    placeholder = st.empty()
    message = ''
    for token in st.session_state["ai"].srun(
        query = user_input
    ):
        message += token
        placeholder.chat_message("ai").markdown(message, unsafe_allow_html=True)

    # print(message) # Testing

