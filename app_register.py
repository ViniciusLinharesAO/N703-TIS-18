from flask import Flask, jsonify, request
from database import cadastrar_usuario, listar_usuarios, atualizar_status
import requests

app = Flask(__name__)



@app.route("/register", methods=["POST"])
def register():
    dados = request.get_json()
    nome = dados.get("user_name")
    email = dados.get("user_email")
    cpf = dados.get("user_cpf")
    situacao = dados.get("user_status")
    
    if not nome or not email:
        return jsonify({"erro": "Nome e email são obrigatorios"}), 400
    
    codigo, mensagem = cadastrar_usuario(nome, email, cpf, situacao)

    if codigo == 200:
        return jsonify({
            "mensagem": "Usuario cadastrado com sucesso",
        }), 201
    else:
        return jsonify({"erro": mensagem}), codigo
    
@app.route("/users", methods=["GET"])
def list_user():
    codigo, mensagem, usuarios = listar_usuarios()
    
    if codigo == 200:
        return jsonify({
            "usuarios": usuarios,
            "total": len(usuarios)
        }), 200
    else:
        return jsonify({"erro": mensagem}), codigo

@app.route("/atualiza_situacao/<cpf>", methods=["PUT"])
def update_status(cpf):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON inválido ou campo 'status' ausente"}), 400
        status = data["user_status"]
        if status not in ["I", "A"]:
            return jsonify({"error": "O status deve ser 'A' ou 'I'"}), 400

        status_code, message = atualizar_status(cpf, status)

        return jsonify({"message": message}), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)
