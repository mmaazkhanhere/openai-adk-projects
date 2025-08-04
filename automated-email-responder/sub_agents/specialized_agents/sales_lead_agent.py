from get_logs import logger
from agents import Agent, function_tool, ModelSettings
from dotenv import load_dotenv

from schema import EmailWriterResponse
from prompts import SALES_LEAD_PROMPT

load_dotenv()

@function_tool
def push_data_to_crm(company_name: str, contact_person: str):
    """Adds a new sales lead to a CRM system.

    This function simulates adding a new lead to a CRM. It is intended to be
    called when an incoming email has been classified as a sales lead. The
    function logs the operation and returns a confirmation message.

    Args:
        company_name: The name of the company associated with the new lead.
        contact_person: The name or email of the contact person for the lead.

    Returns:
        A string message confirming that the data has been pushed to the CRM.
    """
    logger.tool_call("push_data_to_crm", {"company_name": company_name, "contact_person": contact_person}, "")
    """A function that data to crm. It receives company name and contact person as an input args"""
    logger.debug(f"Pushing data to CRM: {company_name}, {contact_person}")
    logger.debug("Data pushed to CRM")
    return "Data pushed to CRM"


sales_agent = Agent(
    name="SalesAgent",
    instructions=SALES_LEAD_PROMPT,
    tools=[push_data_to_crm],
    model_settings=ModelSettings(tool_choice='push_data_to_crm'),
    output_type=EmailWriterResponse
)