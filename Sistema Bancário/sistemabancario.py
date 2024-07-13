menu = """\n******** MENU ********

[1]. Depósito
[2]. Saque
[3]. Extrato
[4]. Encerrar operação
\n"""

saldo = 0
limite_saque = 500
extrato = ""
quantidade_saques = 0
LIMITE_QUANTIDADE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("""DEPÓSITO\n""")
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("ERRO: Valor inválido. Por favor, tente novamente.")

    elif opcao == "2":
        print("SAQUE\n")

        valor = float(input("Insira o valor do saque: "))

        if valor > saldo:
            print(f"ERRO: O valor do saque não pode ser maior do que o saldo da conta.")

        if valor <= 0:
            print("ERRO: Valor inválido. Por favor, tente novamente.")

        if valor > 0 and valor <= 500 and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saques += 1

        if valor > 500:
            print("ERRO: O valor solicitado excede o limite desta transação.\n")

        if quantidade_saques >= LIMITE_QUANTIDADE_SAQUES:
            print("ERRO: O número máximo de saques diários já foi realizado.\n")

    elif opcao == "3":
        print("EXTRATO\n")
        print(extrato)
        print(f"SALDO: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida. Por favor, selecione uma das opções disponíveis.")

