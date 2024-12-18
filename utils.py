import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_api_key(env_var: str) -> str:
    """Retrieve API key from environment variables."""
    api_key = os.getenv(env_var)
    if not api_key:
        raise ValueError(f"{env_var} environment variable not set.")
    return api_key
