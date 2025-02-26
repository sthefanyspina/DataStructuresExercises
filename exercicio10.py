#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

custoFabrica = int(input("Qual o custo de fabrica do carro:"))
percentualDistribuidor = custoFabrica * 28/100
impostos = custoFabrica * 45/100

carroNovo = custoFabrica + percentualDistribuidor + impostos
print(carroNovo)