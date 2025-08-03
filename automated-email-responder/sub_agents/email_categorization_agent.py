from get_logs import logger
from agents import Agent, Runner
from dotenv import load_dotenv

from prompts import EMAIL_CATEGORIZATION_PROMPT
from schema import EmailCategory

load_dotenv()


categorization_agent = Agent(
    name="EmailCategorizationAgent",
    instructions=EMAIL_CATEGORIZATION_PROMPT,
    output_type=EmailCategory
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
  {
    "subject": "Billing System Error",
    "email": "There’s an issue with your billing system. It’s not processing payments, and our finance team is unable to reconcile accounts. Please fix this ASAP as it’s critical."
  },
  {
    "subject": "How to Export Data from Your Tool",
    "email": "I’m using your analytics tool and need help exporting data to CSV. Can you provide instructions or a tutorial link?"
  },
  {
    "subject": "Curious About Your Services",
    "email": "I came across your website and was curious about what services you offer. Can you send me a brochure or more information?"
  },
  {
    "subject": "Request for Quote",
    "email": "Our company is evaluating CRM solutions, and yours looks promising. Can you provide a quote for 50 users and details on implementation?"
  },
  {
    "subject": "Limited Time Offer: 70% Off!",
    "email": "Don’t miss out! Get 70% off our premium VPN service today. Sign up now to secure your online privacy!"
  },
  {
    "subject": "Quick Question About Your Service",
    "email": "Hi, I’m curious about your platform, but we’re also having an issue where some users can’t log in. Can you clarify features and fix this soon?"
  },
  {
    "subject": "Potential Partnership Opportunity",
    "email": "We’re a startup interested in your AI tools. Our current system is crashing frequently, so we need a solution fast. Can we discuss pricing and integration?"
  },
  {
    "subject": "URGENT: Feedback on Recent Update",
    "email": "Your recent update looks great, but it’s causing some minor glitches in our dashboard. Not a huge deal, but please look into it when you can."
  },
  {
    "subject": "Exclusive Offer for You!",
    "email": "As a valued customer, we’re offering you a free trial of our premium analytics tool. Can you confirm if you’re interested in exploring this for your team?"
  },
  {
    "subject": "Issue with Account – Need Info",
    "email": "I can’t access my account. Also, what are the benefits of upgrading to your premium plan? Please respond quickly, as this is affecting my work."
  }
]

for email in emails:
    logger.debug(f"\n##-------------------------------##")
    logger.debug(f"Subject: {email['subject']}")
    logger.debug(f"Email: {email['email']}\n\n")
    result = Runner.run_sync(categorization_agent, email["email"])
    logger.debug(f"Category: {result.final_output.category.value}\nReason: {result.final_output.reason}")
    logger.debug(f"##-------------------------------##\n")

