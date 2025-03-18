from flask import Flask, jsonify, request
from database import cadastrar_usuario

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

if __name__ == "__main__":
    app.run(debug=True, port=5001)
