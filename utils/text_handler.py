import re

def extract_text_from_textfile(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return clean_text(text)

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text).strip()
    return text
