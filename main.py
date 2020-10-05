from financeiro import Financeiro, financeiroException
from datetime import datetime

#pendentes = []
#1
# areceber = []
contas = Financeiro()

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

