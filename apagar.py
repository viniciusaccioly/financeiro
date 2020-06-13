class Apagar:

    def __init__(self, descricao, valor, quantidade, vencimento):
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade
        self.vencimento = vencimento

    def setDescricao(self,new_descricao):
        self.descricao = new_descricao

    def getDescricao(self):
        return self.descricao

    def setValor(self,newValor):
        self._valor += newValor

    def getValor(self):
        return self.valor

    def setQuantidade(self, new_qtd):
        self.quantidade = new_qtd
    def getQuantidade(self):
        return self.quantidade
        
    def setVencimento(self,new_vencimento):
        self.quantidade = vencimento
    def getVencimento(self):
        return self.vencimento

    def __str__(self):
        return f'{self.descricao}; {self.valor}; {self.quantidade}; {self.vencimento}'
