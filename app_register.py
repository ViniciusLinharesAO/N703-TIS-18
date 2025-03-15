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
        return 200, "Sucesso"
    except sqlite3.IntegrityError:
        return 409, "Este email já está cadastrado"
    except sqlite3.OperationalError:
        return 500, "O database está locked"
    except Exception as e:
        return 500, "Erro inesperado"


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    code, error_message = add_user(name, email)
    if code == 200:
        return jsonify({"message": "Usuário cadastrado com sucesso"}), 201
    elif code == 409:
        return jsonify({"error": error_message}), 409
    elif code == 500:
        return jsonify({"error": error_message}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
