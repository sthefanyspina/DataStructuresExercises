#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que
# ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
# ultrapassar este valor, calcular e escrever o seu salário total.

salario = float(input("Qual o valor do seu salario?"))
vendas1 = int(input("Quantas vendas de ate R$1500,00 voce efetuou esse mês?"))
vendas2 = int(input("Quantas vendas efetuou de mais de R$1.500,00 voce efetuou esse mês?"))

totalVendas1 = vendas1 * 0.03
totalVendas2 = vendas2 * 0.05

totalSalario = int(salario) + totalVendas1 + totalVendas2
print(totalSalario)