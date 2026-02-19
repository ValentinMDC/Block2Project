from flask import Flask, request, jsonify, render_template
from passwordStrengthChecker import check_password_strength
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)