from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import fitz


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Smart Resume Screener API is running"
    }


@app.post("/screen")
async def screen_resume(
    file: UploadFile | None = File(None),
    resume_text: str | None = Form(None)
):

    if resume_text and resume_text.strip():

        text = resume_text.strip()

        return {
            "input_type": "text",
            "filename": None,
            "resume_text": text
        }


    if file:

        filename = file.filename

        # Read uploaded file into Python
        file_bytes = await file.read()

        if filename.lower().endswith(".pdf"):

            pdf = fitz.open(
                stream=file_bytes,
                filetype="pdf"
            )

            text = ""

            for page in pdf:

                text += page.get_text()


            pdf.close()

            return {
                "input_type": "pdf",
                "filename": filename,
                "resume_text": text
            }

        elif filename.lower().endswith(".txt"):

            text = file_bytes.decode(
                "utf-8",
                errors="ignore"
            )

            return {
                "input_type": "txt",
                "filename": filename,
                "resume_text": text
            }

        else:

            return {
                "error": "Only PDF and TXT files are supported."
            }

    return {
        "error": "Please upload a resume or enter resume text."
    }