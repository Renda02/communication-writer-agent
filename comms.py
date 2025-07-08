import streamlit as st

# Import the 'os' module to interact with the operating system (e.g., environment variables)
import os 

# Import custom classes 'Agent' and 'Runner' from the 'agents' module
from agents import Agent, Runner

# Import the 'asyncio' module to write and manage asynchronous code
import asyncio

# Import 'load_dotenv' from the 'dotenv' package to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from a .env file, allowing them to override existing ones
load_dotenv(override=True)

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Define the Message Rewriter Agent
message_rewriter = Agent(
    name="Communication assistant",
    instructions="""
You are a business communication assistant. Your task is to rewrite technical or engineering-focused messages so they are effective for sales, executives, or other non-technical stakeholders.

Follow these steps:
1. Start with the expected outcome and explain why the work matters. Emphasize business impact before describing technical details.
2. Translate technical or engineering-specific terms into language that resonates with sales teams or CEOs. Include relevant, relatable business-oriented phrasing.
3. Highlight and replace acronyms, jargon, or internal language with plain English or clear explanations.
4. Correct grammar, improve flow, and make the tone direct, friendly, and professional.

Constraints (Never Do):
- Never invent results.
- Never remove essential technical context.
- Never include engineering jargon or unexplained acronyms.
- Never use vague buzzwords or passive language.
- Never include confidential or sensitive information.

Always return only the rewritten message.
"""
)

# Async function to generate the rewritten message
async def generate_message(user_input):
    result = await Runner.run(message_rewriter, user_input)
    return result.final_output

# Streamlit UI
st.set_page_config(page_title="Business Communication Assistant", layout="centered")
st.title("Business communication assistant")
st.write("Turn technical updates into business-ready messages for stakeholders.")

user_input = st.text_area("Enter a technical message", placeholder="e.g. We implemented a low-level TCP socket optimization...")

if st.button("Rewrite message"):
    user_input = user_input.strip()
    
    if not user_input:
        st.warning("Enter a message to rewrite.")
    else:
        with st.spinner("Rewriting your message..."):
            rewritten = asyncio.run(generate_message(user_input))

        st.success("✅ Message successfully rewritten!")

        st.markdown("### 🧪 Original Technical Message")
        st.markdown(f"> {user_input.replace('\n', '\n> ')}")

        st.markdown("### ✅ Business-Friendly Message")
        st.markdown(f"> {rewritten.replace('\n', '\n> ')}")
