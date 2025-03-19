
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
    
def listar_usuarios():
    try:
        # Busca todos os usuários no banco
        usuarios = list(collection.find({}, {"_id": 0}))
        
        if not usuarios:
            return 404, "Nenhum usuário encontrado", []
        
        return 200, None, usuarios
    except Exception as e:
        return 500, f"Erro ao listar usuários: {str(e)}", []
    
def atualizar_status(cpf,status):
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