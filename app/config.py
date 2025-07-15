from dotenv import load_dotenv
from pathlib import Path
import os

# absolute path to the root (could be solved with os.path.join as well)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

PORT = int(os.getenv("PORT"))
