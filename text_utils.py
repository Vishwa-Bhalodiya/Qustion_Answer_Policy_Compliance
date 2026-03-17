import re
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file):
    filename = file.filename.lower()
    
    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    elif filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([para.text for para in doc.paragraphs])
    
    elif filename.endswith(".txt"):
        return file.file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    
def split_paragraphs(text):
    paragraphs = re.split(r'\n\s*\n', text)
    return [ p.strip() for p in paragraphs if p.strip()]