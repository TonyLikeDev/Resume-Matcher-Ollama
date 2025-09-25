Resume Matcher (Ollama Local AI)

This project helps analyze resumes against job descriptions using **local AI (Ollama)**.  
It extracts text from PDF/Images and uses a local LLM (`llama3`) to compare skills, experience, and relevance.  

Features
- Upload resume (PDF / PNG / JPG)
- OCR text extraction (via Tesseract for images)
- AI-powered resume critique with improvement suggestions
- Local inference using [Ollama](https://ollama.ai)
- Streamlit web interface

Tech Stack
- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Sentence Transformers
- Ollama (local LLM inference)

Setup
1. Clone repo:
   ```bash
   git clone https://github.com/TonyLikeDev/Resume-Matcher-Ollama.git
   cd Resume-Matcher-Ollama
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Install & Run Ollama

  - Download Ollama from Ollama.ai and install it.
  - Then pull the llama3 model:
    ```bash:
    ollama pull llama3
  - Run the Ollama server (it runs on [ localhost:11434 ]  by default):
    ```bash:
    ollama serve
4. Run Streamlit app:
    ```
    streamlit run Resume_Matcher.py
