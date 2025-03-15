import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

@app.route("/users", methods=["GET"])
def view_users():
    users = get_users()
    user_list = [{"id": u[0], "name": u[1], "email": u[2]} for u in users]
    return jsonify(user_list)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
