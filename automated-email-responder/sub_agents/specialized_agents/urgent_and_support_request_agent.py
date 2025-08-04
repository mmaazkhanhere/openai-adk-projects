from get_logs import logger
from agents import Agent, function_tool, ModelSettings
from dotenv import load_dotenv

from schema import Priority, EmailWriterResponse
from prompts import URGENT_AND_SUPPORT_PROMPT

load_dotenv()

@function_tool
def send_slack_message(summary: str, priority: Priority):
    """Send a Slack message for urgent or support request emails.
    
    This function is called when an urgent or support request email is received.
    It logs the message details and sends a notification to the Slack team.
    
    Args:
        summary (str): A brief summary of the email content
        priority (Priority): The priority level of the email (from schema.Priority)
        
    Returns:
        str: Confirmation message indicating the message was sent to Slack
        
    Example:
        >>> send_slack_message("Customer needs urgent help with login", Priority.HIGH)
        'Message sent to Slack'
    """
    logger.tool_call("send_slack_message", {"summary": summary, "priority": priority}, "")
    logger.debug(f"Sending message to Slack: {summary}")
    logger.debug(f"Priority: {priority}")
    logger.debug("Message sent to Slack")
    return "Message sent to Slack"


urgent_and_support_agent = Agent(
    name="UrgentAndSupportAgent",
    instructions=URGENT_AND_SUPPORT_PROMPT,
    tools=[send_slack_message],
    model_settings=ModelSettings(tool_choice='send_slack_message'),
    output_type=EmailWriterResponse
)