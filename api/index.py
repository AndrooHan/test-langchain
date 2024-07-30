import os

from flask import Flask
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor

app = Flask(__name__)

@app.route('/')
def home():
    agent = AgentExecutor(agent=None, tools=[], verbose=True)
    llm = OpenAI(temperature=0.9)
    text = "What would be a good company name a company that makes colorful socks?"

    return llm(text)
