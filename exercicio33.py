#Ler dois valores e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.

valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))

if valor1 == valor2:
    print("Números iguais")
elif valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
else:
    print(f"{valor2} é maior que {valor1}")