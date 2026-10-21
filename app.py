import json
from pathlib import Path

from flask import Flask, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api")
def api():
    with (BASE_DIR / "data" / "api_data.json").open(encoding="utf-8") as file:
        return jsonify(json.load(file))


if __name__ == "__main__":
    app.run(debug=True)
