from flask import Flask
from flask.globals import request
from flask.json import jsonify
import json

app = Flask(__name__)

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

@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Dev com ID: {} não existe".format(id)
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro não previsto"
            response = {"status": "erro", "mensagem": mensagem}
        return jsonify(response)

    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
        
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"mensagem": "Registro excluído com sucesso"})

@app.route("/dev/", methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify({"status": "sucesso", "mensagem": "registro inserido"})
    elif request.method == "GET":
        return jsonify(desenvolvedores)    

if __name__ == "__main__":
    app.run()