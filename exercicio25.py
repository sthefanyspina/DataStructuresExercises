#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
# escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
# ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_conta = int(input("Digite o número da sua conta: "))
saldo = int(input("Digite o saldo da sua conta: "))
debito = int(input("Qual a quantidade de debito da sua conta: "))
credito = int(input("Qual a quantidade de credito da sua conta: "))
saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print(f"Seu saldo atual é de {saldo_atual}. Saldo Positivo")
else:
    print(f"Seu saldo atual é de {saldo_atual}. Saldo Negativo")