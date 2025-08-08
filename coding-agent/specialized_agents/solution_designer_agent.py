from agents import Agent

from prompts import SOLUTION_DESIGNER_PROMPT
from specialized_agents.code_generator_agent import code_generator_agent

solution_designer_agent = Agent(
    name="SolutionDesignerAgent",
    instructions=SOLUTION_DESIGNER_PROMPT,
    handoff_description="Transfer to agent when generating code based on the pseudo code generated.",
    handoffs=[code_generator_agent],
)