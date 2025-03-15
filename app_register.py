import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)

def add_user(name, email):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    if add_user(name, email):
        return jsonify({"message": "Usuário cadastrado com sucesso"}), 201
    else:
        return jsonify({"error": "Erro ao cadastrar usuário"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
