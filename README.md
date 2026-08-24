# Smart Resume Screener 🤖📄

An **AI-powered Resume Screening System** that automatically analyzes candidate resumes and evaluates their suitability for a specific job position.

The project is designed to help recruiters and HR teams quickly screen resumes based on required and preferred skills, reducing the time spent on manual resume evaluation.

---

## 🚀 Features

* 📄 Upload resumes in **PDF** or **TXT** format
* 📝 Paste resume text directly into the application
* 🤖 AI-powered resume analysis
* 🔍 Extracts and evaluates candidate skills
* 🎯 Compares resume information with job requirements
* 📊 Provides a screening result and recommendation
* 🐍 Python-based backend using **FastAPI**
* 🌐 Simple and responsive HTML/CSS frontend
* ⚡ Real-time communication between frontend and backend
* 🔐 `.env` support for storing API keys and sensitive configuration

---

## 💼 Job Position

The current version of the application screens candidates for:

### Python + AI Developer

**Required Skills:**

* Python
* SQL
* REST APIs
* FastAPI
* Git

**Preferred Skills:**

* LangChain
* LangGraph
* Machine Learning
* Docker

The job requirements can be modified according to the position being screened.

---

## 🏗️ Project Structure

```text
Smart-Resume-Screener/
│
├── backend/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── style.css
│
├── resumes/
│   └── sample_resume.pdf
│
├── .gitignore
├── README.md
└── requirements.txt
```

> The exact file structure may vary depending on your implementation.

---

## 🛠️ Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Backend development            |
| FastAPI            | REST API                       |
| HTML               | Frontend structure             |
| CSS                | Frontend styling               |
| JavaScript         | Frontend-backend communication |
| AI/LLM             | Resume analysis                |
| PDF/TXT Processing | Resume extraction              |
| Git & GitHub       | Version control                |

---

## ⚙️ How It Works

The application follows these basic steps:

```text
Candidate Resume
       ↓
Upload PDF / TXT
       ↓
FastAPI Backend
       ↓
Resume Text Extraction
       ↓
AI Resume Analysis
       ↓
Compare with Job Requirements
       ↓
Generate Screening Result
       ↓
Display Result on Website
```

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-resume-screener.git
```

Move into the project directory:

```bash
cd smart-resume-screener
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the backend/project directory.

Example:

```env
API_KEY=your_api_key_here
```

Do **not** upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
```

---

## ▶️ Running the Application

### Start the FastAPI Backend

From the backend directory, run:

```bash
uvicorn main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

---

### Open the Frontend

Open:

```text
frontend/index.html
```

in your browser.

The frontend sends the resume to the FastAPI `/screen` endpoint:

```text
POST /screen
```

---

## 📤 Using the Application

1. Open the Smart Resume Screener webpage.
2. Select the **Python + AI Developer** job position.
3. Upload a resume in PDF/TXT format **or** paste resume text.
4. Click **Start Screening**.
5. The resume is sent to the FastAPI backend.
6. The AI analyzes the candidate's resume.
7. The screening result is displayed on the webpage.

---

## 📊 Example Screening Output

The system can provide information such as:

```text
Candidate: John Doe

Overall Score: 85

Recommendation: Selected

Matched Skills:
- Python
- SQL
- FastAPI
- Git
- Machine Learning

Missing Skills:
- Docker
- LangGraph

Strengths:
- Strong Python programming experience
- Backend development experience
- Experience working with REST APIs

Areas to Improve:
- Limited Docker experience
- No significant LangGraph experience
```

The exact output depends on the AI model and backend implementation.

---

## 🔌 API Endpoint

### Screen Resume

**Endpoint:**

```text
POST /screen
```

**Request:**

The endpoint accepts multipart form data containing:

```text
file
resume_text
```

Example frontend request:

```javascript
const formData = new FormData();

formData.append("file", file);
formData.append("resume_text", resumeText);

const response = await fetch(
    "http://127.0.0.1:8000/screen",
    {
        method: "POST",
        body: formData
    }
);
```

---

## 🔒 Security

* Keep API keys inside `.env`.
* Never commit `.env` to GitHub.
* Do not expose private API credentials in frontend JavaScript.
* Validate uploaded files before processing them.
* Limit the allowed resume file types and sizes in production.

---

## 🔮 Future Improvements

Some possible improvements include:

* 📊 Resume ranking dashboard
* 👥 Multiple candidate comparison
* 🧠 Improved AI-based skill extraction
* 📈 Candidate scoring visualization
* 📑 Automatic resume parsing
* 🗂️ Candidate database
* 🔐 User authentication
* 📥 Export screening reports as PDF
* 🐳 Docker deployment
* ☁️ Cloud deployment
* 🎯 Support for multiple job descriptions
* 📧 Automated candidate notification
* 📝 Interview question generation based on the resume

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Create a Pull Request.

---

## 📄 License

This project is created for educational and development purposes.

You can add a specific license such as **MIT License** if you decide to open-source the project.

---

## 🎥 Demo Video

Watch the project demonstration here:

**Demo Video:** [Add your demo video link here]

> Replace the link above with your YouTube, Google Drive, or other publicly accessible demo video URL.

---

## 👨‍💻 Author

**Your Name**

GitHub: [Add your GitHub profile link]

LinkedIn: [Add your LinkedIn profile link]

---

⭐ If you find this project useful, consider giving the repository a star!
