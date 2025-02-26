#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
# dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input("Quantos anos você tem:"))
meses = int(input("Quantos meses você tem:"))
dias = int(input("Quantos dias você tem:"))

transformar = (anos * 365) + (meses * 30) + dias
print(transformar)