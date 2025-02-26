#Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule
#e mostre seu peso ideal, utilizando as seguintes fórmulas:
#- para sexo masculino: peso ideal = (72.7 * altura) - 58
#- para sexo feminino: peso ideal = (62.1 * altura) - 44.7

nome = input("Qual é o seu nome?")
genero = input("Informe seu genero (F/M):")
altura = float(input("Qual sua altura em metros?"))

if genero == "M":
    pesoIdealMasculino = (72.7 * altura) - 58
    print(f"O seu peso ideal é {pesoIdealMasculino}")
else:
    pesoIdealFeminino = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {pesoIdealFeminino}")
