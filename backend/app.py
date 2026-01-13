from flask import Flask
app = Flask(__name__)

@app.route("/transactions")
def get_transactions():
    return transactions
