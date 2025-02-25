from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/get-recipe", methods=["POST"])
def get_recipe():
    data = request.json  # Expecting a JSON body with ingredients
    ingredients = data.get("ingredients", [])

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    # Dummy recipe logic (Replace this with real recipe fetching logic)
    recipe = {
        "title": "Random Dish",
        "ingredients": ingredients,
        "instructions": "Mix everything and cook!"
    }

    return jsonify(recipe)

if __name__ == "__main__":
    app.run(debug=True)
