from apagar import *

class financeiroException(Exception):
        """Classe de exceção lançada quando uma violação de acesso aos elementos
        do gerenciador é identificado.
        """
        def __init__(self, msg):
            """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
            """
            super().__init__(msg)

class Financeiro:
    def __init__(self):
        self.pendentes=[]
        self.pagas=[]
        self.__saldo = 0


    def cadastrarApagar(self, descricao, valor, quantidade, vencimento):
        try:
            nova_Conta = Apagar(descricao, valor, quantidade, vencimento)
            self.pendentes.append(nova_Conta)
#            return self.pendentes
        except IndexError:
            raise financeiroException (f'Tipo de cadastro inválido!') 
        except:
            raise
    
    """def __str__(self):
        return f'{self.pendentes}'"""
    
    def listarApagar(self):
        if len(self.pendentes) == 0:
            return f'Lista Vazia!'
        else:
            for c in self.pendentes:
                print(c)


