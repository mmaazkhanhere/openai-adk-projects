from pydantic import BaseModel, Field, ConfigDict

class AnalyzerAgentOutputSchema(BaseModel):
    language: str = Field(description="Programming language of the code.")
    main_task: str = Field(description="Main task of the code.")
    sub_tasks: list[str] = Field(description="List of sub tasks of the code.")
    constraints: list[str] = Field(description="Constraints of the code.")
    preferences: list[str] = Field(description="Preferences of the code.")
    clarifications_needed: list[str] = Field(description="List of clarifications needed.")

    

    