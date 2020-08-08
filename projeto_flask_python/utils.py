from models import Pessoa

def insere_pessoas():
    pessoa = Pessoa(nome="Leonardo", idade=29)    
    pessoa.save()
    
def consulta():
    pessoa = Pessoa.query.all()
    pessoa2 = Pessoa.query.filter_by(nome="Leonardo").first()

def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome="Leonardo").first()
    pessoa.idade = 30
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome="Leonardo").first()
    pessoa.delete();

if __name__ == "__main__":
    insere_pessoas()
    consulta()
    altera_pessoa()
    exclui_pessoa()