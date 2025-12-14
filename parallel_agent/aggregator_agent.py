from .utils import retry_config
from .finance_researcher import finance_researcher_agent
from .health_researcher import health_researcher_agent
from .tech_researcher import tech_researcher_agent

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# The AggregatorAgent runs *after* the parallel step to synthesize the results.
aggregator_agent = Agent(
    # A simple name and description to identify our agent
    name="AggregatorAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""Combine these three research findings into a single executive summary:
**Technology Trends:**
{tech_research}

**Health Breakthroughs:**
{health_research}

**Finance Innovations:**
{finance_research}

Your summary should highlight common themes, surprising connections, and the most important key takeaways from all three reports. The final summary should be around 200 words.""",
    
    # This will be the final output of the entire system.
    output_key="executive_summary",
)

print("✅ aggregator_agent created.")
