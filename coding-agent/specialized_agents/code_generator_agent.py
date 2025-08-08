from agents import Agent

from prompts import CODE_GENERATOR_PROMPT
from schema import CodeGeneratorSchema

code_generator_agent = Agent(
    name="CodeGeneratorAgent",
    instructions=CODE_GENERATOR_PROMPT,
    output_type=CodeGeneratorSchema,
)
