#Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. 
# Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

n = int(input("Digite o número desejado:"))

if n < 0:
  n = int(input("Digite o número desejado:"))
else:
    contador = 1
    while contador <= n:
        print(f"{contador}")
        contador += 1