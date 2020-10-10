""" #   name = "relembrando"


#    def setName(self,new_name):
#        self.name = new_name
class Teste:
    def __ini__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = self.new_name
    def getNome():
        return self.name

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def getNome(self):
        return self.name
a = Snake("teste")
print(a.name)
a.change_name("vinicius")
print(a.getNome())
"""
def leiaint(msg):
    while True:

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho("Sistema Financeiro v1.0")
    c = 0
    for item in lista:
        print(f"{c} - {item}")
        c +=1
    print(linha)

menu(['Sair', 'Contas a pagar','Contas a receber', 'Grava', 'Lẽ'])
