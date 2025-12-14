from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Outline Agent: Creates the initial blog post outline
outline_agent = Agent(
    # A simple name to identify our agent
    name="OutlineAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # The agent's guiding prompt. This tells the agent what its goal is and how to behave.
    instruction="""Create a blog outline for the given topic with:
    1. A catchy headline
    2. An introduction hook
    3. 3-5 main sections with 2-3 bullet points for each
    4. A concluding thought""",

    # The result of this agent will be stored in the session state with this key.
    output_key="blog_outline",
)

print("✅ outline_agent created.")