from agents import Agent, Runner
from dotenv import load_dotenv

from prompts import CODING_AGENT_PROMPT
from schema import OptimizedAgentOutput
from specialized_agents.requirement_analyzer_agent import requirement_agent
# from specialized_agents.solution_designer_agent import solution_designer_agent
# from specialized_agents.code_generator_agent import code_generator_agent

from get_logs import logger

load_dotenv()

coding_agent = Agent(
    name="CodingAgent",
    instructions=CODING_AGENT_PROMPT,
    handoff_description="THe main agent that takes user request and delegates it to requirement_agent for getting requirements detail",
    handoffs=[requirement_agent],
    output_type=OptimizedAgentOutput
)

result = Runner.run_sync(coding_agent, "Create a function to sort numbers.")

logger.info(result)