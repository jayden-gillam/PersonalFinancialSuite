from flask import Flask, jsonify, request
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


@app.route("/income", methods=["POST"])
def add_income():
    data = request.get_json()

    income_source = data["income_source"]
    gross_amount = data["gross_amount"]
    net_amount = data["net_amount"]
    income_date = data["income_date"]
    income_notes = data["income_notes"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO INCOME (income_source, gross_amount, net_amount, income_date, income_notes)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (income_source, gross_amount, net_amount, income_date, income_notes)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Income added successfully"}), 201


