from flask import Flask
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
import os

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)

@app.route("/")
def hello():
    llm = OpenAI(temperature=.7)
    template = """You are a teacher in physics for High School student. Given the text of question, it is your job to write a answer that question with example.
    Question: {text}
    Answer:
    """
    prompt_template = PromptTemplate(input_variables=["text"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run("What is the formula for Gravitational Potential Energy (GPE)?")
    return answer
