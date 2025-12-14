from .utils import retry_config

from google.adk.tools import google_search, FunctionTool
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

"""
Now, we need a way for the loop to actually stop based on the critic's feedback. The LoopAgent itself doesn't automatically know that "APPROVED" means "stop."

We need an agent to give it an explicit signal to terminate the loop.

We do this in two parts:
    1. A simple Python function that the LoopAgent understands as an "exit" signal.
    2. An agent that can call that function when the right condition is met.
"""

# This is the function that the RefinerAgent will call to exit the loop.
def exit_loop(tool_context):
    """Call this function ONLY when the critique is 'APPROVED', indicating the story is finished and no more changes are needed."""

    #  Explicitly signal the LoopAgent to stop (escalate)
    if hasattr(tool_context, 'actions'):
        tool_context.actions.escalate = True

    return {
        "status": "approved",
        "message": "Story approved. Exiting refinement loop"
    }
print("✅ exit_loop function created.")

# This agent refines the story based on critique OR calls the exit_loop function.
refiner_agent = Agent(
    # A simple name to identify our agent
    name="RefinerAgent",

    # The specific LLM that will power the agent's reasoning
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    
    # This agent receives the `{blog_draft}` from the writer agent's output.
    instruction="""You are a story refiner. You have a story draft and critique.
    
    Story Draft: {current_story}
    Critique: {critique}
    
    Your task is to analyze the critique.
    - IF the critique is EXACTLY "APPROVED", you MUST call the `exit_loop` function and nothing else.
    - OTHERWISE, rewrite the story draft to fully incorporate the feedback from the critique.""",
    
    # This is the final output of the entire pipeline.
    output_key="current_story",

    tools=[
        FunctionTool(exit_loop)
    ],
)

print("✅ refiner_agent created.")
