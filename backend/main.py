from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import json
from backend.llm_screener import screen_resume
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
async def screen_resume_api(
    file: UploadFile | None = File(None),
    resume_text: str | None = Form(None)
):

    try:

        text = ""

        # -------------------------------
        # Pasted resume
        # -------------------------------

        if resume_text and resume_text.strip():

            text = resume_text.strip()


        # -------------------------------
        # Uploaded file
        # -------------------------------

        elif file:

            filename = file.filename

            file_bytes = await file.read()


            if filename.lower().endswith(".pdf"):

                pdf = fitz.open(
                    stream=file_bytes,
                    filetype="pdf"
                )

                for page in pdf:
                    text += page.get_text()

                pdf.close()


            elif filename.lower().endswith(".txt"):

                text = file_bytes.decode(
                    "utf-8",
                    errors="ignore"
                )


            else:

                return {
                    "error": "Only PDF and TXT files are supported."
                }


        else:

            return {
                "error": "Please upload a resume or paste resume text."
            }


        # -------------------------------
        # Check text
        # -------------------------------

        if not text.strip():

            return {
                "error": "No resume text found."
            }


        print("\n==============================")
        print("RESUME RECEIVED")
        print("==============================")
        print(text[:500])
        print("==============================\n")


        # -------------------------------
        # Call LLM
        # -------------------------------

        print("Calling LLM...")

        result = screen_resume(text)

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError:
            result_json = {
                "raw_result": result
            }

        print("LLM RESPONSE RECEIVED")


        return {
            "resume_text": text,
            "screening_result": result
        }


    except Exception as e:

        print("\n==============================")
        print("ERROR")
        print("==============================")
        print(type(e).__name__)
        print(str(e))
        print("==============================\n")

        return {
            "error": f"{type(e).__name__}: {str(e)}"
        }