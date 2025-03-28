from flask import Flask, jsonify, request

import requests

app = Flask(__name__)

api_base_url = 'http://localhost:5001'
api_key = '3cdea1b06e8f4c08213ca4cbd702a27871914c971ee226cf9debf88b8435c375'

@app.route("/list_users", methods=["GET"])
def view_users():
    try:
        response = requests.get(api_base_url+"/users", headers={"X-API-KEY": api_key})
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Obtém os dados JSON da resposta
            data = response.json()
            users = data.get('usuarios', [])

            # Formata conforme necessário
            user_list = [{"id": u.get('user_cpf'),
                         "name": u.get('user_name'),
                         "email": u.get('user_email'),
                         "status":u.get('user_status')} for u in users]

            return jsonify(user_list), 200
        else:
            return jsonify({"erro": f"Erro na API: {response.status_code}"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"erro": f"Erro de conexão: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500

@app.route("/atualiza_situacao_integracao/<cpf>", methods=["PUT"])
def update_status(cpf):
    try:
        url = api_base_url+f"/atualiza_situacao/{cpf}"
        data = request.get_json()
        status = data["user_status"]
        response = requests.put(url, json={"user_status": status}, headers={"X-API-KEY": api_key})
        if response.status_code == 200:
            return jsonify({"mensagem": "Status atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5002)
