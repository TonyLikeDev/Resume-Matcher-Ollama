# Resume Matcher (Ollama Local AI)

This project helps analyze resumes against job descriptions using **local AI (Ollama)**.  
It extracts text from PDF/Images and uses a local LLM (`llama3`) to compare skills, experience, and relevance.  

<img width="553" height="588" alt="Screenshot 2025-09-26 055348" src="https://github.com/user-attachments/assets/79c3ed6c-204b-44b3-b2f3-450edc8221fb" />

## Table of Contents
- [Overview](#resume-matcher-ollama-local-ai)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Notes](#notes-for-create-a-public-server)
- [Future Inprovements](#future-improvements)

## Features
- Upload resume (PDF / PNG / JPG)
- OCR text extraction (via Tesseract for images)
- AI-powered resume critique with improvement suggestions
- Local inference using [Ollama](https://ollama.ai)
- Streamlit web interface

## Tech Stack
- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Sentence Transformers
- Ollama (local LLM inference)

## Setup
#### 1. Clone repo:
   ```bash
   git clone https://github.com/TonyLikeDev/Resume-Matcher-Ollama.git
   cd Resume-Matcher-Ollama
   ```
   
#### 2. Install dependencies:
    pip install -r requirements.txt

#### 3. Install & Run Ollama

  - Download Ollama from Ollama.ai and install it.
  - Then pull the llama3 model:
    ```bash:
    ollama pull llama3
    ```
  - Run the Ollama server (it runs on [ localhost:11434 ]  by default):
    ```bash:
    ollama serve
    ```
#### 4. Run Streamlit app:
    
    streamlit run Resume_Matcher.py
    
## Notes (for create a public server)

Keep your .env file private (create and put file in .gitignore).

Hugging Face / API tokens should never be committed.

If GitHub blocks push due to secrets, clean your history using git filter-repo.

## Future Improvements

Integrate semantic similarity scoring with sentence-transformers.

Add support for multiple resumes vs one job description.

Generate visual graphs of skill matching.

Deploy on cloud with Docker.( On-going )
