import os
from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

GROQ_API_KEY = os.getenv("groq_api")
DATA_BASE_URL = os.getenv("DATA_BASE_URL")