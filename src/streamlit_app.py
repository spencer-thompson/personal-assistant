from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time

from gpt import GPT

st.set_page_config(layout="wide")


"""
# Welcome.
"""



if "ai" not in st.session_state:
    st.session_state.ai = GPT()

with st.sidebar:
    gpt4 = st.toggle(label="GPT4")


if gpt4:
    st.session_state.ai.update_model("gpt-4")
else:
    st.session_state.ai.update_model("gpt-3.5-turbo")        
        

prompt = st.chat_input("Say something")
    # if prompt == "hello": # Need to fix auto chat deletion
    #     time.sleep(1)
    #     with st.chat_message("user"):
    #         st.write("Hello 👋")

if prompt:
# PAGES?
    print(st.session_state.ai)
    st.session_state.ai.run(prompt)
    st.session_state.messages = st.session_state.ai.messages



    for message in st.session_state.ai.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# with st.echo(code_location='below'):
# this will give the output of the code below onto the page