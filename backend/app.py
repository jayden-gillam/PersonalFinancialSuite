from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/income")
def get_income():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Income;")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


