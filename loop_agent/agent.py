from .critic import critic_agent
from .inital_writer import initial_writer_agent
from .refiner import refiner_agent
from .utils import retry_config

import asyncio
from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent, SequentialAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool
from os import getenv
from dotenv import load_dotenv

load_dotenv()

try: 
    GOOGLE_API_KEY = getenv("GOOGLE_API_KEY")
    print("✅ Gemini API key setup complete.")

    # The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.
    story_refinement_loop = LoopAgent(
        name="StoryRefinementLoop",
        sub_agents=[critic_agent, refiner_agent],
        
        # Prevents infinite loops
        max_iterations=3
    )

    # The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
    root_agent = SequentialAgent(
        name="StoryPipeline",
        sub_agents=[initial_writer_agent, story_refinement_loop]
    )

    print("✅ Sequential Agent defined.")

except Exception as e:
    print(f"Could not find google: {e}")
