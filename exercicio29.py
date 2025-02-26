#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores. 

valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))

if valor1 > valor2 and valor1 > valor3:
    if valor2 > valor3:
        print(valor1 + valor2)
    else:
        print(valor1 + valor3)
elif valor2 > valor1 and valor2 > valor3:
    if valor1 > valor3:
        print(valor2 + valor1)
    else:
        print(valor2 + valor3)
else:
    if valor1 > valor2:
        print(valor3 + valor1)
    else:
        print(valor3 + valor2)