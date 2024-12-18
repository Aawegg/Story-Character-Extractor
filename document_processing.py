import os
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document
from typing import List

def load_stories(directory: str) -> List[Document]:
    """Load all text documents from a directory."""
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            try:
                loader = TextLoader(os.path.join(directory, filename), encoding="utf-8")
                documents.extend(loader.load())
            except UnicodeDecodeError:
                print(f"Skipping file due to encoding issues: {filename}")
    return documents
