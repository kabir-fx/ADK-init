import asyncio
from google.genai import types
from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from os import getenv
from dotenv import load_dotenv

load_dotenv()

"""
When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff.
"""
retry_config = types.HttpRetryOptions(
    # Maximum number of attempts, including the original request.
    attempts=5,

    # Multiplier by which the delay increases after each attempt
    exp_base=7,

    # Initial delay before the first retry (in seconds)
    initial_delay=1,

    # List of HTTP status codes that should trigger a retry 
    http_status_codes=[429, 500, 503, 504]
)

try: 
    GOOGLE_API_KEY = getenv("GOOGLE_API_KEY")
    print("✅ Gemini API key setup complete.")

    root_agent = Agent(
        # A simple name and description to identify our agent
        name="helpful_assistant",
        description="A simple agent that can answer general questions.",

        # The specific LLM that will power the agent's reasoning
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config
        ),

        # The agent's guiding prompt. This tells the agent what its goal is and how to behave.
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",

        #  A list of tools that the agent can use.
        tools=[google_search],
    )

    print("✅ Root Agent defined.")

except Exception as e:
    print(f"Could not find google: {e}")


runner = InMemoryRunner(agent=root_agent)
print("✅ Runner created.")
