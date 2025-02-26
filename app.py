import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Spoonacular API Key
SPOONACULAR_API_KEY = "0c3e10f27f214d4885091db6c42ad96f"

@app.route("/")
def home():
    return "Flask Recipe API is live"

@app.route("/recipes", methods=["POST"])
def get_recipes():
    data = request.json
    ingredients = ",".join(data.get("ingredients", []))  # Convert list to comma-separated string

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={SPOONACULAR_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        recipes = response.json()
        return jsonify(recipes)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
