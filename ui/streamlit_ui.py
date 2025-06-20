import streamlit as st
import logging
from typing import Tuple

from services.adk_service import initialize_adk, run_adk_sync
from google.adk.runners import Runner
from config.settings import (
    MESSAGE_HISTORY_KEY,
    APP_NAME_FOR_ADK,
    USER_ID,
    MODEL_GEMINI,
    # get_api_key #uncomment if you want to check API key in the future
)


def setup_page_config():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="ADK Greeting & Chat Agent",
        layout="wide",
        initial_sidebar_state="collapsed"  # Ensure sidebar is collapsed by default
    )


def render_header():
    """Render the application header and description"""
    st.title("👋 Greeting & Chat Assistant (Powered by ADK & Gemini)")
    st.markdown("""
        This application uses the Google Agent Development Kit (ADK) to provide a chat interface
        for greeting you and allowing general chat.
        \n\n
        **Note:** Ensure you have set up your Google API key correctly in the `.env` file to use this application.
    """)
    st.divider()


# def check_api_key():
#     """Check if API key is valid and display error if not"""
#     api_key = get_api_key()
#     if not api_key:
#         st.error(
#             "⚠️ **Action Required: Google API Key Not Found or Invalid!** ⚠️\n\n"
#             "1. Create a file named `.env` in the same directory as your script.\n"
#             "2. Add the following line to the `.env` file:\n"
#             "   `GOOGLE_API_KEY='YOUR_ACTUAL_GEMINI_API_KEY'`\n"
#             "3. Replace `YOUR_ACTUAL_GEMINI_API_KEY` with your valid key from Google AI Studio.\n"
#             "4. **Restart the Streamlit application.**",
#             icon="🔥"
#         )
#         st.stop()  # Halt further execution if key is missing/invalid
#     return api_key


def initialize_adk_service() -> Tuple[Runner, str]:
    """Initialize ADK Runner and Session with error handling"""
    try:
        adk_runner, current_session_id = initialize_adk()
        return adk_runner, current_session_id
    except Exception as e:
        st.error(f"**Fatal Error:** Could not initialize the ADK Runner or Session Service: {e}", icon="❌")
        st.error("Please check the terminal logs for more details, ensure your API key is valid, and restart the application.")
        logging.exception("Critical ADK Initialization failed in Streamlit UI context.")
        st.stop()  # Stop the app if ADK fails to initialize


def initialize_message_history():
    """Initialize message history in session state if not exists"""
    if MESSAGE_HISTORY_KEY not in st.session_state:
        st.session_state[MESSAGE_HISTORY_KEY] = []
        print("Initialized Streamlit message history.")


def render_chat_interface(adk_runner: Runner, current_session_id: str):
    """Render the main chat interface"""
    st.subheader("Chat with the Assistant")
    st.markdown("Try saying **'hello'** or **'greet me'** after filling in your details above.")

    # Initialize message history
    initialize_message_history()

    # Display existing chat messages
    for message in st.session_state[MESSAGE_HISTORY_KEY]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=False)

    # Chat input field
    if prompt := st.chat_input("Ask for a greeting (e.g., 'greet me'), or just chat..."):
        print(f"User input received: '{prompt[:50]}...'")
        # Add user message to history and display
        st.session_state[MESSAGE_HISTORY_KEY].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt, unsafe_allow_html=False)

        # Process prompt with ADK agent and display response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Assistant is thinking..."):
                try:
                    agent_response = run_adk_sync(adk_runner, current_session_id, prompt)
                    message_placeholder.markdown(agent_response, unsafe_allow_html=False)
                except Exception as e:
                    error_msg = f"Sorry, an error occurred while processing your request: {e}"
                    st.error(error_msg)
                    agent_response = f"Error: Failed to get response. {e}"
                    logging.exception("Error occurred within the Streamlit chat input processing block.")
        
        # Add agent response to history
        st.session_state[MESSAGE_HISTORY_KEY].append({"role": "assistant", "content": agent_response})
        print("Agent response added to history. Streamlit will rerun.")


def render_debug_info(current_session_id: str):
    """Render debugging information in an expandable section"""
    with st.expander("ADK Internal Details (for debugging)"):
        st.caption(f"**App Name:** `{APP_NAME_FOR_ADK}`")
        st.caption(f"**User ID:** `{USER_ID}`")
        st.caption(f"**Session ID:** `{current_session_id}`")
        st.caption(f"**LLM Model:** `{MODEL_GEMINI}`")
        st.caption("Powered by Google Agent Development Kit.")


def run_streamlit_app():
    """Main function to run the Streamlit application"""
    # Setup page configuration
    setup_page_config()
    
    # Render header
    render_header()
    
    # Check API key
    # check_api_key()
    
    # Initialize ADK service
    adk_runner, current_session_id = initialize_adk_service()
    
    st.divider()
    
    # Render chat interface
    render_chat_interface(adk_runner, current_session_id)
    
    # Render debug information
    render_debug_info(current_session_id)
    
    print("✅ Streamlit UI Rendering Complete.")


if __name__ == "__main__":
    run_streamlit_app()
    