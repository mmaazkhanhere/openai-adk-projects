from get_logs import logger
from agents import Agent
from dotenv import load_dotenv

from schema import CategorizationAgentResponse
from prompts import EMAIL_CATEGORIZATION_PROMPT

load_dotenv()


categorization_agent = Agent(
    name="EmailCategorizationAgent",
    instructions=EMAIL_CATEGORIZATION_PROMPT,
    output_type=CategorizationAgentResponse
)