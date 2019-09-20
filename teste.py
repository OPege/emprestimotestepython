idade = int(input("Qual é sua idade ? \n"))
if idade > 21 or idade < 65:
	salario = float(input("Digite seu salário: \n"))
	emprestimo = float(input("Qual valor do empréstimo? \n"))
	if salario*10 > emprestimo: print("Empréstimo pré-aprovado!")
	else: print("Salário incompatível pelo valor do empréstimo requerido")  
else: print("Empréstimo negado por idade")