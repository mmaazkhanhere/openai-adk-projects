from agents import Agent, CodeInterpreterTool

from schema import ValidationAgentSchema
from prompts import VALIDATION_AGENT_PROMPT
from specialized_agents.optimization_agent import optimization_agent

validation_agent = Agent(
    name="ValidationAgent",
    output_type=ValidationAgentSchema,
    instructions=VALIDATION_AGENT_PROMPT,
    tools=[CodeInterpreterTool(tool_config={})],
    handoffs=[optimization_agent],
    handoff_description="This agent create and execute tests and generate feedback. The output is based to optimization_agent to generate optimized code"
)