from get_logs import logger
from agents import Agent, function_tool
from dotenv import load_dotenv

from schema import AgentResponse, Priority
from prompts import ROUTER_AGENT_PROMPT

load_dotenv()

@function_tool
def send_slack_message(summary: str, priority: Priority):
    """A function that is called when urgent or support request email is received. It receives summary and priority and it is send to slack team"""
    logger.tool_call("send_slack_message", {"summary": summary, "priority": priority}, "")
    logger.debug(f"Sending message to Slack: {summary}")
    logger.debug(f"Priority: {priority}")
    logger.debug("Message sent to Slack")
    return "Message sent to Slack"

@function_tool
def push_data_to_crm(company_name: str, contact_person: str):
    """A function that is called when email is of category sales lead. It extracts company name and contact person from email and add it to CRM"""
    logger.tool_call("push_data_to_crm", {"company_name": company_name, "contact_person": contact_person}, "")
    """A function that data to crm. It receives company name and contact person as an input args"""
    logger.debug(f"Pushing data to CRM: {company_name}, {contact_person}")
    logger.debug("Data pushed to CRM")
    return "Data pushed to CRM"

@function_tool
def query_knowledge_base(query: str):
    logger.tool_call("query_knowledge_base", {"query": query}, "")
    """A function that queries the knowledge base. It receives query as an input argument that is searched through knowledge base to get the answer"""
    knowledge_base = [
        {
            "question": "How do I reset my password?",
            "answer": "To reset your password, go to the login page and click on 'Forgot Password'. Enter your registered email address, and a password reset link will be sent to you."
        },
        {
            "question": "What are your business hours?",
            "answer": "Our customer support is available Monday to Friday, from 9:00 AM to 5:00 PM EST. Our online services are available 24/7."
        },
        {
            "question": "How can I contact customer support?",
            "answer": "You can reach our customer support team via email at support@example.com, or by calling us at +1-800-555-0199 during business hours."
        },
        {
            "question": "What payment methods do you accept?",
            "answer": "We accept major credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers for our services."
        },
        {
            "question": "How long does shipping take?",
            "answer": "Standard shipping within the continental US typically takes 3-5 business days. International shipping times vary depending on the destination, usually between 7-21 business days."
        },
        {
            "question": "Can I cancel my subscription?",
            "answer": "Yes, you can cancel your subscription at any time by logging into your account settings and navigating to the 'Subscription' section. Follow the prompts to cancel."
        },
        {
            "question": "Do you offer refunds?",
            "answer": "Our refund policy allows for full refunds within 30 days of purchase if you are not satisfied with our product or service. Please refer to our terms and conditions for more details."
        },
        {
            "question": "Where can I find product documentation?",
            "answer": "All product documentation, including user manuals and FAQs, can be found in the 'Support' or 'Documentation' section of our website."
        },
        {
            "question": "Is there a free trial available?",
            "answer": "Yes, we offer a 14-day free trial for all new users. No credit card is required to start your trial."
        },
        {
            "question": "How do I update my billing information?",
            "answer": "To update your billing information, log in to your account, go to 'Account Settings', and then select 'Billing Information' to make changes."
        }
    ]
    for item in knowledge_base:
        if item["question"].lower() in query.lower():
            logger.debug(f"Querying knowledge base: {query}")
            logger.debug("Knowledge base queried")
            return item["answer"]
        else:
            logger.debug(f"Querying knowledge base: {query}")
            logger.debug("Knowledge base queried")
            return "No answer found in knowledge base. Escalating to another agent for email response drafting."

router_agent = Agent(
    name="RouterAgent",
    instructions=ROUTER_AGENT_PROMPT,
    tools=[send_slack_message, push_data_to_crm, query_knowledge_base],
    output_type=AgentResponse,
)