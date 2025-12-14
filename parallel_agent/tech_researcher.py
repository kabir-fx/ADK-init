from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Tech Researcher: Focuses on AI and ML trends.
tech_researcher_agent = Agent(
    # A simple name to identify our agent
    name="TechResearcher",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    

    instruction="""Research the latest AI/ML trends. Include 3 key developments,
the main companies involved, and the potential impact. Keep the report very concise (100 words).""",

    tools=[google_search],

    # The result of this agent will be stored in the session state with this key.
    output_key="tech_research",
)

print("✅ tech_researcher created.")
