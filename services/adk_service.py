# services/adk_service.py

import os
import asyncio # Make sure asyncio is imported
import time
import logging
import streamlit as st
from typing import Tuple

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types as genai_types

from agents.greeting_agent import create_greeting_agent
from config.settings import (
    APP_NAME_FOR_ADK,
    USER_ID,
    INITIAL_STATE,
    ADK_SESSION_KEY
)


@st.cache_resource
def initialize_adk() -> Tuple[Runner, str]:
    """
    Initializes the ADK Runner and InMemorySessionService for the application.
    Manages the unique ADK session ID within the Streamlit session state.

    Returns:
        tuple: (Runner instance, active ADK session ID)
    """
    print("--- ADK Init: Attempting to initialize Runner and Session Service... ---")

    # Create the greeting agent
    root_agent = create_greeting_agent()

    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME_FOR_ADK,
        session_service=session_service
    )
    print("--- ADK Init: Runner and Session Service initialized successfully ---")

    if ADK_SESSION_KEY not in st.session_state:
        session_id = f"streamlit_adk_session_{int(time.time())}_{os.urandom(4).hex()}"
        st.session_state[ADK_SESSION_KEY] = session_id
        print(f"--- ADK Init: Created new session with ID: {st.session_state[ADK_SESSION_KEY]} ---")
        try:
            # Create the initial session record within the ADK session service
            # AWAITING THE ASYNC CALL USING asyncio.run()
            asyncio.run(session_service.create_session(
                app_name=APP_NAME_FOR_ADK,
                user_id=USER_ID,
                session_id=session_id,
                state={},  # Initial ADK session state is empty
            ))
            print(f"--- ADK Init: Successfully created new session in ADK SessionService. ---")
            # AWAITING THE ASYNC CALL USING asyncio.run() FOR DEBUG PRINT
            test_session_after_create = asyncio.run(session_service.get_session(app_name=APP_NAME_FOR_ADK, user_id=USER_ID, session_id=session_id))
            print(f"--- ADK Init: DEBUG - Session immediately after initial creation: {test_session_after_create is not None} ---")
        except Exception as e:
            print(f"--- ADK Init: FATAL ERROR - Could not create initial session in ADK SessionService: {e} ---")
            logging.exception("ADK Session Service create_session failed:")
            raise  # Re-raise to stop app if session can't be created
    else:
        session_id = st.session_state[ADK_SESSION_KEY]
        print(f"--- ADK Init: Reusing existing ADK session ID from Streamlit state: {session_id} ---")
        # AWAITING THE ASYNC CALL USING asyncio.run()
        if not asyncio.run(session_service.get_session(app_name=APP_NAME_FOR_ADK, user_id=USER_ID, session_id=session_id)):
            print(f"--- ADK Init: WARNING - Session {session_id} not found in InMemorySessionService memory (likely due to script restart). Recreating session. State will be lost. ---")
            try:
                # AWAITING THE ASYNC CALL USING asyncio.run()
                asyncio.run(session_service.create_session(
                    app_name=APP_NAME_FOR_ADK,
                    user_id=USER_ID,
                    session_id=session_id,
                    state=INITIAL_STATE  # Recreated session starts with initial state
                ))
                # AWAITING THE ASYNC CALL USING asyncio.run() FOR DEBUG PRINT
                test_session_after_recreate = asyncio.run(session_service.get_session(app_name=APP_NAME_FOR_ADK, user_id=USER_ID, session_id=session_id))
                print(f"--- ADK Init: DEBUG - Session immediately after recreation: {test_session_after_recreate is not None} ---")
            except Exception as e:
                print(f"--- ADK Init: ERROR - Could not recreate missing session {session_id} in ADK SessionService: {e} ---")
                logging.exception("ADK Session Service recreation failed:")

    print(f"--- ADK Init: Initialization sequence complete. Runner is ready. Active Session ID: {session_id} ---")
    return runner, session_id


async def run_adk_async(runner: Runner, session_id: str, user_message_text: str) -> str:
    """
    Asynchronously executes one turn of the ADK agent conversation.

    Args:
        runner: The initialized ADK Runner.
        session_id: The current ADK session ID.
        user_message_text: The text input from the user for this turn.

    Returns:
        The agent's final text response as a string.
    """
    print(f"\n--- ADK Run: Starting async execution for session {session_id} ---")
    print(f"--- ADK Run: Processing User Query (truncated): '{user_message_text[:150]}...' ---")

    # Retrieve the ADK session object to update its state
    session = await runner.session_service.get_session(app_name=APP_NAME_FOR_ADK, user_id=USER_ID, session_id=session_id)
    if not session:
        return "Error: ADK session not found. Please refresh the page."

    print(f"--- ADK Run: Session state BEFORE agent run: {session.state} ---")
    print(f"--- ADK Run: Updated ADK session state with Streamlit inputs: {session.state} ---")

    # Format the user's message for the ADK runner
    content = genai_types.Content(
        role='user',
        parts=[genai_types.Part(text=user_message_text)]
    )
    final_response_text = "[Agent encountered an issue and did not produce a final response]"
    start_time = time.time()  # Start timing

    try:
        async for event in runner.run_async(user_id=USER_ID, session_id=session_id, new_message=content):
            if event.is_final_response():
                print(f"--- ADK Run: Final response event received. ---")
                # Extract text from the final response event
                if event.content and event.content.parts and hasattr(event.content.parts[0], 'text'):
                    final_response_text = event.content.parts[0].text
                else:
                    final_response_text = "[Agent finished but produced no text output]"
                    print(f"--- ADK Run: WARNING - Final event received, but no text content found. Event: {event} ---")
                break  # Stop iterating after the final response
    except Exception as e:
        print(f"--- ADK Run: !! EXCEPTION during agent execution: {e} !! ---")
        logging.exception("ADK runner.run_async failed:")
        final_response_text = f"Sorry, an error occurred while processing your request: {e}"

    end_time = time.time()
    duration = end_time - start_time
    print(f"--- ADK Run: Turn execution completed in {duration:.2f} seconds. ---")
    print(f"--- ADK Run: Final Response (truncated): '{final_response_text[:150]}...' ---")
    return final_response_text


def run_adk_sync(runner: Runner, session_id: str, user_message_text: str) -> str:
    """
    Synchronous wrapper that executes the asynchronous run_adk_async function.
    """
    return asyncio.run(run_adk_async(runner, session_id, user_message_text))


print("✅ ADK Service initialization and helper functions defined.")