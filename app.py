import streamlit as st
import openai
import os

# Set your OpenAI API key here or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Smart Budget Advisor", page_icon="💸")

st.title("💬 Smart Budget Advisor")
st.write("Ask me anything about budgeting, expenses, savings, or planning your finances.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful financial budgeting assistant that helps users make smart money decisions."}
    ]

# Display past messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_prompt = st.chat_input("How can I help you with your budget?")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # OpenAI Chat Completion
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=st.session_state.messages
        )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
