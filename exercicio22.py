#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, 
# cujo cálculo é o valor da hora regular com um acréscimo de 50%.
# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva
# o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
# (considere que o mês possua 4 semanas exatas).

horasTrabalhadas = int(input("Qual o número de horas trabalhadas?"))
salario = int(input("Qual o valor da hora do funcionário?"))

horasExtras = horasTrabalhadas - 40

if horasExtras != 0:
    valorHoraExtra = horasExtras * (salario/2)
    print(F"O valor a ser recebido como hora extra é de R${valorHoraExtra}")
else:
    print("Não há hora extra a ser recebida")
