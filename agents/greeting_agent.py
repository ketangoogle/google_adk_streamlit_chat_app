from google.adk.agents import Agent
from tools.greeting_tools import fetch_greeting
from config.settings import MODEL_GEMINI


def create_greeting_agent():
    """Create and return the greeting agent with proper configuration"""
    
    root_agent = Agent(
        name="greeting_agent",
        model=MODEL_GEMINI,
        description="An agent that greets the user based on their name, hobbies, and interests.",
        instruction="""
        You are a helpful assistant that greets the user.
        
        When a user tells you their name, hobbies, or interests, use the 'fetch_greeting' tool with the appropriate parameters to store this information and get a personalized greeting.
        
        Examples of when and how to use fetch_greeting:
        - "My name is John" -> call fetch_greeting(name="John")  
        - "I'm Sarah and I love reading" -> call fetch_greeting(name="Sarah", hobbies="reading")
        - "I enjoy hiking and cooking" -> call fetch_greeting(hobbies="hiking and cooking")
        - "I'm interested in technology" -> call fetch_greeting(interests="technology")
        - "Hi" or "Hello" or "Give me a greeting" -> call fetch_greeting() with no parameters
        
        The 'fetch_greeting' tool will:
        1. Update any user information you provide
        2. Generate a personalized greeting using all stored user information
        3. Return the greeting message
        
        You can also answer general questions and have normal conversations with the user.
        Always be friendly and helpful.
        """,
        tools=[fetch_greeting],  # Register the single tool
    )
    
    return root_agent


print("Greeting agent module loaded successfully")