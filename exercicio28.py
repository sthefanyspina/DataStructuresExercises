# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles. 
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))

if valor1 > valor2 and valor1 > valor3:
    print(f"{valor1}")
elif valor2 > valor1 and valor2 > valor3:
    print(f"{valor2}")
else:
    print(f"{valor3}")