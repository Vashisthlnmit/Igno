from agno.agent import Agent
from typing import List
from agno.models.groq import Groq
from pydantic import BaseModel,Field
class Question(BaseModel):
    question:str=Field(description="Provide the question")
class Question_Set(BaseModel):
    questions:List[Question]=Field(description="List of questions")
Interviewer = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an expert interviewer. Your task is to generate a set of 15-20 industry-specific questions for a given job role and difficulty level.",
    response_model=Question_Set
)
def Interviewer_Util(job_role: str, difficulty: str):
    prompt = f"""
    Generate exactly 15-20 interview questions for the job role: '{job_role}' at '{difficulty}' difficulty.
    
    Your response **must be valid JSON** and follow this structure:
    {{
        "questions": [
            {{"question": "First interview question?"}},
            {{"question": "Second interview question?"}},
            {{"question": "Third interview question?"}}
        ]
    }}
    """
    response=Interviewer.run(prompt)
    return response.content

def HR_Interviewer(difficulty: str, job_role: str):
    prompt=f"""
    Generate 10-15 HR-specific interview questions with difficulty {difficulty} and job_role {job_role}.
    
    Your response **must be valid JSON** and follow this structure:
    {{
        "questions": [
            {{"question": "First HR-specific question?"}},
            {{"question": "Second HR-specific question?"}},
            {{"question": "Third HR-specific question?"}}
        ]
    }}
    """
    response=Interviewer.run(prompt)
    return response.content
# Competitive-Agent
class Coding_Question(BaseModel):
    question: str = Field(description="Provide a mixed DSA problem")
    example: str = Field(description="Provide an example input-output explanation")
    test_case: List[str] = Field(description="Provide 5-10 test cases")

# Define the structure for multiple coding questions
class Coding_Question_Set(BaseModel):
    questions: List[Coding_Question] = Field(description="List of generated coding questions")

# Define the Competitive Coding Agent
Competitive_Coder = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an expert Competitive Coder. Your task is to generate a set of 3-4 DSA problems with a given difficulty level.",
    response_model=Coding_Question_Set
)

# Function to generate coding questions
def Coding_Round(difficulty: str):
    prompt = f"""
    Generate exactly 3-4 DSA problem statements at '{difficulty}' difficulty level.
    
    Each problem **must** include:
    - A clear **problem statement**
    - A well-explained **example**
    - **5-10 test cases** in a structured format.

    Your response **must be valid JSON** and follow this structure:
    {{
        "questions": [
            {{
                "question": "Problem statement here",
                "example": "Example input and output explanation",
                "test_case": [
                    "Test case 1 input-output",
                    "Test case 2 input-output",
                    "Test case 3 input-output"
                ]
            }},
            {{
                "question": "Second problem statement here",
                "example": "Example input and output explanation",
                "test_case": [
                    "Test case 1 input-output",
                    "Test case 2 input-output"
                ]
            }}
        ]
    }}
    """
    
    response = Competitive_Coder.run(prompt)
    
    return response.content  

# Example usage
resp = Coding_Round("Medium")
print(resp)