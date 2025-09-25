import os
import re
import fitz  # PyMuPDF for PDF text extraction
import pytesseract
from PIL import Image
import streamlit as st
import requests
from sentence_transformers import SentenceTransformer, util

# -----------------------------
# Ollama Inference API (local)
# -----------------------------
def ollama_inference(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"  # ✅ correct endpoint
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        if response.status_code != 200:
            return f"⚠️ Ollama error {response.status_code}: {response.text}"
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"⚠️ Ollama request failed: {e}"


# -----------------------------
# Resume Text Extraction
# -----------------------------
def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        file.seek(0)  # 🔧 reset cursor
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf:
            text += page.get_text()
    elif file.type in ["image/png", "image/jpeg", "image/jpg"]:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    return text


# -----------------------------
# AI Resume Critique (via Ollama, fallback if fails)
# -----------------------------
def improve_resume_ai(resume_text, job_desc):
    prompt = f"""

Show the matching between the resume and job description by percentage and keyword, highlighting key skills and experiences that align well. Provide a summary of the overall fit for the role based on the analysis.
    
    
You are an experienced career coach specializing in resume and job description analysis. Review the provided resume and compare it against the given job description. Point out the part that was Good and Identify and explain any weaknesses, missing skills, and gaps in relevant experience. Suggest specific, actionable improvements, including example bullet points that illustrate how these changes could be reflected on the resume.
Provide a concise summary of the overall fit for the role based on your analysis.
show some link + url to relevant resources for further reading or course.
show tips if needed.

Resume:
{resume_text[:2000]}

Job Description:
{job_desc}
"""
    result = ollama_inference(prompt, model="llama3")
    if result.startswith("⚠️"):  # fallback if Ollama not available
        return (
            "⚠️ Ollama not available. Using fallback analysis.\n\n"
            
        )
    return result

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Resume Matcher", page_icon="📑", layout="centered")
st.title("📑 Resume Matcher (Ollama Local AI) cause i dont have moni")

resume_file = st.file_uploader(
    "Upload Resume (PDF/Image)",
    type=["pdf", "png", "jpeg", "jpg"],
    accept_multiple_files=False,
    key="resume_uploader",
)

job_desc = st.text_area("Paste Job Description")

analyze_button = st.button("🔍 Analyze")

if resume_file and job_desc and analyze_button:
    resume_text = extract_text(resume_file)
    if not resume_text.strip():
        st.error("❌ Could not extract text from resume. Please try a different file.")
    else:
        with st.spinner("Analyzing resume..."):
            
            
            # Debug info
            st.info(f"🔎 Debug: Resume length = {len(resume_text)} chars")

            # AI critique
            suggestions = improve_resume_ai(resume_text, job_desc)
            st.markdown("## 📝 Detailed Analysis")
            if suggestions.startswith("⚠️"):
                st.warning(suggestions)
            else:
                st.markdown(suggestions)
