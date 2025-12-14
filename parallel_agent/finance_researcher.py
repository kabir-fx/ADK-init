from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Finance Researcher: Focuses on fintech trends.
finance_researcher_agent = Agent(
    # A simple name to identify our agent
    name="FinanceResearcher",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    instruction="""Research current fintech trends. Include 3 key trends,
their market implications, and the future outlook. Keep the report concise (100 words).""",

    tools=[google_search],

    # The result of this agent will be stored in the session state with this key.
    output_key="finance_research",
)

print("✅ finance_researcher created.")
