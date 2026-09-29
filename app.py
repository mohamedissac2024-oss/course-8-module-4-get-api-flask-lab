from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Homepage route - welcome message so we can confirm the API is up
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API!"}), 200


# Collection route - returns every product, or only the ones in a category
# when the optional ?category= query string is provided (case-insensitive)
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        results = [
            product
            for product in products
            if product["category"].lower() == category.strip().lower()
        ]
    else:
        results = products

    return jsonify(results), 200


# Single resource route - looks the product up by id, and returns a JSON
# error body with a 404 when no product matches
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((item for item in products if item["id"] == id), None)

    if product is None:
        return jsonify({"error": f"Product with id {id} not found"}), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
