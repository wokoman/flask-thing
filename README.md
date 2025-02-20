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

Run both Flask backend and Streamlit frontend with a single command:

```bash
python run.py
```

This will:
- Start Flask backend on port 5000
- Launch Streamlit frontend on port 8501
- Both services will be accessible via HTTP

## Deployment Notes

- Application is designed to run in containerized environments
- Flask backend exposes REST API on port 5000
- Streamlit frontend serves UI on port 8501
- No browser automation or local dependencies required

## Running as a Service

Create a systemd service file:
```ini
# /etc/systemd/system/flask-streamlit.service
[Unit]
Description=Flask Streamlit Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/app
Environment="LOCAL_DEV=false"
ExecStart=/home/ubuntu/app/.venv/bin/python /home/ubuntu/app/run.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable flask-streamlit
sudo systemctl start flask-streamlit
```

## Environment Variables

- `LOCAL_DEV`: Controls API URL configuration
  - `true` (default): Uses direct Flask URL for local development
  - `false`: Uses relative paths for production/NGINX setup

Example for production:
```bash
export LOCAL_DEV=false
python run.py
```

## API Endpoints

- `/api/endpoint1`