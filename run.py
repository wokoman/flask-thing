import multiprocessing
import subprocess
import sys
import time
from config import FLASK_PORT, STREAMLIT_PORT, FLASK_HOST, STREAMLIT_HOST

def run_flask():
    from app import app
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False)

def run_streamlit():
    # Wait a moment for Flask to start
    time.sleep(2)
    # Run streamlit using subprocess to handle its CLI interface
    subprocess.run([
        "streamlit", 
        "run", 
        "frontend.py",
        "--server.port", str(STREAMLIT_PORT),
        "--server.address", STREAMLIT_HOST,
        "--server.headless", "true"  # Run in headless mode
    ])
    
if __name__ == "__main__":
    print(f"Starting Flask backend on port {FLASK_PORT}")
    flask_process = multiprocessing.Process(target=run_flask)
    flask_process.start()
    
    try:
        print(f"Starting Streamlit frontend on port {STREAMLIT_PORT}")
        run_streamlit()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        flask_process.terminate()
        flask_process.join()
        sys.exit(0) 