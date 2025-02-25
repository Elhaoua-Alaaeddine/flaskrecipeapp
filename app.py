import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running on Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get Railway-assigned port or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
