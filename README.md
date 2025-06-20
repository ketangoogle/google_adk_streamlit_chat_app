# Google-ADK Greeting Chat Application 

A personalized greeting and chat application built with **Streamlit** and **Google Agent Development Kit (ADK)**. The application uses Gemini AI to provide intelligent, personalized greetings based on user information and enables natural conversation.

## 📋 Features

- **Personalized Greetings**: Stores and uses user's name, hobbies, and interests for customized interactions
- **Intelligent Chat Interface**: Powered by Google's Gemini 2.0 Flash model
- **Session Management**: Maintains conversation context across interactions
- **Real-time Processing**: Asynchronous handling of user requests
- **Clean Architecture**: Well-organized, modular codebase
- **Debug Information**: Built-in debugging tools for development

## 🏗️ Architecture

The application is structured with a clean, modular architecture:

```
greeting_chat_app/
├── main.py                 # Main application entry point
├── config/
│   ├── __init__.py
│   └── settings.py         # Configuration constants and environment setup
├── agents/
│   ├── __init__.py
│   └── greeting_agent.py   # Agent definition and configuration
├── tools/
│   ├── __init__.py
│   └── greeting_tools.py   # Tool functions (fetch_greeting)
├── services/
│   ├── __init__.py
│   └── adk_service.py      # ADK initialization and session management
├── ui/
│   ├── __init__.py
│   └── streamlit_ui.py     # Streamlit UI components and layout
├── utils/
│   ├── __init__.py
│   └── helpers.py          # Helper functions and utilities
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API Key with access to Gemini models
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   ```
   
   > **How to get a Google API Key:**
   > 1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   > 2. Sign in with your Google account
   > 3. Create a new API key
   > 4. Copy the key and paste it in your `.env` file

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser**
   
   The application will automatically open in your default browser, typically at `http://localhost:8501`

## 🎯 How to Use

### Getting Started

1. **Launch the app** and you'll see the greeting interface
2. **Try these example interactions**:
   - "Hello" or "Hi" - Get a basic greeting
   - "My name is John" - Store your name
   - "I love reading and coding" - Store your hobbies
   - "I'm interested in AI and technology" - Store your interests
   - "Greet me" - Get a personalized greeting with all stored info

### Example Conversations

```
User: "Hi, my name is Sarah and I love photography"
Assistant: Hello Sarah! I see you enjoy photography. How can I help you today?

User: "I'm also interested in travel and art"
Assistant: Hello Sarah! I see you enjoy photography. Your interests in travel and art sound fascinating! How can I help you today?
```

### Features You Can Use

- **Personalized Greetings**: The app remembers your name, hobbies, and interests
- **Natural Conversation**: Ask questions, have discussions, get help with various topics
- **Session Persistence**: Your information is remembered during your session
- **Real-time Responses**: Fast, intelligent responses powered by Gemini AI

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google AI API key for Gemini access | Yes |

### Application Settings

You can modify these settings in `config/settings.py`:

- `MODEL_GEMINI`: AI model version (default: "gemini-2.0-flash")
- `USER_ID`: User identifier (default: "ketanraj")
- `APP_NAME_FOR_ADK`: Application name for ADK
- `INITIAL_STATE`: Default user information

## 📁 Project Structure Details

### Core Components

- **`main.py`**: Application entry point that starts the Streamlit server
- **`config/settings.py`**: Centralized configuration management
- **`agents/greeting_agent.py`**: Defines the AI agent behavior and instructions
- **`tools/greeting_tools.py`**: Custom tools for fetching and storing user greetings
- **`services/adk_service.py`**: ADK session management and async communication
- **`ui/streamlit_ui.py`**: Complete Streamlit user interface
- **`utils/helpers.py`**: Utility functions for common operations

### Key Features

- **Modular Design**: Each component has a specific responsibility
- **Error Handling**: Comprehensive error handling and logging
- **Session Management**: Persistent sessions with state management
- **Async Processing**: Non-blocking user interaction handling
- **Debug Tools**: Built-in debugging and monitoring capabilities

## 🐛 Troubleshooting

### Common Issues

1. **"API Key Not Found" Error**
   - Ensure `.env` file exists in the root directory
   - Check that `GOOGLE_API_KEY` is correctly set
   - Restart the application after adding the key

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Ensure you're running from the correct directory

3. **Session Errors**
   - Refresh the browser page to reset the session
   - Check terminal output for detailed error messages

4. **Slow Responses**
   - This is normal for the first request (model initialization)
   - Subsequent requests should be faster

### Debug Information

The app includes a debug panel (expand "ADK Internal Details") showing:
- Current session ID
- User ID
- Model being used
- App configuration

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing code structure
4. Test your changes thoroughly
5. Submit a pull request

### Code Style

- Follow existing naming conventions
- Add appropriate comments and docstrings
- Maintain the modular structure
- Test all new features

## 📄 License

This project is open source. Please check with the original authors regarding specific licensing terms.

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the terminal output for error messages
3. Ensure your API key is valid and has proper permissions
4. Try refreshing the browser page

For technical questions about Google ADK, refer to the [Google AI documentation](https://google.github.io/adk-docs/).

---

**Built with ❤️ using Streamlit and Google ADK**