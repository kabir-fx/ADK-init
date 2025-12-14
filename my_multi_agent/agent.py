from .editor import editor_agent
from .outline import outline_agent 
from .writer import writer_agent
from .utils import retry_config

import asyncio
from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool
from os import getenv
from dotenv import load_dotenv

load_dotenv()

try: 
    GOOGLE_API_KEY = getenv("GOOGLE_API_KEY")
    print("✅ Gemini API key setup complete.")

    # Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
    root_agent = SequentialAgent(
        name="BlogPipeline",
        sub_agents=[outline_agent, writer_agent, editor_agent]
    )

    print("✅ Sequential Agent defined.")

except Exception as e:
    print(f"Could not find google: {e}")
