#Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo): 
#C/5 = F-32 / 9

fahrenheit = int(input("Digite a temperatura:"))

celsius = ((fahrenheit - 32) * 5) / 9
print(celsius)