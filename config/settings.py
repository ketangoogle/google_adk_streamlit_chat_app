import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging to suppress most ADK internal logs, showing only errors
logging.basicConfig(level=logging.ERROR)

# Constants
GREETING_FETCH_CACHE_STATE_KEY = "greeting_fetch_cache_state"
MODEL_GEMINI = "gemini-1.5-flash"
APP_NAME_FOR_ADK = "greeting_app"
USER_ID = "ketanraj"  # Consider making this dynamic in a real app

# Initial state for ADK session
INITIAL_STATE = {
    "user_name": "Ketan Raj",
    "user_hobbies": "Coding, Reading, Gaming",
    "user_interests": "AI, Technology, Open Source"
}

# Streamlit session keys
MESSAGE_HISTORY_KEY = "messages_final_mem_v2"
ADK_SESSION_KEY = "adk_session_id"

# # API Key validation
# def get_api_key():
#     """Get and validate Google API key from environment"""
#     api_key = os.environ.get("GOOGLE_API_KEY")
#     if not api_key or "YOUR_GOOGLE_API_KEY" in api_key:
#         return None
#     return api_key

print("Configuration loaded successfully")