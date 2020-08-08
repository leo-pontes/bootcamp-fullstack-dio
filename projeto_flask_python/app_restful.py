from flask import Flask, jsonify
from flask_restful import Resource, Api
from habilidades import Habilidades
from flask_httpauth import HTTPBasicAuth
import json

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

USUARIOS = {
    "Leonardo": "123",
    "Pontes": "321"
}

@auth.verify_password
def verificacao(login, senha):    
    if not (login, senha):
        return False

    return USUARIOS.get(login) == senha

desenvolvedores = [
    {
        "id": "0",
        "nome": "Leonardo",
        "habilidades": ["Python", "Flask"]
    },
    {
        "id": "1",
        "nome": "Pontes",
        "habilidades": ["Python", "Django"]
    }
]

class Desenvolvedor(Resource):
    @auth.login_required
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Dev com ID: {} não existe".format(id)
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro não previsto"
            response = {"status": "erro", "mensagem": mensagem}
        return response

    @auth.login_required
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    @auth.login_required
    def delete(self, id):
        desenvolvedores.pop(id)
        return {"mensagem": "Registro excluído com sucesso"}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    @auth.login_required
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return {"status": "sucesso", "mensagem": "registro inserido"}

api.add_resource(ListaDesenvolvedores, "/dev/")
api.add_resource(Desenvolvedor, "/dev/<int:id>/")
api.add_resource(Habilidades, "/habilidades/")

if __name__ == "__main__":
    app.run()