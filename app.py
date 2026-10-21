import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from pymongo.errors import PyMongoError

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api")
def api():
    with (BASE_DIR / "data" / "api_data.json").open(encoding="utf-8") as file:
        return jsonify(json.load(file))


@app.get("/todo")
def todo():
    return render_template("todo.html")


@app.post("/submittodoitem")
def submit_todo_item():
    item_name = request.form.get("itemName", "").strip()
    item_description = request.form.get("itemDescription", "").strip()
    if not item_name or not item_description:
        return {"error": "Item Name and Item Description are required."}, 400

    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        return {"error": "MONGO_URI is missing from the .env file."}, 500

    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        database = client[os.getenv("MONGO_DB_NAME", "git_github_assignment")]
        result = database.todo_items.insert_one(
            {"itemName": item_name, "itemDescription": item_description}
        )
    except PyMongoError as error:
        return {"error": str(error)}, 500

    return {"message": "To-Do item saved", "id": str(result.inserted_id)}, 201


if __name__ == "__main__":
    app.run(debug=True)
