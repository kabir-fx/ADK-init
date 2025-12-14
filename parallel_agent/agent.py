from .finance_researcher import finance_researcher_agent
from .health_researcher import health_researcher_agent
from .tech_researcher import tech_researcher_agent
from .aggregator_agent import aggregator_agent

import asyncio
from google.genai import types
from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from os import getenv
from dotenv import load_dotenv

load_dotenv()

try: 
    GOOGLE_API_KEY = getenv("GOOGLE_API_KEY")
    print("✅ Gemini API key setup complete.")

    parallel_agent = ParallelAgent(
        name="ParallelResearchTeam",
        sub_agents=[tech_researcher_agent, finance_researcher_agent, health_researcher_agent]
    )

    # This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
    root_agent = SequentialAgent(
        name="ResearchSystem",
        sub_agents=[parallel_agent, aggregator_agent]
    )

    print("✅ Parallel & Root Agents defined.")

except Exception as e:
    print(f"Could not find google: {e}")
