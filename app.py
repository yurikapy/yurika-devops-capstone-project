from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify(message="Hello World")

@app.route("/accounts", methods=["POST"])
def create_account():
    account_data = request.get_json()
    # Simulasi pembuatan account
    return jsonify(account_data), 201

@app.route("/accounts", methods=["GET"])
def list_accounts():
    # Simulasi daftar account
    accounts = [{"id": 1, "name": "Account 1", "balance": 100.0}]
    return jsonify(accounts)

if __name__ == "__main__":
    app.run(debug=True)
