#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente. 

valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))

if valor1 > valor2 and valor2 > valor3:
    print(f"{valor1}, {valor2},{valor3}")
elif valor1 > valor2 and valor3 > valor2:
    print(f"{valor1}, {valor3},{valor2}")
elif valor2 > valor1 and valor1 > valor3:
    print(f"{valor2}, {valor1},{valor3}")
elif valor2 > valor1 and valor3 > valor1:
    print(f"{valor2}, {valor3},{valor2}")
elif valor3 > valor1 and valor1 > valor2:
    print(f"{valor3}, {valor1},{valor2}")
else:
    print(f"{valor3}, {valor2},{valor1}")