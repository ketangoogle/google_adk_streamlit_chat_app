"""
Utility helper functions for the ADK Greeting Chat Application
"""

import os
import time
from typing import Dict, Any, Optional


def generate_session_id() -> str:
    """Generate a unique session ID for ADK sessions"""
    return f"streamlit_adk_session_{int(time.time())}_{os.urandom(4).hex()}"


def validate_user_input(user_input: str) -> bool:
    """Validate user input for basic requirements"""
    if not user_input or not user_input.strip():
        return False
    return len(user_input.strip()) > 0


def format_user_details(name: str = "", hobbies: str = "", interests: str = "") -> Dict[str, str]:
    """Format user details into a standardized dictionary"""
    return {
        "user_name": name.strip() if name else "",
        "user_hobbies": hobbies.strip() if hobbies else "",
        "user_interests": interests.strip() if interests else ""
    }


def truncate_text(text: str, max_length: int = 150) -> str:
    """Truncate text to specified length with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def log_user_interaction(action: str, details: Optional[Dict[str, Any]] = None):
    """Log user interactions for debugging purposes"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] User Action: {action}"
    if details:
        log_message += f" - Details: {details}"
    print(log_message)


def safe_get_env_var(var_name: str, default_value: str = "") -> str:
    """Safely get environment variable with default fallback"""
    return os.environ.get(var_name, default_value)


def format_greeting_response(status: str, content: str) -> Dict[str, str]:
    """Format greeting tool response in standardized format"""
    return {
        "status": status,
        "content": content,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }


print("Helper utilities loaded successfully")