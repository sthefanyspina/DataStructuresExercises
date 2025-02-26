#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor do novo salário. 

salario = int(input("Digite o valor do salario atual:"))
reajuste = int(input("Digite a porcentagem do reajuste:"))

porcentagemReajuste = reajuste / 100
valorPorcentagem = salario * porcentagemReajuste
novoSalario = salario + valorPorcentagem

print(novoSalario)