import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st  #import correctly
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI & LangChain API keys (already in  env)
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("Langchain OpenAI Chatbot")
input_text = st.text_input("Enter your question:")

# OpenAI LLM config
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
output_parser = StrOutputParser()

# Chain: Prompt -> LLM -> Output
chain = prompt | llm | output_parser

# When user submits input
if input_text:
    result = chain.invoke({"question": input_text})
    st.write(result)
