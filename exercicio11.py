#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
# mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
# efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
# vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
# vendedor.

salario = int(input("Digite o valor de seu salario: "))
quantidade_vendas = int(input("Quantos carros foram vendidos? "))
valor_total = int(input("Qual o valor total de suas vendas? "))
valor_carro_vendido = int(input("Qual o valor recebido por venda de carro? "))

comissao = valor_carro_vendido * quantidade_vendas
comissao_vendas = valor_total * 0.05

salario_final = salario + comissao + comissao_vendas
print(salario_final)