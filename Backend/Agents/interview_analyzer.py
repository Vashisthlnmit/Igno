from agno.agent import Agent
from typing import List
from agno.models.groq import Groq
from pydantic import BaseModel, Field

# Define the structure for analyzing interview responses
class Feedback(BaseModel):
    question: str = Field(description="Original interview question")
    user_answer: str = Field(description="User's provided answer")
    feedback: str = Field(description="Analysis and feedback on the user's answer")

class Feedback_Set(BaseModel):
    feedback_list: List[Feedback] = Field(description="List of analyzed responses with feedback")

# Define the Interviewer Analyser Agent
Interviewer_Analyser = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an expert interviewer analyzer. Your task is to analyze the user's answer, evaluate correctness, and provide constructive feedback.",
    response_model=Feedback_Set
)

def Interviewer_Analyser_Util(user_responses: List[dict]):
    """
    Analyzes the answers provided by the user and generates feedback.
    
    Parameters:
    user_responses (List[dict]): A list of dictionaries containing interview questions and user answers.
    
    Expected format of user_responses:
    [
        {"question": "What is polymorphism?", "user_answer": "It allows method overriding."},
        {"question": "Explain SQL indexing.", "user_answer": "It speeds up data retrieval."}
    ]
    """
    
    prompt = f"""
    Analyze the following interview responses and provide feedback:
    
    {user_responses}
    
    Your response **must be valid JSON** and follow this structure:
    {{
        "feedback_list": [
            {{
                "question": "Original interview question",
                "user_answer": "User's provided answer",
                "feedback": "Analysis and constructive feedback"
            }}
        ]
    }}
    """
    
    response = Interviewer_Analyser.run(prompt)
    return response.content

class CodeFeedback(BaseModel):
    question: str = Field(description="Original coding problem")
    user_solution: str = Field(description="User's provided solution")
    feedback: str = Field(description="Analysis and feedback on the user's solution")
    correctness: str = Field(description="Evaluation of the correctness of the solution")
    efficiency: str = Field(description="Assessment of the time and space complexity")

class CodeFeedback_Set(BaseModel):
    feedback_list: List[CodeFeedback] = Field(description="List of analyzed coding responses with feedback")

# Define the Coding Evaluator Agent
Code_Evaluator = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an expert coding evaluator. Your task is to analyze the user's solution, evaluate correctness, efficiency, and provide constructive feedback.",
    response_model=CodeFeedback_Set
)

def Coding_Evaluator_Util(user_solutions: List[dict]):
    """
    Evaluates the coding solutions provided by the user and generates feedback.
    
    Parameters:
    user_solutions (List[dict]): A list of dictionaries containing coding problems and user solutions.
    
    Expected format of user_solutions:
    [
        {"question": "Implement binary search.", "user_solution": "def binary_search(arr, x): ..."},
        {"question": "Find the longest palindrome substring.", "user_solution": "def longest_palindrome(s): ..."}
    ]
    """
    
    prompt = f"""
    Analyze the following coding solutions and provide feedback:
    
    {user_solutions}
    
    Your response **must be valid JSON** and follow this structure:
    {{
        "feedback_list": [
            {{
                "question": "Original coding problem",
                "user_solution": "User's provided solution",
                "feedback": "Analysis and constructive feedback",
                "correctness": "Evaluation of the correctness of the solution",
                "efficiency": "Assessment of the time and space complexity"
            }}
        ]
    }}
    """
    
    response = Code_Evaluator.run(prompt)
    return response.content

