# 🧠 AI Resume Analyzer with NLP (No Paid APIs)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://ai-resume-analyzer-bxcchzhgfyee2h8kkyrpd6.streamlit.app/)


A smart AI-powered Resume Analyzer built using Python, spaCy NLP, and PDF parsing — no OpenAI or paid APIs!  
This tool extracts skills from a user's resume and compares them with a job description to calculate skill match %, suggest missing skills, and provide improvement suggestions.

---

## 🚀 Features

- ✅ Upload a resume in PDF format
- ✅ Paste a job description (any role)
- ✅ Extract keywords using spaCy NLP
- ✅ Skill matching using Python sets
- ✅ Calculate and display:
  - Skill match percentage
  - Matched skills
  - Missing skills

---

## 📊 Example Output

Skill Match: 67.89%

✅ Matched Skills:
['html', 'css', 'javascript', 'react', 'git']

❌ Missing Skills:
['aws', 'mongodb', 'ci/cd', 'heroku']


---

## 🧠 Tech Stack

- Python 3.x  
- spaCy NLP (`en_core_web_sm`)  
- PyPDF2 for resume text extraction  
- Google Colab (or Streamlit version coming soon!)

---

## 📁 How to Run

1. Clone the repo or open in [Google Colab](https://colab.research.google.com/)
2. Install dependencies:
!pip install spacy PyPDF2
!python -m spacy download en_core_web_sm

3. Run the notebook and:
- Upload your resume (PDF)
- Paste any job description
4. Get instant AI-based resume feedback 🚀

---

## 💡 Future Enhancements

- Streamlit UI web app
- Grammar checks and formatting suggestions
- Resume keyword tailoring for ATS systems

---

## 🙋‍♀️ About Me

Final year engineering student passionate about AI, NLP, and building real-world career tools.  
Looking for Data, NLP, or AI roles — open to internships and full-time!

