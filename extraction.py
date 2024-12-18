from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage
from pydantic import BaseModel, Field
from typing import Dict, Union
import json
import sys
from utils import get_api_key


class RelationDetails(BaseModel):
    relationType: str
    summary: str

    class Config:
        extra = 'ignore'


class CharacterInfo(BaseModel):
    name: str = Field(..., description="Character's name")
    storyTitle: str = Field(..., description="Title of the story")
    summary: str = Field(..., description="Brief character summary")
    relations: Dict[str, RelationDetails] = Field(default_factory=dict, description="Dictionary of relationships with other characters")
    characterType: str = Field(..., description="Role in the story")

    class Config:
        extra = 'ignore'  # Ignore extra fields not defined in the model
        populate_by_name = True


def get_character_info(character_name: str) -> CharacterInfo:
    """
    Retrieve character information using vector database and LLM.
    
    Args:
        character_name (str): Name of the character to retrieve information about.
    
    Returns:
        CharacterInfo: Structured information about the character.
    
    Raises:
        ValueError: If there are issues retrieving or parsing character information.
    """
    try:
        # Load API key
        api_key = get_api_key("MISTRAL_API_KEY")
        
        # Initialize vector database with embeddings
        embeddings = MistralAIEmbeddings(
            model="mistral-embed", 
            api_key=api_key
        )
        vectorstore = Chroma(
            persist_directory="./story_embeddings",
            embedding_function=embeddings,
        )
        
        # Query for character information
        query = f"Detailed information about character {character_name}"
        docs = vectorstore.similarity_search(query, k=3)
        
        # Check if any documents were found
        if not docs:
            raise ValueError(f"No relevant documents found for character {character_name}")
        
        # Initialize the LLM for generating responses
        llm = ChatMistralAI(
            api_key=api_key, 
            model="mistral-large-latest",  # Use the most capable model
            temperature=0.2  # Low temperature for more consistent responses
        )
        
        # Create a prompt template for extracting character information
        prompt = ChatPromptTemplate.from_template(""" 
        You are an expert literary analyst extracting character information.

        Story Excerpts:
        {context}

        Task: Provide a comprehensive JSON description for the character {character_name}.
        
        JSON Format Requirements:
        - name: Full name of the character
        - storyTitle: Title of the story/work
        - summary: Concise 2-3 sentence character description 
        - relations: Dictionary of key relationships with details
          * Keys are other character names
          * Values are objects with:
            - relationType: Describes the nature of the relationship
            - summary: Brief description of the relationship
        - characterType: Archetypal or narrative role (e.g., protagonist, antagonist, mentor)

        Important: Ensure the JSON is valid and matches the specified structure.
        Provide a professional, detailed, and accurate response.
        """)
        
        # Combine prompt and LLM into a chain and invoke it with context from documents
        chain = prompt | llm
        response = chain.invoke({
            "character_name": character_name,
            "context": "\n".join(doc.page_content for doc in docs),
        })
        
        # Extract content from AIMessage or fallback to string representation of response
        content = response.content if isinstance(response, AIMessage) else str(response)
        
        # Parse JSON content into a CharacterInfo object
        def parse_character_info(content: Union[str, Dict]) -> CharacterInfo:
            if isinstance(content, dict):
                return CharacterInfo.parse_obj(content)
            
            try:
                # Attempt to parse JSON directly from string content
                json_dict = json.loads(content)
                return CharacterInfo.parse_obj(json_dict)
            except json.JSONDecodeError as e:
                # Fallback to regex-based extraction if JSON parsing fails
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL | re.MULTILINE)
                if json_match:
                    try:
                        json_dict = json.loads(json_match.group())
                        return CharacterInfo.parse_obj(json_dict)
                    except Exception as extract_err:
                        raise ValueError(f"Could not extract valid JSON: {extract_err}")
                else:
                    raise ValueError(f"No valid JSON found in the response: {content}")
        
        return parse_character_info(content)

    except Exception as e:
        print(f"An error occurred while retrieving character information: {e}", file=sys.stderr)
        raise


# Optional: Example usage for testing purposes
if __name__ == "__main__":
    try:
        character_info = get_character_info("John")
        
        # Use model_dump_json() instead of json() for Pydantic v2 compatibility
        print(character_info.model_dump_json(indent=4))
    except Exception as e:
        print(f"Error retrieving character info: {e}", file=sys.stderr)
