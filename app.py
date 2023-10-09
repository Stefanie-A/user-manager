from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "CRUD APP"


if __name__ == "__main_":
    app.run(debug=True)
