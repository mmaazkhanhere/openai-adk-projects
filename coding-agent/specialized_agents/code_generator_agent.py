from agents import Agent

from prompts import CODE_GENERATOR_PROMPT
from schema import CodeGeneratorSchema
from specialized_agents.validation_agent import validation_agent

code_generator_agent = Agent(
    name="CodeGeneratorAgent",
    instructions=CODE_GENERATOR_PROMPT,
    #output_type=CodeGeneratorSchema,
    handoffs=[validation_agent],
    handoff_description="Pass the generated code to the agent to validate the code by generating code"
)
