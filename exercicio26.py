#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
# quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
# média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
# a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

estoque_atual = int(input("Qual a quantidade de estoque atual? "))
estoque_maximo = int(input("Qual a quantidade maxima de estoque? "))
estoque_minimo = int(input("Qual a quantidade minima de estoque? "))

quantidade_media = estoque_maximo + estoque_minimo / 2

if estoque_atual <= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")