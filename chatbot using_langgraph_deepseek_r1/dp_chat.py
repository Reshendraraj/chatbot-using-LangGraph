#from langchain_core.prompts import ChatPromptTemplate
#from langchain_ollama.llms import OllamaLLM
#import streamlit as st

#from langchain.prompts import ChatPromptTemplate  # Fixed import
#from langchain.llms import OllamaLLM 

#st.title("Langchain-Deepseek-R1 app")

#template = """Question:{question}
#Answer :Lets's Think Step by step."""

#prompt = ChatPromptTemplate.from_template(template)

#model = ollamaLLM(model="deepseek-r1")

#chain = prompt|model
#question=st.chat_input("enter your qestion here")
#if question:
#    st.write (chain.invoke({"question":question}))

#from langchain.prompts import ChatPromptTemplate  # Fixed import
#from langchain.llms import OllamaLLM  # Updated import
import streamlit as st

from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain  # Using LLMChain for general LLM usage
from langchain.llms import Ollama 

st.title("Langchain-Deepseek-R1 App")

# Define the prompt template
template = """Question: {question}
Answer: Let's think step by step."""

# Create the prompt from the template
prompt = ChatPromptTemplate.from_template(template)

# Initialize the Ollama model (ensure the model name is correct)
model = Ollama(model="deepseek-r1")

# Set up the chain using the prompt and model
chain = prompt | model

# Streamlit input for the user's question
question = st.text_input("Enter your question here:")

# Display the model's response if the question is provided
if question:
    response = chain.invoke({"question": question})
    st.write(response)
