<<<<<<< HEAD
from financeiro import *
import os
pendentes = []
areceber = []
contas = Financeiro()
=======
from financeiro import Financeiro, financeiroException
from datetime import datetime
>>>>>>> 6b165337d70b95c59de1add3617e18753b2c7efc

#pendentes = []
#1
# areceber = []
contas = Financeiro()

<<<<<<< HEAD
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Bem vindo ao sistema financeiro")
    print("""
1 - Contas a pagar
2 - Contas a receber
3 - Grava (Exportar)
4 - Lê (Importar)
0 - Sair""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


def submenu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
0 - Voltar ao menu anterior
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 4)


def pede_descrição():
    return input("Descrição: ")


def pede_valor():
    return float(input("Valor: "))


def pede_quantidade():
    return int(input("Quantidade: "))


def pede_vencimento():
    return int(input("Vencimento: "))


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


def novo():
    #global pendentes
    nome = pede_descrição()
    valor = pede_valor()
    quantidade = pede_quantidade()
    vencimento = pede_vencimento()
    contas.cadastrarApagar(nome, valor, quantidade, vencimento)
    print("Cadastro Efetuado com Sucesso!")
    #pendentes.append([nome, telefone])


""" while True:
    try:
        #contas.listarApagar()
        #print("Cadastro Efetuado com Sucesso!")
    else:
        print("Digite novamente")
        break
    except:
        print('Nossos engenheiros irão analisar o problema!')

1 - Contas a pagar
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
2 - Contas a receber
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
3 - Grava (Exportar)
4 - Lê (Importar)
 """

while True:
    opção = menu()
    # Opção 0 - Sai,  Encerra o sistema
    if opção == 0:
        break

    elif opção == 1:
        submenu()
        if opção == 1:
            novo()
        elif opção == 2:
            print('altera()')
        elif opção == 3:
            print('apaga()')
        elif opção == 4:
            print('lista()')
        elif opção == 0:
            print("Voltando ao menu anterior")
            menu()
    # Opção 1 - Contas a pagar,
    #    1 - Novo
    #    2 - Altera
    #    3 - Apaga
    #    4 - Lista
    #    limpa_tela()
    elif opção == 2:
        print("Contas a receber")
        # Opção 1 - Contas a receber,
        #    1 - Novo
        #    2 - Altera
        #    3 - Apaga
        #    4 - Lista
        #  limpa_tela()
    elif opção == 3:
        print('grava()')
        # 3 - Grava (Exportar para arquivo de dados)
                # limpa_tela()
    elif opção == 4:
        # 4 - Lê (Importar de um arquivo de dados)
        print('le()')
        #  limpa_tela()
=======
def novo_apagar():
	desc = input("Descrição: ")
	valor = float(input("Valor a pagar: "))
	qtd = int(input("Quantas parcelas: "))
	venc = int(input("Dia vencimento: "))
	contas.cadastrarApagar(desc, valor, qtd, venc)
	print("Cadastro Efetuado com Sucesso!")

def valida_faixa_inteiro(pergunta, inicio, fim):
	while True:
		try:
			valor= int(input(pergunta))
			if inicio <= valor <= fim:
				return valor
		except ValueError:
			print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
	print("Sistema Finaceiro", datetime.today())
	print("""
1 - Cadastrar Contas a pagar;
2 - Cadastrar Contas a receber;
3 - Lista;
4 - Grava (exportar);
5 - Le (importar);
0 - Sai
""")
	return valida_faixa_inteiro("Escolha uma opção: ", 0,6)

while True:
	opção = menu()
	if opção == 0:
		break
	elif opção == 1:
		novo_apagar()
	elif opção == 2:
		alterar()
	elif opção == 3:
		lista()
	elif opção == 4:
		grava()
	elif opção == 5:
		le()

>>>>>>> 6b165337d70b95c59de1add3617e18753b2c7efc
