#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. 
#Calcular e escrever o percentual que cada um representa em relação ao totaL de eleitores. 

totalDeEleitores = int(input("Qual o número total de eleitores:"))
totalDeVotosBrancos = int(input("Qual o número total de votos brancos:"))
totalDeVotosNulos = int(input("Qual o número total de votos nulos:"))
totalDeVotosValidos = int(input("Qual o número total de votos válidos:"))

porcVotosBrancos = (totalDeVotosBrancos * 100) / totalDeEleitores
porcVotosNulos = (totalDeVotosNulos * 100) / totalDeEleitores
porcVotosValidos = (totalDeVotosValidos * 100) / totalDeEleitores

print(porcVotosBrancos, porcVotosNulos, porcVotosValidos)