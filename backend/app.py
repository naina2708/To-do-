from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todos"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({"message": "Item saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)