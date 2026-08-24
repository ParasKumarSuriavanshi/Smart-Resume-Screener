import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import (
    JOB_TITLE,
    JOB_DESCRIPTION,
    REQUIRED_SKILLS,
    PREFERRED_SKILLS,
    MIN_EXPERIENCE
)

from backend.prompts import SYSTEM_PROMPT

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def screen_resume(resume_text: str):

    prompt = ChatPromptTemplate.from_messages([

        (
            "system",
            SYSTEM_PROMPT
        ),

        (
            "human",
            """
            Analyze the following candidate resume against
            the provided job requirements.

            ==============================
            JOB INFORMATION
            ==============================

            Job Title:
            {job_title}

            Job Description:
            {job_description}

            Required Skills:
            {required_skills}

            Preferred Skills:
            {preferred_skills}

            Minimum Experience:
            {min_experience} years


            ==============================
            CANDIDATE RESUME
            ==============================

            {resume_text}


            ==============================
            TASK
            ==============================

            Evaluate the candidate and provide:

            1. Candidate name
            2. Overall score out of 100
            3. Skills score out of 100
            4. Experience score out of 100
            5. Education score out of 100
            6. Project relevance score out of 100
            7. Matched required skills
            8. Missing required skills
            9. Matched preferred skills
            10. Candidate strengths
            11. Candidate weaknesses
            12. Final recommendation
            13. Short justification

            Recommendation must be one of:

            SHORTLIST
            REVIEW
            REJECT
            """
        )
    ])

    chain = prompt | llm

    response = chain.invoke({

        "job_title": JOB_TITLE,

        "job_description":
            JOB_DESCRIPTION,

        "required_skills":
            ", ".join(REQUIRED_SKILLS),

        "preferred_skills":
            ", ".join(PREFERRED_SKILLS),

        "min_experience":
            MIN_EXPERIENCE,

        "resume_text":
            resume_text
    })
    return response.content