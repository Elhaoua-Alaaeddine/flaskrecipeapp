import os
from io import BytesIO

import requests
from flask import Flask, jsonify, request, send_file
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
    ingredients = ",".join(data.get("ingredients", []))

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={SPOONACULAR_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        recipes = response.json()

        # Modify image URLs to go through our proxy
        for recipe in recipes:
            if "image" in recipe:
                recipe["image"] = f"{request.host_url}proxy-image?url={recipe['image']}"

        return jsonify(recipes)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route("/proxy-image")
def proxy_image():
    """Fetches images through backend to prevent CORS issues."""
    image_url = request.args.get("url")
    if not image_url:
        return jsonify({"error": "No image URL provided"}), 400

    response = requests.get(image_url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch image"}), 500

    return send_file(BytesIO(response.content), mimetype="image/jpeg")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
