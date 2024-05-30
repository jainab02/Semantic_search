import os
from fastapi import UploadFile
from utils.text_handler import extract_text_from_textfile
from utils.embeddings import embed_text
from elasticsearch import Elasticsearch

# Initialize Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

async def save_file(file: UploadFile):
    file_location = f"samples/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    text = extract_text_from_textfile(file_location)
    embedding = embed_text(text)
    document = {
        "filename": file.filename,
        "content": text,
        "embedding": embedding.tolist()
    }
    es.index(index="documents", document=document)
