
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://unifor703:unifor@cluster0.9hdml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_DATABASE = "n703_db"
MONGODB_COLLECTION = "users"

try:
    client = MongoClient(URI)
    db = client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION]
except Exception as e:
    print(f"Erro ao conectar com MongoDB: {str(e)}")


def cadastrar_usuario(nome, email, cpf, status):
    try:
        if collection.find_one({"user_cpf": cpf}):
            return 409, f"O CPF informado ja esta cadastrado"
        if collection.find_one({"user_email": email}):
            return 409, f"Email {email} ja cadastrado"
        
        dados_usuario = {"user_name": nome, "user_email": email, "user_cpf": cpf, "user_status": status}
        collection.insert_one(dados_usuario)
        
        return 200, None
    except Exception as e:
        return 500, f"Erro: {str(e)}", None
    
