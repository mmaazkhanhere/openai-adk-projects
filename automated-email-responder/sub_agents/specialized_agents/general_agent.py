from get_logs import logger
from agents import Agent, function_tool, ModelSettings
from dotenv import load_dotenv

from schema import EmailWriterResponse
from prompts import GENERAL_INQUIRY_PROMPT

load_dotenv()

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


general_agent = Agent(
    name="GeneralInquiryAgent",
    instructions=GENERAL_INQUIRY_PROMPT,
    tools=[query_knowledge_base],
    model_settings=ModelSettings(tool_choice='query_knowledge_base'),
    output_type=EmailWriterResponse
)