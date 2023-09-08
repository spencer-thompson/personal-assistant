from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time

from gpt import GPT

"""
# Welcome.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

ai = GPT()

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User: {prompt}") 
    st.chat_message("user", prompt)
    # if prompt == "hello": # Need to fix auto chat deletion
    #     time.sleep(1)
    #     with st.chat_message("user"):
    #         st.write("Hello 👋")

# PAGES?
st.sidebar.markdown("# Main page 🎈")

ai.run(prompt)
st.session_state.messages = ai.messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# with st.echo(code_location='below'):
# this will give the output of the code below onto the page