import streamlit as st
import spacy
import PyPDF2
from io import BytesIO

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Extract keywords (noun chunks)
def extract_keywords(text):
    doc = nlp(text)
    return set([chunk.text.strip().lower() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 1])

# Match and calculate % logic
def analyze_match(resume_text, job_description):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords.difference(resume_keywords)
    match_percent = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

    return match_percent, matched, missing

# PDF text extractor
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    # Clean bad characters
    text = text.encode('utf-8', 'ignore').decode('utf-8')
    return text

# Streamlit UI
st.title("📄 AI Resume Analyzer (No Paid APIs)")

st.write("Upload your resume PDF and paste a job description to check skill match.")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste the job description here", height=200)

if st.button("🔍 Analyze Match"):
    if uploaded_file and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)
        match_percent, matched_skills, missing_skills = analyze_match(resume_text, job_description)

        st.success(f"✅ Skill Match: {match_percent:.2f}%")
        st.write("### ✅ Matched Skills:")
        st.write(", ".join(sorted(matched_skills)) if matched_skills else "None")

        st.write("### ❌ Missing Skills (consider adding to resume):")
        st.write(", ".join(sorted(missing_skills)) if missing_skills else "None")
    else:
        st.error("Please upload a resume and paste a job description.")
