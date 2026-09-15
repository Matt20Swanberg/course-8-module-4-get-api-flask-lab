from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


@app.route("/")
def home():
    """
    Return a welcome message for the homepage.
    
    Returns:
        Response: A JSON welcome message with a 200 status code.
    """
    return jsonify({"message": "Welcome to my homepage"}), 200

@app.route("/products")
def get_products():
    """
    Return all products or filter products by category.
    Returns:
        Response: A JSON list of all products or products matching
        the specified category with a 200 status code.
    """

    # Gets the optional category query parameter from the URL
    category_filter = request.args.get('category')

    # Filters products when a category is provided
    if category_filter:
        filtered_products = [
            p for p in products if p['category'].lower() == category_filter.lower()
        ]
        return jsonify(filtered_products), 200
        
    # Returns all products when no category filter is provided
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):
    """
    Return a specific product by its ID.
    
    Args:
        id (int): The ID of the product to retrieve.
        
    Returns:
        Response: The matching product as JSON with a 200 status code,
        or an empty JSON object with a 404 status code if not found.
    """
    # Searches for a product with an ID matching the requested ID
    product = next((p for p in products if p['id'] == id), None)

    # Returns a 404 response if no matching product is found
    if product is None:
        return jsonify({}), 404

    # Returns the matching product
    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)
