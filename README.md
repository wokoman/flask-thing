
# Flask + Streamlit Demo App

A demo application showing integration between Flask API backend and Streamlit frontend with dynamic responses and image generation.

## Setup

```bash
# Create virtual environment using uv
uv venv .venv

# Activate virtual environment
source .venv/bin/activate  # Unix/MacOS
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -r requirements.txt
```

## Running the Application

1. Start Flask backend (port 8025):

    ```bash
    python app.py
    ```

2. In a new terminal, start Streamlit frontend:

    ```bash
    streamlit run frontend.py
    ```

## API Endpoints

- `/api/endpoint1` - Generates autopilot status with random flight parameters
- `/api/endpoint2` - Provides weather analysis with random conditions
- `/api/endpoint3` - Returns navigation updates with random flight details
- `/api/endpoint4` - Serves random images from Lorem Picsum API

## Commands

Available text commands in Streamlit interface:

- `status` or `autopilot` - Flight status
- `weather` - Weather conditions
- `navigation` or `route` - Flight details
- `image` - Random photo from Lorem Picsum

## Features

- Flask backend with dynamic text generation using Faker
- Streamlit frontend with typing animation
- Real-time image fetching from Lorem Picsum
- Command history with clear functionality
- Simulated processing delays with spinners
