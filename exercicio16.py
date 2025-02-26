#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra. 

applequantity = int(input("Quantas maçãs serão compradas?"))

if applequantity < 12:
    print(applequantity * 1.30)
else:
    print(applequantity * 1.00)