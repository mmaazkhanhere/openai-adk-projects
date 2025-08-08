from agents import Agent

from schema import AnalyzerAgentOutputSchema
from prompts import ANALYZER_AGENT_PROMPT

requirement_agent = Agent(
    name="RequirementAnalyzerAgent",
    instructions=ANALYZER_AGENT_PROMPT,
    output_type=AnalyzerAgentOutputSchema,
    #handoff_description="",
    #handoffs=[],
)