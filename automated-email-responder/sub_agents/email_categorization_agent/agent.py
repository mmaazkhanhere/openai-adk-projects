from get_logs import logger
from agents import Agent
from dotenv import load_dotenv

from schema import CategorizationResponse
from sub_agents.email_categorization_agent.sub_agents.categorization_agent import categorization_agent
from sub_agents.email_categorization_agent.sub_agents.router_agent import router_agent

load_dotenv()


email_categorization_agent = Agent(
    name="EmailCategorizationAgent",
    output_type=list[CategorizationResponse],
    handoffs=[categorization_agent, router_agent]
)


