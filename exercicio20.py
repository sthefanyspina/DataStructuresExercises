# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente. 

valor1 = int(input("Digite o primeiro número:"))
valor2 = int(input("Digite o segundo número:"))

if valor1 > valor2:
    print(f"{valor1}, {valor2}")
else:
    print(f"{valor2}, {valor1}")