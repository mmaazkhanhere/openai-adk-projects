from get_logs import logger
from agents import Agent
from dotenv import load_dotenv

from schema import EmailWriterResponse
from prompts import EMAIL_WRITER_AGENT

load_dotenv()

email_writer_agent = Agent(
    name="EmailWriterAgent",
    instructions=EMAIL_WRITER_AGENT,
    output_type=EmailWriterResponse,
)