#Ler um valor e escrever se é positivo, negativo ou zero

valor = int(input("Digite o valor que deseja verificar:"))

if valor > 0:
    print("O número é positivo")
elif valor == 0:
    print("O número é zero")
else:
    print("O número é negativo")