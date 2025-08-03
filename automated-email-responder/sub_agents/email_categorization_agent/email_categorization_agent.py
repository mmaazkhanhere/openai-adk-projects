from get_logs import logger
from agents import Agent, Runner
from dotenv import load_dotenv

from prompts import EMAIL_CATEGORIZATION_PROMPT
from schema import AgentResponse
from sub_agents.urgent_and_support_agent import urgent_and_support_agent

load_dotenv()


categorization_agent = Agent(
    name="EmailCategorizationAgent",
    # instructions=EMAIL_CATEGORIZATION_PROMPT,
    output_type=AgentResponse,
    handoffs=[urgent_and_support_agent]
)


emails: list[dict[str, str]] = [
  {
    "subject": "Critical Issue with Website Downtime",
    "email": "Our website has been down since this morning, and customers are complaining they can’t place orders. This is urgent as we’re losing sales every hour. Please help immediately!"
  },
  {
    "subject": "Question About Account Setup",
    "email": "Hi, I’m trying to set up my account but keep getting an error message when I try to verify my email. Can you guide me through the process?"
  },
  {
    "subject": "Feedback on Your Recent Update",
    "email": "I noticed your platform got a new update. It looks great! Can you share more about the new features and how they benefit users?"
  },
  {
    "subject": "Inquiry About Your Pro Plan",
    "email": "We’re a small business looking to upgrade to your Pro Plan. Could you send me details on pricing, features, and any available demos?"
  },
  {
    "subject": "You’ve Been Selected for a Free Vacation!",
    "email": "Congratulations! You’ve won a free vacation to Hawaii. Click the link below to claim your prize before it expires!"
  },
]

for email in emails:
    logger.debug(f"\n##-------------------------------##")
    logger.debug(f"Subject: {email['subject']}")
    logger.debug(f"Email: {email['email']}\n\n")
    result = Runner.run_sync(categorization_agent, email["email"])
    logger.debug(f"Category: {result.final_output.category.value}\nSummary: {result.final_output.summary}\nPriority: {result.final_output.priority.value}\n")
    logger.debug(f"##-------------------------------##\n")

