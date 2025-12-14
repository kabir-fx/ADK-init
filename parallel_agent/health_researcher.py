from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Health Researcher: Focuses on medical breakthroughs.
health_researcher_agent = Agent(
    # A simple name to identify our agent
    name="HealthResearcher",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    instruction="""Research recent medical breakthroughs. Include 3 significant advances,
their practical applications, and estimated timelines. Keep the report concise (100 words).""",

    tools=[google_search],

    # The result of this agent will be stored in the session state with this key.
    output_key="health_research",
)

print("✅ health_researcher created.")
