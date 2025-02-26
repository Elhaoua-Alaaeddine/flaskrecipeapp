import os

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample recipe database
RECIPES = [
    {"name": "Pasta", "ingredients": ["pasta", "tomato", "cheese"]},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"]},
    {"name": "Omelette", "ingredients": ["egg", "cheese", "butter"]},
]

@app.route("/")
def home():
    return "Flask Recipe API is live!"

@app.route("/recipes", methods=["POST"])
def get_recipes():
    data = request.json
    ingredients = set(data.get("ingredients", []))  # Convert to set for easy matching

    # Find recipes that use at least 1 ingredient
    matched_recipes = [
        recipe for recipe in RECIPES
        if ingredients.intersection(recipe["ingredients"])
    ]

    return jsonify({"recipes": matched_recipes})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
