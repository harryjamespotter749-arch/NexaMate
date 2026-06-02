from pathlib import Path

# Root folder of the whole project
BASE_DIR = Path(__file__).resolve().parent.parent

# Main project folders
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
DATABASE_DIR = BASE_DIR / "database"

# Main project files
FAQ_FILE = DATA_DIR / "faqs.csv"
INTENT_EXAMPLES_FILE = DATA_DIR / "intent_examples.csv"
INTENT_MODEL_FILE = MODEL_DIR / "intent_model.joblib"

# Chatbot confidence settings
MIN_SIMILARITY_SCORE = 0.25
MIN_INTENT_CONFIDENCE = 0.40

# Create folders automatically if they do not exist
DATA_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)