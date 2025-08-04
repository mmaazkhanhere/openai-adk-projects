from agents import Agent
from dotenv import load_dotenv

from schema import EmailWriterResponse
from prompts import SPAM_PROMPT

load_dotenv()


spam_agent = Agent(
    name="SpamAgent",
    instructions=SPAM_PROMPT,
    output_type=EmailWriterResponse
)