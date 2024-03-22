import json

from flask import Flask, request, jsonify
import uuid
from points import get_total_receipt_points
from validations import validate_receipt

server = Flask(__name__)

receipts_data = {}
receipts = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }, {
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
            }, {
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
            }, {
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
            }, {
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
            }
        ],
        "total": "35.35"
    }
@server.route("/receipts/process")
def example():
    #if request.method=="PUT":
    return jsonify(receipts)
@server.route("/receipts/process", methods=["POST"])
def get_data():
    #data = request.form["author"]
    receipt = request.get_json()
    validation_result = validate_receipt(receipt)
    if not validation_result.is_valid:
        return jsonify(error="The receipt is invalid", message=validation_result.message), 400
    receipt_id = str(uuid.uuid4())
    points = get_total_receipt_points(receipt)
    receipts_data[receipt_id] = points
    return jsonify(id=receipt_id), 201
    #data = json.loads(data)

@server.route("/receipts/<id>/points", methods=["GET"])
def get_points(id: str):
    points = receipts_data.get(id)

    if points is None:
        return jsonify(error="No receipt found for that id"), 404
    return jsonify(points=points)


if __name__ == "__main__":
    server.run(host='0.0.0.0')