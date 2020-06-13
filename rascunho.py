#   name = "relembrando"


#    def setName(self,new_name):
#        self.name = new_name
"""class Teste:
    def __ini__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = self.new_name
    def getNome():
        return self.name
"""
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

