import os

# Server configuration
FLASK_PORT = 5000  # Changed to standard Flask port
STREAMLIT_PORT = 8501  # Changed back to standard Streamlit port
FLASK_HOST = "localhost"  # Only accept local connections since NGINX will proxy
STREAMLIT_HOST = "localhost"  # Only accept local connections since NGINX will proxy

# API URL configuration
LOCAL_DEV = os.getenv('LOCAL_DEV', 'true').lower() == 'true'
API_BASE_URL = f"http://localhost:{FLASK_PORT}" if LOCAL_DEV else "" 