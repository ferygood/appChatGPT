import os
import openai
import streamlit as st
import time
from myGPT.askGPT import askGPT

# 1. Get openai_api_key from environment
# set your environment api key, tutorial: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
openai.api_key = os.environ["OPENAI_API_KEY"]

# 2. display almost everything using st.write
st.write("""
# appChatGPT
""")

# text elements
st.title("Introduction")
st.caption("""
appChatGPT is a software that provide user interface and can allow user 
to ask their question to ChatGPT and receive response.
""")

# 3. get user input string to ChatGPT
question = st.text_area(
    "Please type your question below :point_down:",
    "What is Love?",
)

answer = askGPT(question)

answer

# download your question and answer from ChatGPT
text_contents = f"Q: {question} \nA: {answer}"
st.download_button("Download", text_contents)

