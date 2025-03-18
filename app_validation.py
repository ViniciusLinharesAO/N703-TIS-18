from flask import Flask, jsonify, request
from database import cadastrar_usuario
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://unifor703:unifor@cluster0.9hdml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_DATABASE = "n703_db"
MONGODB_COLLECTION = "users"

app = Flask(__name__)


def connect_collecion(URI,MONGODB_DATABASE,MONGODB_COLLECTION):
    try:
        client = MongoClient(URI)
        db = client[MONGODB_DATABASE]
        collection = db[MONGODB_COLLECTION]
        return collection
    except Exception as e:
        print(f"Erro ao conectar com MongoDB: {str(e)}")

def update_user_status(cpf,status):
    collection = connect_collecion(URI,MONGODB_DATABASE,MONGODB_COLLECTION)
    if collection is None:
        return 500, "Erro na conexao com o banco de dados"
    try:
        user = collection.find_one({"user_cpf": cpf})
        if not user:
            return 404, "O CPF informado não consta na base de dados"
        if user.get("user_status") == status:
            return 200, f"O status do usuario ja consta como '{status}'"
        collection.update_one(
            {"user_cpf": cpf}, 
            {"$set": {"user_status": status}}
        )
        return 200, f"Status do usuario atualizado para '{status}'"

    except Exception as e:
        return 500, f"Erro: {str(e)}"

@app.route("/atualiza_situacao/<cpf>", methods=["PUT"])
def update_status(cpf):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON inválido ou campo 'status' ausente"}), 400
        status = data["user_status"]
        if status not in ["I", "A"]:
            return jsonify({"error": "O status deve ser 'A' ou 'I'"}), 400

        status_code, message = update_user_status(cpf, status)

        return jsonify({"message": message}), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5003)
