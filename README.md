# Google-ADK Greeting Chat Application

A personalized greeting and chat application built with **Streamlit** and **Google Agent Development Kit (ADK)**. The application uses Gemini AI to provide intelligent, personalized greetings based on user information and enables natural conversation.

## 👋 Features

-   **Personalized Greetings**: Stores and uses user's name, hobbies, and interests for customized interactions.
-   **Intelligent Chat Interface**: Powered by Google's Gemini 1.5 Flash model.
-   **Session Management**: Maintains conversation context across interactions.
-   **Real-time Processing**: Asynchronous handling of user requests.
-   **Clean Architecture**: Well-organized, modular codebase.
-   **Debug Information**: Built-in debugging tools for development.

## 🏗️ Architecture

The application is structured with a clean, modular architecture:

```

greeting\_chat\_app/
├── main.py                 \# Main application entry point
├── config/
│   ├── **init**.py
│   └── settings.py         \# Configuration constants and environment setup
├── agents/
│   ├── **init**.py
│   └── greeting\_agent.py   \# Agent definition and configuration
├── tools/
│   ├── **init**.py
│   └── greeting\_tools.py   \# Tool functions (fetch\_greeting)
├── services/
│   ├── **init**.py
│   └── adk\_service.py      \# ADK initialization and session management
├── ui/
│   ├── **init**.py
│   └── streamlit\_ui.py     \# Streamlit UI components and layout
├── utils/
│   ├── **init**.py
│   └── helpers.py          \# Helper functions and utilities
├── .env                    \# Environment variables (Google Cloud/API Key settings)
├── requirements.txt        \# Python dependencies
└── README.md              \# This file

````

## 🚀 Quick Start

### Prerequisites

-   Python 3.8 or higher
-   Google Cloud Project with **Vertex AI API enabled**
-   `gcloud` CLI installed and authenticated (for Vertex AI)
-   `pip` (Python package installer)

### Installation

1.  **Clone or download the project files**

    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

2.  **Create and activate a virtual environment**
    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    **`requirements.txt` content:**
    ```
    streamlit
    google-generativeai
    python-dotenv
    google-cloud-aiplatform
    google-api-core
    google-auth
    ```

### Google Cloud Project Setup & Authentication (Recommended: Vertex AI)

This application is configured to primarily use **Google Cloud Vertex AI** for accessing the Gemini models. Vertex AI provides enhanced security (IAM-based authentication), better model management, and access to more enterprise-grade features.

#### a. `.env` Configuration for Vertex AI

Create a file named `.env` in the root directory of your project and add the following lines:

```env
# If using Google Cloud services (including Vertex AI), set the following environment variables.
# Set GOOGLE_GENAI_USE_VERTEXAI to TRUE to use Vertex AI.
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id  # Replace with your actual Google Cloud Project ID
GOOGLE_CLOUD_LOCATION=asia-south1                 # Replace with your desired Vertex AI region (e.g., us-central1, europe-west1).
                                                  # Ensure the MODEL_GEMINI (currently gemini-1.5-flash) is available in this region.
````

**Important Notes:**

  * **`GOOGLE_CLOUD_PROJECT`**: This **must** be the ID of your Google Cloud Project where you have enabled the Vertex AI API.
  * **`GOOGLE_CLOUD_LOCATION`**: This is the Google Cloud region where you want to access the models. Ensure that the `MODEL_GEMINI` specified in `config/settings.py` (currently `gemini-1.5-flash`) is available in this region. You can check model availability [here](https://www.google.com/search?q=https://cloud.google.com/vertex-ai/docs/generative/model-versions%23generative_model_versions).

#### b. Authenticate with Google Cloud CLI

For local development, the application uses **Application Default Credentials (ADC)**.

1.  **Install Google Cloud CLI:** If you don't have it, follow the official instructions [here](https://cloud.google.com/sdk/docs/install).

2.  **Authenticate:** Open your terminal and run the following command. This will open a browser for you to log in to your Google account and grant permissions.

    ```bash
    gcloud auth application-default login
    ```

#### c. Enable Vertex AI API

In your Google Cloud Project (`your-google-cloud-project-id`), ensure that the **Vertex AI API** is enabled. You can do this by navigating to "APIs & Services \> Enabled APIs & services" in the Google Cloud Console.

### 4\. Run the application

```bash
streamlit run main.py
```

### 5\. Open your browser

The application will automatically open in your default browser, typically at `http://localhost:8501`.

## 🎮 How to Use

### Getting Started

1.  **Launch the app** and you'll see the greeting interface.
2.  **Try these example interactions**:
      * "Hello" or "Hi" - Get a basic greeting.
      * "My name is John" - Store your name.
      * "I love reading and coding" - Store your hobbies.
      * "I'm interested in AI and technology" - Store your interests.
      * "Greet me" - Get a personalized greeting with all stored info.

### Example Conversations

```
User: "Hi, my name is Sarah and I love photography"
Assistant: Hello Sarah! I see you enjoy photography. How can I help you today?

User: "I'm also interested in travel and art"
Assistant: Hello Sarah! I see you enjoy photography. Your interests in travel and art sound fascinating! How can I help you today?
```

### Features You Can Use

  - **Personalized Greetings**: The app remembers your name, hobbies, and interests.
  - **Natural Conversation**: Ask questions, have discussions, get help with various topics.
  - **Session Persistence**: Your information is remembered during your session.
  - **Real-time Responses**: Fast, intelligent responses powered by Gemini AI.

## ⚙️ Configuration

### Environment Variables (`.env` file)

| Variable                  | Description                                                | Required (for Vertex AI) |
| :------------------------ | :--------------------------------------------------------- | :----------------------- |
| `GOOGLE_GENAI_USE_VERTEXAI` | Set to `TRUE` to use Vertex AI for model access.           | Yes                      |
| `GOOGLE_CLOUD_PROJECT`    | Your Google Cloud Project ID.                              | Yes                      |
| `GOOGLE_CLOUD_LOCATION`   | The Google Cloud region for Vertex AI models (e.g., `us-central1`, `asia-south1`). | Yes                      |
| `GOOGLE_API_KEY`          | Your Google AI API key for Gemini access. (Used only if `GOOGLE_GENAI_USE_VERTEXAI` is `FALSE`). | No (Yes for API Key mode) |

### Application Settings (`config/settings.py`)

You can modify these settings in `config/settings.py`:

  - `MODEL_GEMINI`: AI model version (current default: `"gemini-1.5-flash"`)
  - `USER_ID`: User identifier (default: `"ketanraj"`)
  - `APP_NAME_FOR_ADK`: Application name for ADK
  - `INITIAL_STATE`: Default user information for new ADK sessions

## 📁 Project Structure Details

### Core Components

  - **`main.py`**: Application entry point that starts the Streamlit server.
  - **`config/settings.py`**: Centralized configuration management.
  - **`agents/greeting_agent.py`**: Defines the AI agent behavior and instructions.
  - **`tools/greeting_tools.py`**: Custom tool for fetching and storing user greetings.
  - **`services/adk_service.py`**: ADK initialization, session management, and async communication with the agent.
  - **`ui/streamlit_ui.py`**: Complete Streamlit user interface, including chat history and input.
  - **`utils/helpers.py`**: Utility functions for common operations.

### Key Features

  - **Modular Design**: Each component has a specific responsibility.
  - **Error Handling**: Comprehensive error handling and logging.
  - **Session Management**: Persistent sessions with state management.
  - **Async Processing**: Non-blocking user interaction handling.
  - **Debug Tools**: Built-in debugging and monitoring capabilities.

## ⚠️ Troubleshooting

### Common Issues

1.  **"Publisher Model ... not found" Error**

      * This means the `MODEL_GEMINI` specified in `config/settings.py` is not available in the `GOOGLE_CLOUD_LOCATION` you set in your `.env` file.
      * **Solution:** Update `MODEL_GEMINI` to one known to be available in your region (e.g., `gemini-1.5-flash` in `asia-south1`), or change your `GOOGLE_CLOUD_LOCATION` to a region where your desired model is available.

2.  **Authentication Errors (e.g., "Insufficient permissions")**

      * Ensure you have run `gcloud auth application-default login` and are logged in with an account that has permissions (`Vertex AI User` and `Service Usage Consumer` roles at minimum) on your Google Cloud project.
      * Verify the Vertex AI API is enabled in your Google Cloud Project.
      * Check that `GOOGLE_CLOUD_PROJECT` in `.env` matches your actual Google Cloud Project ID.

3.  **"API Key Not Found" Error**

      * This error message indicates that the application is still looking for `GOOGLE_API_KEY`, which is typically the case when `GOOGLE_GENAI_USE_VERTEXAI` is set to `FALSE` or when the API key check code is uncommented.
      * **Solution:** Ensure `GOOGLE_GENAI_USE_VERTEXAI=TRUE` in your `.env` file and verify that the API key check code (in `ui/streamlit_ui.py` and `config/settings.py`) remains commented out.

4.  **Import Errors**

      * Make sure all dependencies are installed: `pip install -r requirements.txt`.
      * Ensure you're running the application from the correct directory (`greeting_chat_app/`).

5.  **Session Errors**

      * Refresh the browser page to reset the Streamlit session.
      * Check your terminal output for detailed error messages.

6.  **Slow Responses**

      * The very first request might be slower due to model initialization.
      * Subsequent requests should be faster.

### Debug Information

The app includes a debug panel (expand "ADK Internal Details") showing:

  - Current session ID
  - User ID
  - Model being used
  - App configuration

## 🤝 Contributing

To contribute to this project:

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes, following the existing code structure and style.
4.  Test your changes thoroughly.
5.  Submit a pull request.

### Code Style

  - Follow existing naming conventions.
  - Add appropriate comments and docstrings.
  - Maintain the modular structure.
  - Test all new features.

## 📄 License

This project is open source. Please check with the original authors regarding specific licensing terms.

## 🙋‍♂️ Support

If you encounter issues:

1.  Check the troubleshooting section above.
2.  Review the terminal output for error messages.
3.  Ensure your environment variables and Google Cloud setup are correct.
4.  Try refreshing the browser page.

For technical questions about Google ADK, refer to the [Google AI documentation](https://google.github.io/adk-docs/).

-----

**Built with ❤️ using Streamlit and Google ADK**

```
```