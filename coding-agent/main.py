from agents import Agent, Runner
from dotenv import load_dotenv

from prompts import CODING_AGENT_PROMPT
from schema import CodeGeneratorSchema
from specialized_agents.requirement_analyzer_agent import requirement_agent
# from specialized_agents.solution_designer_agent import solution_designer_agent
# from specialized_agents.code_generator_agent import code_generator_agent

from get_logs import logger

load_dotenv()

coding_agent = Agent(
    name="CodingAgent",
    instructions=CODING_AGENT_PROMPT,
    handoff_description="Main coding agent that analyzes requests and coordinates with specialized agents for specific tasks.",
    handoffs=[requirement_agent],
    output_type=CodeGeneratorSchema
)

result = Runner.run_sync(coding_agent, "Create a function to sort numbers.")

logger.info(result.final_output)