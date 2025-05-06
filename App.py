import openai
import streamlit as st
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Streamlit UI
st.title("Customer Support Chatbot")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", placeholder="Type your question here...")

# Function to get response from OpenAI
def get_openai_response(messages, model="gpt-3.5-turbo", temperature=0.7):
