import os
from datasets import load_dataset
import requests
import PyPDF2
from docx import Document

os.makedirs("data/raw", exist_ok=True)

cuad = load_dataset("theatticusproject/cuad", ignore_verifications=True)
cuad.save_to_disk("data/raw/cuad")

urls = [
    "https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf",
    "https://oag.ca.gov/privacy/ccpa"
]

for url in urls:
    response = requests.get(url)
    with open(f"data/raw/{os.path.basename(url)}", "wb") as f:
        f.write(response.content)
    
print("Data download completed.")

def ingest_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def ingest_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

for file in os.listdir("data/raw"):
    if file.endswith(".pdf"):
        text = ingest_pdf(f"data/raw/{file}")
        with open(f"data/processed/{file}.txt", "w") as f:
            f.write(text)
    
