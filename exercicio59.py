#Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

for i in range(10):
    valor = int(input("Informe um valor:"))
if valor > 0:
    print(f"O número {valor} é positivo")
else:
    print(f"O número {valor} é negativo")
