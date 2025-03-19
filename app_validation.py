from flask import Flask, jsonify, request
from database import cadastrar_usuario
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

#URI = "mongodb+srv://unifor703:unifor@cluster0.9hdml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#MONGODB_DATABASE = "n703_db"
#MONGODB_COLLECTION = "users"

app = Flask(__name__)

@app.route("/atualiza_situacao_integracao/<cpf>", methods=["PUT"])
def update_status(cpf):
    try:
        url = f"http://localhost:5001/atualiza_situacao/{cpf}"
        data = request.get_json()
        status = data["user_status"]
        response = requests.put(url, json={"user_status": status})
        if response.status_code == 200:
            return jsonify({"mensagem": "Status atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5003)
