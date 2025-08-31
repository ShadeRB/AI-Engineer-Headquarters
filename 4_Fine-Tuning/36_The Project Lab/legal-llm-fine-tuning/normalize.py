import re
import os

def normalize_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with single space
    text = text.strip()  # Remove leading and trailing whitespace
    chunks = re.split(r'(Article|Section|Clause)\s+\d+', text)
    return chunks

os.makedirs("data/processed/chunks", exist_ok=True)

for file in os.listdir("data/processed"):
    if file.endswith(".txt"):
        with open(f"data/processed/{file}", "r") as f:
            text = f.read()
        chunks = normalize_text(text)
        for i, chunk in enumerate(chunks):
            with open(f"data/processed/chunks/{file}_chunk_{i}.txt", "w") as f:
                f.write(chunk)
            
print("Text normalization and chunking completed.")