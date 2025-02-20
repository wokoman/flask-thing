from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
from faker import Faker
import requests
import time
from config import FLASK_PORT, FLASK_HOST

app = Flask(__name__)
CORS(app)
fake = Faker()

def generate_paragraph():
    return " ".join([fake.sentence() for _ in range(3, 6)])

def get_flight_info():
    return {
        "endpoint1": f"""Autopilot Status Report:
{generate_paragraph()} Current altitude is {fake.random_int(min=25000, max=35000)} feet. {generate_paragraph()} 
Flight systems are {fake.random_element(['nominal', 'optimal', 'functioning within parameters'])}.
{generate_paragraph()}""",
        
        "endpoint2": f"""Weather Analysis:
{generate_paragraph()} Visibility is {fake.random_int(min=5, max=15)} kilometers. {generate_paragraph()}
Atmospheric conditions: {fake.random_element(['stable', 'improving', 'requiring minor adjustments'])}.
{generate_paragraph()}""",
        
        "endpoint3": f"""Navigation Update:
Flight {fake.bothify(text='??###')} from {fake.city()} to {fake.city()}. {generate_paragraph()}
{generate_paragraph()} Estimated arrival in {fake.random_int(min=1, max=12)} hours {fake.random_int(min=0, max=59)} minutes.
{generate_paragraph()}"""
    }

def get_random_text(endpoint_name):
    responses = get_flight_info()
    return f"From {endpoint_name}: {responses[endpoint_name]}"


# API endpoints
@app.route("/api/endpoint1", methods=["GET"])
def endpoint1():
    return jsonify({"text": get_random_text("endpoint1")})


@app.route("/api/endpoint2", methods=["GET"])
def endpoint2():
    return jsonify({"text": get_random_text("endpoint2")})


@app.route("/api/endpoint3", methods=["GET"])
def endpoint3():
    return jsonify({"text": get_random_text("endpoint3")})


@app.route("/api/endpoint4", methods=["GET"])
def endpoint4():
    try:
        # Add random timestamp to force new image each time
        timestamp = int(time.time())
        image_url = f'https://picsum.photos/500/300?random={timestamp}'
        return jsonify({
            "text": f"""Image Request:
A new random image has been retrieved from Lorem Picsum. 
URL: {image_url}""",
            "image_url": image_url
        })
    except Exception as e:
        return jsonify({
            "text": "Error fetching image",
            "error": str(e)
        }), 500


# Frontend chatbot-like interface
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Autopilot Interface</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            button { margin-right: 10px; margin-bottom: 10px; }
            #response { margin-top: 20px; border: 1px solid #ccc; padding: 10px; max-width: 600px; }
        </style>
    </head>
    <body>
        <h1>Autopilot Interface</h1>
        <p>Click a button below to call an API endpoint and display its response.</p>
        <button onclick="callEndpoint('endpoint1')">Call Endpoint 1</button>
        <button onclick="callEndpoint('endpoint2')">Call Endpoint 2</button>
        <button onclick="callEndpoint('endpoint3')">Call Endpoint 3</button>
        <button onclick="callEndpoint('endpoint4')">Call Endpoint 4</button>
        <div id="response">
            <p>Responses will appear here.</p>
        </div>
        <script>
            function callEndpoint(endpoint) {
                fetch('/api/' + endpoint)
                    .then(response => response.json())
                    .then(data => {
                        const responseDiv = document.getElementById('response');
                        responseDiv.innerHTML += '<p>' + data.text + '</p>';
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True)
