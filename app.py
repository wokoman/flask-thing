from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Fixed responses for each endpoint
ENDPOINT_RESPONSES = {
    "endpoint1": "Autopilot is engaged. Current altitude: 30,000 feet, Speed: 500 knots",
    "endpoint2": "Weather conditions: Clear skies, Wind speed: 15 knots, Temperature: 15°C",
    "endpoint3": "Navigation status: On course, ETA: 2 hours 15 minutes, Distance to destination: 1,000 NM"
}


def get_random_text(endpoint_name):
    return f"From {endpoint_name}: {ENDPOINT_RESPONSES[endpoint_name]}"


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
    # Listen on port 8888 on all interfaces with debug mode enabled
    app.run(host="0.0.0.0", port=8888, debug=True)
