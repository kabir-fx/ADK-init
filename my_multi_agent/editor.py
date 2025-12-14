from .utils import retry_config

from google.adk.tools import google_search
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Summarizer Agent: Edits and polishes the draft from the writer agent.
editor_agent = Agent(
    # A simple name to identify our agent
    name="EditorAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # This agent receives the `{blog_draft}` from the writer agent's output.
    instruction="""Edit this draft: {blog_draft}
    Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.""",
     
    # This is the final output of the entire pipeline.
    output_key="final_blog",
)

print("✅ editor_agent created.")
