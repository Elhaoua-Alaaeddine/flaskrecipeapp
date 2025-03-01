import os

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Spoonacular API Key
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

@app.route("/")
def home():
    return "Flask Recipe API is live"


@app.route("/recipes", methods=["POST"])
def get_recipes():
    data = request.json
    # Convert list to comma-separated string
    ingredients = ",".join(data.get("ingredients", []))

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={SPOONACULAR_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        recipes = response.json()
        return jsonify(recipes)


    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch recipes", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
