import typer
from embeddings import compute_embeddings
from extraction import get_character_info

app = typer.Typer()

@app.command()
def compute_embeddings_cli(dataset_path: str):
    """Compute embeddings for all story files in the specified directory."""
    try:
        compute_embeddings(dataset_path)
    except Exception as e:
        print(f"Error: {e}")

@app.command()
def get_character_info_cli(character_name: str):
    """Retrieve information about a specific character."""
    try:
        info = get_character_info(character_name)
        print(info.model_dump_json(indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app()
