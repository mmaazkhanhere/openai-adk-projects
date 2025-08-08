from agents import Agent

from prompts import SOLUTION_DESIGNER_PROMPT

solution_designer_agent = Agent(
    name="SolutionDesignerAgent",
    instructions=SOLUTION_DESIGNER_PROMPT,
    #handoff_description="Transfer to agent when you need to design system architecture, create technical specifications, or plan solution approaches for complex problems.",
    #handoffs=[],
)