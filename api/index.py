import os

from flask import Flask
from langchain.llms import OpenAI
from langchain.agents import create_json_chat_agent 

app = Flask(__name__)

@app.route('/')
def home():
    agent = create_json_chat_agent(None, [], prompt=None)
    llm = OpenAI(temperature=0.9)
    text = "What would be a good company name a company that makes colorful socks?"

    return llm(text)
