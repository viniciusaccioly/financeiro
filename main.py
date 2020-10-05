from financeiro import *


pendentes=[]
areceber=[]

contas=Financeiro()

while True:
	try:
	    print("Bem vindo ao sistema financeiro")
	    opcao=int(input("Digite uma opcao: "))
	    if opcao == 1:
		print("Cadastrar a pagar")
		desc= input("Descrição: ")
		valor= int(input("Valor a pagar: "))
		qtd= int(input("Quantas parcelas: "))
		venc= int(input("Dia vencimento: "))
		contas.cadastrarApagar(desc,valor,qtd,venc)
		contas.listarApagar()
		print("Cadastro Efetuado com Sucesso!")
	    else:
		print("Digite novamente")
		break
	   except:
	      print('Nossos engenheiros irão analisar o problema!')
