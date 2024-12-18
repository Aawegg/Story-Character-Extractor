# Story Character Extractor

The **Story Character Extractor** is a Python-based project designed to compute embeddings for story datasets and extract detailed character information using machine learning models. It uses **LangChain**, **MistralAI embeddings**, and **vector databases** for efficient text processing and querying.

---

## Features

- **Compute Embeddings**: Generate embeddings for story datasets and store them in a vector database.
- **Character Information Extraction**: Retrieve structured information about characters from stories, including their roles, relationships, and summaries.

---

## Project Structure

```text
.
├── embeddings.py         # Script for computing embeddings from story datasets
├── extraction.py         # Script for extracting character information
├── document_processing.py # Utility for loading story documents
├── main.py               # CLI interface to interact with the project
├── utils.py              # Utility functions (e.g., API key management)
├── requirements.txt      # Python dependencies
```

## Requirements

Ensure you have the following installed:

- Python 3.8 or higher

---

## Installation Steps

### 1. Clone the repository:
```bash
git clone https://github.com/Aawegg/Story-Character-Extractor.git
cd Story-Character-Extractor
```

### 2. Create a virtual environment:
```bash
python -m venv venv
```

### 3. Activate the virtual environment:
On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Compute Embeddings
Generate embeddings for a directory of story text files and store them in a vector database:

```bash
python main.py compute-embeddings-cli --dataset-path <path_to_story_directory>
```

---

## File Details

### embeddings.py
- Loads story documents from a specified directory.
- Splits text into manageable chunks.
- Computes embeddings using the **MistralAI model**.
- Stores embeddings in a **Chroma vector database**.

### extraction.py
- Queries the vector database for relevant story excerpts.
- Uses a language model to generate structured JSON data about characters, including:
  - **Name**
  - **Story title**
  - **Summary**
  - **Relationships with other characters**
  - **Narrative role** (e.g., protagonist, antagonist)

### document_processing.py
- Provides utility functions to load .txt files from a directory into **LangChain-compatible document objects**.

### main.py
- Command-line interface (CLI) to interact with the project functionalities:
  - Compute embeddings.
  - Retrieve character information.

### utils.py
- Contains helper functions such as API key retrieval.

---

## Environment Variables

Set your **MistralAI API key** as an environment variable:

```bash
export MISTRAL_API_KEY="your-mistral-api-key"
```

Alternatively, modify utils.py to include your API key directly (not recommended for production).

---

## Error Handling

- **No Documents Found**: Ensure your dataset directory contains .txt files.
- **Invalid API Key**: Verify that your **MistralAI API key** is correctly set in the environment or in utils.py.
- **JSON Parsing Errors**: Check the output format of the language model if issues arise during character info extraction.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
