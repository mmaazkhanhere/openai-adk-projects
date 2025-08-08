from agents import Agent, CodeInterpreterTool

from schema import OptimizedAgentOutput
from prompts import OPTIMIZER_AGENT_PROMPT  

optimization_agent = Agent(
    name="OptimizedAgent",
    instructions=OPTIMIZER_AGENT_PROMPT,
    output_type=OptimizedAgentOutput,
    tools=[CodeInterpreterTool(tool_config={})]
)