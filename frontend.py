import streamlit as st
import requests
import time
import random

st.title("Flight Control System")
st.subheader("Natural Language Flight Control")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""
if 'last_input' not in st.session_state:
    st.session_state.last_input = ""

def clear_history():
    st.session_state.messages = []
    st.session_state.prompt = ""
    st.session_state.last_input = ""

# Function to make API calls
def call_endpoint(endpoint):
    try:
        response = requests.get(f"http://localhost:8025/api/{endpoint}")
        return response.json()  # Return the full JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")
        return None

# Update the help text
st.markdown("""
Try these commands:
- Type "status" or "autopilot" for flight status
- Type "weather" for weather conditions
- Type "navigation" or "route" for flight details
- Type "image" for a random high-quality photo
""")

# Text input for prompts
prompt = st.text_input("Enter your command:", key="prompt")

# Process the prompt when user hits enter
if prompt and (prompt != st.session_state.last_input or 'image' in prompt.lower()):
    st.session_state.last_input = prompt
    response = None
    if any(word in prompt.lower() for word in ["status", "autopilot"]):
        with st.spinner('Processing request...'):
            time.sleep(random.uniform(0.5, 2.0))
            response = call_endpoint("endpoint1")
            response = response['text'] if response else None
    elif "weather" in prompt.lower():
        with st.spinner('Analyzing weather data...'):
            time.sleep(random.uniform(0.5, 2.0))
            response = call_endpoint("endpoint2")
            response = response['text'] if response else None
    elif any(word in prompt.lower() for word in ["navigation", "route"]):
        with st.spinner('Calculating route...'):
            time.sleep(random.uniform(0.5, 2.0))
            response = call_endpoint("endpoint3")
            response = response['text'] if response else None
    elif "image" in prompt.lower():
        with st.spinner('Fetching image...'):
            time.sleep(random.uniform(0.5, 2.0))
            response = call_endpoint("endpoint4")  # Keep full response for images
    else:
        st.warning("Command not recognized. Please try one of the suggested commands.")
    
    if response:
        # Add new message to history immediately
        st.session_state.messages.append({"prompt": prompt, "response": response})
        
        # Create a new container for the typing animation
        st.markdown("### Latest Response")
        with st.empty():
            displayed_response = ""
            for char in response:
                displayed_response += char
                st.markdown(f"{displayed_response}▌")
                time.sleep(0.001)
            # Final display without cursor
            st.markdown(displayed_response)
            
            # If this is an image response, display the image
            if isinstance(response, dict) and 'image_url' in response:
                st.image(response['image_url'], caption="Random Photo")

# Display conversation history
st.markdown("### Previous Responses")
for message in list(reversed(st.session_state.messages))[1:]:
    st.markdown(f"**Command:** {message['prompt']}")
    if isinstance(message['response'], dict) and 'image_url' in message['response']:
        st.text(message['response']['text'])
        st.image(message['response']['image_url'], caption="Random Photo")
    else:
        st.text(message['response'])
    st.markdown("---")

# Add a clear button with callback
st.button("Clear History", on_click=clear_history) 