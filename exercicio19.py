# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles. 

valor1 = int(input("Digite o primeiro número:"))
valor2 = int(input("Digite o segundo número:"))

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor1 == valor2:
    print("Os valores são iguais")
else:
    print(f"{valor2} é maior que {valor1}")