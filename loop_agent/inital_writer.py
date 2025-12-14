from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# This agent runs ONCE at the beginning to create the first draft.
initial_writer_agent = Agent(
    # A simple name to identify our agent
    name="InitialWriterAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # The agent's guiding prompt. This tells the agent what its goal is and how to behave.
    instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
    Output only the story text, with no introduction or explanation.""",

    # The result of this agent will be stored in the session state with this key.
    output_key="current_story",
)

print("✅ initial_writer_agent created.")