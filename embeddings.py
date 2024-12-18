from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from document_processing import load_stories
from utils import get_api_key
import os
api_key = os.getenv("MISTRAL_API_KEY", "your-mistral-api-key")

import os

def compute_embeddings(dataset_path: str):
    """Load stories, split text, and compute embeddings."""
    api_key = get_api_key("MISTRAL_API_KEY")

    # Load documents
    documents = load_stories(dataset_path)
    if not documents:
        raise ValueError("No documents found in the specified directory.")

    # Initialize embeddings
    embeddings = MistralAIEmbeddings(model="mistral-embed", api_key=api_key)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    # Create and persist vector database
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./story_embeddings"
    )
    print("Embeddings computed and stored successfully.")
