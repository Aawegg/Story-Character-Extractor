# Character Information Extraction System
This project is a text document processing pipeline designed to extract detailed character information from stories. Using embeddings, vector databases, and a large language model (LLM), the system provides structured information about characters, including their relationships, roles, and summaries.

---

## Features
* **Document Processing**: Loads and preprocesses .txt files from a specified directory.
* **Embedding Computation**: Generates vector embeddings for text chunks using MistralAI.
* **Character Information Extraction**: Retrieves structured details about characters using vector similarity search and LLM prompts.
* **Command-Line Interface (CLI)**: Provides an easy-to-use interface for embedding computation and character queries.
## Technologies Used
* Python
* LangChain Framework
* MistralAI
* Chroma Vector Database
* Typer (CLI Framework)
* Pydantic (Data Validation)

---

## Installation
### Clone the Repository

```bash
git clone https://github.com/your-username/character-info-extraction.git
cd character-info-extraction
```
### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
  Create a .env file or set the following environment variables:

```makefile
MISTRAL_API_KEY=your-mistral-api-key
```

---

## Usage
1. Compute Embeddings
Generate embeddings for all .txt files in a directory and store them in a vector database.

```bash
python main.py compute-embeddings-cli <dataset_path>
```
* Example:
```bash
python main.py compute-embeddings-cli ./stories
```

2. Retrieve Character Information
Query the system for details about a specific character.

```bash
python main.py get-character-info-cli <character_name>
```

* Example:
```bash
python main.py get-character-info-cli Alice
```

---

## Project Structure
```bash
character-info-extraction/
├── document_processing.py   # Handles loading and preprocessing text files.
├── embeddings.py            # Computes and stores embeddings in a vector database.
├── extraction.py            # Extracts structured character information using LLMs.
├── main.py                  # CLI for embedding computation and character queries.
├── requirements.txt         # List of dependencies.
└── README.md                # Project documentation.
```
---

## Example Workflow
1. Prepare a Dataset:
  Place .txt files in a directory, e.g., ./stories.

2. Compute Embeddings:
  Run the compute-embeddings-cli command to generate embeddings.

3. Query Character Information:
  Use the get-character-info-cli command to retrieve details about characters.

## Sample Output
### Input Command:
```bash
python main.py get-character-info-cli Alice
```
### Output (JSON):
```json
{
    "name": "Alice",
    "storyTitle": "Adventures in Wonderland",
    "summary": "A curious and adventurous girl who explores a magical world.",
    "relations": {
        "White Rabbit": {
            "relationType": "Friend",
            "summary": "A guide and companion during her journey."
        },
        "Queen of Hearts": {
            "relationType": "Antagonist",
            "summary": "The ruler of Wonderland who opposes Alice."
        }
    },
    "characterType": "Protagonist"
}
```
---

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or support, contact Aaweg Bhaladhare at your-email@example.com.

_Feel free to replace placeholders like your-username, your-mistral-api-key, and your-email@example.com with the actual details for your project._
