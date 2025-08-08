from agents import Agent

from prompts import SOLUTION_DESIGNER_PROMPT
from schema import SolutionDesignerOutputSchema
from specialized_agents.code_generator_agent import code_generator_agent

solution_designer_agent = Agent(
    name="SolutionDesignerAgent",
    instructions=SOLUTION_DESIGNER_PROMPT,
    output_type=SolutionDesignerOutputSchema,
    handoff_description="This agent create pseudo code and delegate to code_generator_agent to generate code.",
    handoffs=[code_generator_agent],
)