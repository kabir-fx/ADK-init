from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Writer Agent: Writes the full blog post based on the outline from the previous agent.
writer_agent = Agent(
    # A simple name to identify our agent
    name="WriterAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # The `{blog_outline}` placeholder automatically injects the state value from the previous agent's output.
    instruction="""Following this outline strictly: {blog_outline}
    Write a brief, 200 to 300-word blog post with an engaging and informative tone.""",

    # The result of this agent will be stored in the session state with this key.
    output_key="blog_draft",
)

print("✅ writer_agent created.")
