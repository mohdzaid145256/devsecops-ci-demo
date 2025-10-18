from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DevSecOps CI/CD Demo App!"

@app.route('/health')
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    # Important for Render: bind to 0.0.0.0, not localhost
    app.run(host="0.0.0.0", port=5000)

