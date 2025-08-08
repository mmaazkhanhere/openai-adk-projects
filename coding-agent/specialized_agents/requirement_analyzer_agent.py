from agents import Agent

from specialized_agents.solution_designer_agent import solution_designer_agent
from schema import AnalyzerAgentOutputSchema
from prompts import ANALYZER_AGENT_PROMPT

requirement_agent = Agent(
    name="RequirementAnalyzerAgent",
    instructions=ANALYZER_AGENT_PROMPT,
    output_type=AnalyzerAgentOutputSchema,
    handoff_description="Analyzes user requirements and passes structured analysis to solution designer for technical implementation planning",
    handoffs=[solution_designer_agent],
)