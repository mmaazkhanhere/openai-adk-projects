from agents import Agent

from schema import ValidationAgentSchema
from prompts import VALIDATION_AGENT_PROMPT

validation_agent = Agent(
    name="ValidationAgent",
    output_type=ValidationAgentSchema,
    instructions=VALIDATION_AGENT_PROMPT,
    #handoffs=[],
    #handoff_description=""
)