import streamlit as st
import asyncio
from agents import Agent, Runner

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

# Define the Project Ideas Generator agent
project_ideas_agent = Agent(
    name="Project Ideas Generator",
    instructions="""
You are a helpful assistant that suggests software project ideas for learners at different skill levels: Beginner, Intermediate, and Advanced.

For each level, provide:
1. A clear project idea with a short description.
2. Key technologies or skills used in the project.
3. Suggestions on how to contribute to related open source projects, including example repositories or communities.
4. A 4-week learning and project roadmap, broken down week-by-week.

Format clearly by level.
"""
)

# Async function to run the agent
async def generate_project_ideas(user_topic):
    return (await Runner.run(project_ideas_agent, user_topic)).final_output

# Streamlit UI
st.set_page_config(page_title="Open source project ideas", layout="centered")
st.title("🚀 Project ideas generator")
st.write("Get software project ideas from beginner to advanced — including open source contribution paths and a 4-week roadmap.")

# Skill level selection
level = st.selectbox("What's your current skill level?", ["Beginner", "Intermediate", "Advanced"])

# Topic input
user_topic = st.text_area(
    "What kind of projects are you interested in?", 
    placeholder="e.g. AI, Web Dev, Finance, or leave blank for general ideas"
)

if st.button("Generate ideas"):
    if user_topic.strip() == "":
        user_topic = f"Generate general {level.lower()} software project ideas."
    else:
        user_topic = f"{level} level project ideas related to: {user_topic}"

    with st.spinner("Generating project ideas and roadmap..."):
        ideas = asyncio.run(generate_project_ideas(user_topic))
        st.success("Here are your project ideas and a 4-week path:")
        st.markdown(ideas)