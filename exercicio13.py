#Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
#Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.

nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))

mediaPonderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
print(mediaPonderada)