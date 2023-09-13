import streamlit as st

from gpt import GPT

# --- Page Config ---
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Initialize GPT() Object into Streamlit ---
if "ai" not in st.session_state:
    st.session_state["ai"] = GPT(system_message="You are a helpful assistant, you output to github flavored markdown.")

# --- Select AI Options ---
with st.container():
    st.title("AI Chat")
    st.write("Configure your chat:")

    col1, col2 = st.columns([1,1])
    with col1:

        model = st.radio(
            "Which model would you like to use?",
            [":rainbow[GPT-4]", "GPT-3.5"],
            captions = ["Smartest Model | More Expensive", "Base ChatGPT | Faster Generations"]
        )

    st.write("---")


if model == ":rainbow[GPT-4]":
    st.session_state["ai"].update_model("gpt-4")
else:
    st.session_state["ai"].update_model("gpt-3.5-turbo")

# --- Chat Area ---
user_input = st.chat_input("Say something")




if user_input:

    print(st.session_state["ai"])
    

    for message in st.session_state["ai"].messages:
        with st.chat_message(message["role"]):
            st.empty().markdown(message["content"])

    st.chat_message("user").markdown(user_input)

    placeholder = st.empty()
    message = ''
    for token in st.session_state["ai"].run_stream(user_input):
        message += token
        placeholder.chat_message("ai").markdown(message, unsafe_allow_html=True)



    # for message in st.session_state["ai"].messages:
    #     placeholder.chat_message(message["role"]).markdown(message["content"])