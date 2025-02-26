#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano. 

anoAtual = 2025
anoNascimento = int(input("Qual o ano de seu nascimento?"))

if (anoAtual - anoNascimento) > 18:
    print("Apto para votar")
else:
    print("Impossibilitado de votar")

