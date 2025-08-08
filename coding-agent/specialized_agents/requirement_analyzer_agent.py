from agents import Agent

from specialized_agents.solution_designer_agent import solution_designer_agent
from schema import AnalyzerAgentOutputSchema
from prompts import ANALYZER_AGENT_PROMPT

requirement_agent = Agent(
    name="RequirementAnalyzerAgent",
    instructions=ANALYZER_AGENT_PROMPT,
    output_type=AnalyzerAgentOutputSchema,
    handoff_description="This agents gets user request as input, create a requirements for the project and delegate to the solution_designer_agent to create pseudo code solution",
    handoffs=[solution_designer_agent],
)