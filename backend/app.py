from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_connection
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.url_map.strict_slashes = False


@app.route("/income")
def get_income():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    query = "SELECT * FROM Income WHERE 1=1"
    params = []

    if start_date:
        print(start_date)
        start = parse_date(start_date)
        if not start:
            return jsonify({"error": "Invalid start_date format (YYYY-MM-DD)"}), 400
        query += " AND income_date >= %s"
        params.append(start)

    if end_date:
        end = parse_date(end_date)
        if not end:
            return jsonify({"error": "Invalid end_date format (YYYY-MM-DD)"}), 400
        query += " AND income_date <= %s"
        params.append(end)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
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


@app.route("/income/<int:income_id>")
def get_income_by_id(income_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Income WHERE income_id = %s;", (income_id,))
    data = cursor.fetchone()

    conn.close()

    if data is None:
        return jsonify({"error": "Income not found"}), 404

    return jsonify(data)


@app.route("/income/<int:income_id>", methods=["PUT"])
def update_income_by_id(income_id):
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
        UPDATE Income
        SET income_source = %s, gross_amount = %s, net_amount = %s, income_date = %s, income_notes = %s
        WHERE income_id = %s;
        """,
        (income_source, gross_amount, net_amount, income_date, income_notes, income_id)
    )

    conn.commit()
    affected = cursor.rowcount
    conn.close()

    if affected == 0:
        return jsonify({"message": "Income not found"}), 404

    return jsonify({"message": "Income updated successfully"}), 201


# Helper Functions

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
