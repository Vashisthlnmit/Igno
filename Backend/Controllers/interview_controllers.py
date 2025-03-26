from Database.Connection import db
from Agents import interview_agent
from Agents import interview_analyzer
from bson import ObjectId
from Database.Schemas import Interview_Question,Interview_Question_Analyser
## Create a Interview
def create_interview(data):
    try:
        job_role=data.get("job_role")
        difficulty=data.get("difficulty")
        type=data.get("type")
        questions=[]
        if type.lower()=="HR":
            questions=interview_agent.HR_Interviewer(job_role=job_role,difficulty=difficulty)
            if len(questions)==0:  
                return {"error":"Error while creating HR interpreter"}
        else:
            questions=interview_agent.Interviewer_Util(job_role=job_role,difficulty=difficulty)
            if len(questions)==0:
                return {"error":"Error while creating Interviewer"}
        interview_data={"email":data.get("email"),"type":type,"difficulty":difficulty,"questions":questions}
        interview_data_validation=Interview_Question(**interview_data)
        interview_id=db.interviews.insert_one(interview_data_validation.model_dump(by_alias=True)).inserted_id
        return {"message":"interview created successfully","id":str(interview_id)},201
    except Exception as e:
        return {"error":str(e)}
def answer_saver(data):
    try:
        interview_data={"interview_id":ObjectId(data.get("interview_id")),"Question_Answer":data.get("Question_Answer")}
        interview_data_validation=Interview_Question(**interview_data)
        interview_answer_id=db.interview_response.insert_one(interview_data_validation.model_dump(by_alias=True)).inserted_id
        return {"messages":"interview_response submitted successfully","id":str(interview_answer_id)},201
    except Exception as e:
        return {"error":str(e)}    
    
