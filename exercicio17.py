#Ler as notas da 1a. e 2a. avaliações de um aluno. 
# Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). 
# Escrever também a média calculada. 

nota1 = int(input("Qual o valor da primeira nota?"))
nota2 = int(input("Qual o valor da segunda nota?"))

media = (nota1 + nota2) / 2

if media > 6:
    print(f"aluno aprovado com média {media}")
else:
    print(f"aluno reprovado com média {media}")