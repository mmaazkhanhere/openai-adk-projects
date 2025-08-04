from get_logs import logger
from agents import Agent, Runner
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv

from prompts import ORCHESTRATOR_PROMPT
from schema import EmailWriterResponse

from sub_agents.categorization_agent.agent import categorization_agent
# from sub_agents.specialized_agents.urgent_and_support_request_agent import urgent_and_support_agent
# from sub_agents.specialized_agents.sales_lead_agent import sales_agent
# from sub_agents.specialized_agents.general_agent import general_agent
# from sub_agents.specialized_agents.spam_agent import spam_agent

load_dotenv()


email_automation_agent = Agent(
    name="EmailAutomationAgent",
    instructions=RECOMMENDED_PROMPT_PREFIX + ORCHESTRATOR_PROMPT,
    handoff_description="This agent delegates incoming emails to categorization_agent for classification, then routes to urgent_and_support_agent (Urgent/Support Request), sales_agent (Sales Lead), general_agent (General Inquiry), or spam_agent (Spam) based on the category.",
    handoffs=[categorization_agent],
    output_type=EmailWriterResponse
)

emails: list[dict[str, str]] = [
    {
        "sender": "jane.doe@acmecorp.com",
        "subject": "Critical Issue with Website Downtime",
        "email_content": "Our website has been down since this morning, and customers are complaining they can’t place orders. This is urgent as we’re losing sales every hour. Please help immediately!"
    },
    {
        "sender": "bob.smith@gmail.com",
        "subject": "Question About Account Setup",
        "email_content": "Hi, I’m trying to set up my account but keep getting an error message when I try to verify my email. Can you guide me through the process?"
    },
    {
        "sender": "emma.brown@outlook.com",
        "subject": "Feedback on Your Recent Update",
        "email_content": "I noticed your platform got a new update. It looks great! Can you share more about the new features and how they benefit users?"
    },
    {
        "sender": "alice.johnson@smallbiz.com",
        "subject": "Inquiry About Your Pro Plan",
        "email_content": "We’re a small business looking to upgrade to your Pro Plan. Could you send me details on pricing, features, and any available demos?"
    },
    {
        "sender": "promo@deals4u.com",
        "subject": "You’ve Been Selected for a Free Vacation!",
        "email_content": "Congratulations! You’ve won a free vacation to Hawaii. Click the link below to claim your prize before it expires!"
    },
    # Edge Case 1: Empty email content
    {
        "sender": "john.doe@example.com",
        "subject": "Urgent Help Needed",
        "email_content": ""
    },
    # Edge Case 2: Missing sender
    {
        "sender": "",
        "subject": "General Question",
        "email_content": "Can you tell me more about your software? I’m curious about its features."
    },
    # Edge Case 3: Mixed categories (urgent + sales inquiry)
    {
        "sender": "sarah.lee@techfirm.com",
        "subject": "Urgent: API Issue + Product Inquiry",
        "email_content": "Our API integration is failing, causing delays in our app. Urgent fix needed! Also, can you share details about your enterprise plan?"
    },
    # Edge Case 4: Ambiguous content
    {
        "sender": "mike.wilson@company.com",
        "subject": "Question",
        "email_content": "Hey, just checking in. What’s up with your platform? Need some info."
    },
    # Edge Case 5: Non-standard format (e.g., informal, fragmented)
    {
        "sender": "chris.taylor@yahoo.com",
        "subject": "help!!",
        "email_content": "yo, your app crashed on me. fix it quick. also, how much is it to get the premium version?"
    }
]

for email in emails:
    logger.debug(f"\n##-------------------------------##")
    logger.debug(f"Sender: {email['sender']}")
    logger.debug(f"Subject: {email['subject']}")
    logger.debug(f"Email: {email['email_content']}\n\n")
    result = Runner.run_sync(email_automation_agent, email["email_content"])
    logger.debug(f"Result: {result.final_output}")
    # logger.debug(f"Category: {result.final_output.category.value}\nSummary: {result.final_output.summary}\nPriority: {result.final_output.priority.value}\n")
    logger.debug(f"##-------------------------------##\n")