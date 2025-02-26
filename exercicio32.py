#Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome
# do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
numero_gols_time1 = int(input("Digite o número de gols do primeiro time: "))
numero_gols_time2 = int(input("Digite o número de gols do segungo time: "))

if numero_gols_time1 > numero_gols_time2:
    print(f"O {time1} é o vencedor!")
elif numero_gols_time2 > numero_gols_time1:
    print(f"O {time2} é o vencedor!")
else:
    print(f"{time1} e {time2} empataram!")