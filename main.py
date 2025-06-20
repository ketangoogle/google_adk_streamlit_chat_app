"""
ADK Greeting Chat Application - Main Entry Point

This is the main entry point for the Streamlit application that uses
Google Agent Development Kit (ADK) to provide a personalized greeting
and chat interface.

To run the application:
    streamlit run main.py

Make sure to:
1. Install all dependencies: pip install -r requirements.txt
2. Set up your .env file with GOOGLE_API_KEY
3. Run the application with the command above
"""

from ui.streamlit_ui import run_streamlit_app

print("Imports and Configuration done")

if __name__ == "__main__":
    print("🚀 Starting ADK Greeting Chat Application...")
    run_streamlit_app()
    print("✅ Application started successfully!")