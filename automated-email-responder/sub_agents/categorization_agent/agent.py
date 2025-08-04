from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv

from schema import EmailCategory
from prompts import EMAIL_CATEGORIZATION_PROMPT
from sub_agents.specialized_agents.urgent_and_support_request_agent import urgent_and_support_agent
from sub_agents.specialized_agents.general_agent import general_agent
from sub_agents.specialized_agents.sales_lead_agent import sales_agent
from sub_agents.specialized_agents.spam_agent import spam_agent

load_dotenv()


categorization_agent = Agent(
    name="EmailCategorizationAgent",
    instructions=RECOMMENDED_PROMPT_PREFIX + EMAIL_CATEGORIZATION_PROMPT,
    handoff_description="This agent categorize the email and based on the category handoff to other agents",
    handoffs=[urgent_and_support_agent, sales_agent, general_agent, spam_agent]
)