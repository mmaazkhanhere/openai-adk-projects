from agents import Agent

from prompts import CODE_GENERATOR_PROMPT
from schema import CodeGeneratorSchema
from specialized_agents.validation_agent import validation_agent

code_generator_agent = Agent(
    name="CodeGeneratorAgent",
    instructions=CODE_GENERATOR_PROMPT,
    output_type=CodeGeneratorSchema,
    handoffs=[validation_agent],
    handoff_description="Gets pseudo in input and generate code based on that. The generated code is delegated to validation_agent to generate and execute tests to validate the code"
)
