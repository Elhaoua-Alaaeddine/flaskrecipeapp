import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Recipe API is live!"

@app.route("/recipes", methods=["POST"])
def get_recipes():
    data = request.json
    ingredients = data.get("ingredients", [])

    # Placeholder response (we'll improve this later)
    recipes = [
        {"name": "Pasta", "ingredients": ["pasta", "tomato", "cheese"]},
        {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"]},
    ]
    
    # Filter recipes that match at least one ingredient
    matching_recipes = [r for r in recipes if any(i in r["ingredients"] for i in ingredients)]

    return jsonify({"recipes": matching_recipes})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
