from pydantic import BaseModel, Field
from enum import Enum

class Status(Enum):
    VALID = "valid"
    FAILED = "failed"

class TestResult(BaseModel):
    test_case: str = Field(description="The test case that was executed.")
    input: str = Field(description="The input that was used for the test case.")
    expected_output: str = Field(description="The expected output for the test case.")
    actual_output: str = Field(description="The actual output from the code.")
    passed: bool = Field(description="Whether the test case passed or not.")    

class AnalyzerAgentOutputSchema(BaseModel):
    language: str = Field(description="Programming language of the code.")
    main_task: str = Field(description="Main task of the code.")
    sub_tasks: list[str] = Field(description="List of sub tasks of the code.")
    constraints: list[str] = Field(description="Constraints of the code.")
    preferences: list[str] = Field(description="Preferences of the code.")
    clarifications_needed: list[str] = Field(description="List of clarifications needed.")

class CodeGeneratorSchema(BaseModel):
    code: str = Field(description="Generated code.")
    

class ValidationAgentSchema(BaseModel):
    code: str = Field(description="Code to be validated.")
    status: Status = Field(description="Status of the validation.")
    test_results: list[TestResult] = Field(description="List of test results.")
    syntax_check: str = Field(description="Syntax check results.")
    feedback: str = Field(description="Feedback that can be used to optimize the code")

class OptimizedAgentOutput(BaseModel):
    code: str = Field(description="Optimized code.")