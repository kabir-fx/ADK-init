from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# This agent's only job is to provide feedback or the approval signal. It has no tools.
critic_agent = Agent(
    # A simple name to identify our agent
    name="CriticAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # The `{current_story}` placeholder automatically injects the state value from the previous agent's output.
    instruction="""You are a constructive story critic. Review the story provided below.
    Story: {current_story}
    
    Evaluate the story's plot, characters, and pacing.
    - If the story is well-written and complete, you MUST respond with the exact phrase: "APPROVED"
    - Otherwise, provide 2-3 specific, actionable suggestions for improvement.""",

    # The result of this agent will be stored in the session state with this key.
    output_key="critique",
)

print("✅ writer_agent created.")
