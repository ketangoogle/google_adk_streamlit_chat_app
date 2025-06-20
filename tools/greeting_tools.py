from typing import Dict, Any, Optional
from google.adk.tools.tool_context import ToolContext


def fetch_greeting(tool_context: ToolContext, name: Optional[str] = None, hobbies: Optional[str] = None, interests: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetches a greeting message based on the user's name, hobbies, and interests.
    Can also update user information if provided as parameters.

    Args:
        tool_context (ToolContext): The ADK ToolContext, providing access to session state via tool_context.state.
        name (str, optional): User's name to update
        hobbies (str, optional): User's hobbies to update  
        interests (str, optional): User's interests to update

    Returns:
       Dict[str, Any]: A dictionary with 'status' ('success' or 'error') and either 'greeting' (personalized message)
        or 'message' (error description).
    """
    print(f" -------Tool: fetch_greeting called with name={name}, hobbies={hobbies}, interests={interests} -------")

    try:
        # Access the ADK session state directly through tool_context.state
        adk_session_state = tool_context.state
        
        # Update user information if provided as parameters
        if name:
            adk_session_state['user_name'] = name
            print(f" -------Tool: SESSION UPDATED - user_name set to: {name} -------")
        
        if hobbies:
            adk_session_state['user_hobbies'] = hobbies
            print(f" -------Tool: SESSION UPDATED - user_hobbies set to: {hobbies} -------")
        
        if interests:
            adk_session_state['user_interests'] = interests
            print(f" -------Tool: SESSION UPDATED - user_interests set to: {interests} -------")

        # Fetch current user details from ADK session state
        user_name = adk_session_state.get('user_name', 'Friend')
        user_hobbies = adk_session_state.get('user_hobbies', '')
        user_interests = adk_session_state.get('user_interests', '')
        
        print(f" -------Tool: fetch_greeting - User details: name={user_name}, hobbies={user_hobbies}, interests={user_interests} -------")

        # Create the personalized greeting message
        greeting_parts = [f"Hello {user_name}!"]
        
        if user_hobbies:
            greeting_parts.append(f"I see you enjoy {user_hobbies}.")
        
        if user_interests:
            greeting_parts.append(f"Your interests in {user_interests} sound fascinating!")
        
        if not user_hobbies and not user_interests:
            greeting_parts.append("Nice to meet you!")
        
        greeting_parts.append("How can I help you today?")
        
        personalized_greeting = " ".join(greeting_parts)
        
        print(f" -------Tool: fetch_greeting - Generated greeting: {personalized_greeting} -------")

        return {"status": "success", "greeting": personalized_greeting}
        
    except Exception as e:
        print(f" -------Tool: ERROR in fetch_greeting: {e} -------")
        return {"status": "error", "message": f"Sorry, I encountered an error while processing your greeting: {str(e)}"}


print("Greeting tools loaded successfully")