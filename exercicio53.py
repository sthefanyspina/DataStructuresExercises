#Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO. 

n = int(input("Digite o número desejado:"))

contador = 1
while contador <= n:
    print(f"{contador}")
    contador += 1