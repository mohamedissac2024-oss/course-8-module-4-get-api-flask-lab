from flask import Flask, jsonify, request, abort
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API!"})

@app.route("/products")
def get_products():
    category = request.args.get('category')
    filtered = [p for p in products if not category or p['category'].lower() == category.lower()]
    return jsonify(filtered)

@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
