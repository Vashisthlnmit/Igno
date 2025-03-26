from pydantic import BaseModel,Field
from typing import List,Optional
from Agents.interview_agent import Question_Set
from Agents.interview_analyzer import Feedback_Set
from bson import ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return str(v)    
class Interview_Question(BaseModel):
    id:Optional[PyObjectId]=Field(alias="_id",default=None)
    email:str=Field(alias="email",default=None)
    type:str=Field("the type of interview")
    difficulty:str=Field("the difficulty of the questions")
    questions:Question_Set=Field("the questions for the interview")
    class Config:
        json_encoders={ObjectId:str}
class InterView_Question_Response(BaseModel):
    id:Optional[PyObjectId]=Field(alias="_id",default=None)
    interview_id:ObjectId
    Question_Answer:List[any]=Field("question and answer of the Question")
    class Config:
        json_encoders={ObjectId:str}
class Interview_Question_Analyser(BaseModel):
    id:Optional[PyObjectId]=Field(alias="_id",default=None)
    interview_id:ObjectId
    FeedBacks:Feedback_Set=Field("the feedbacks for the interview")
    class Config:
        json_encoders={ObjectId:str}
    
