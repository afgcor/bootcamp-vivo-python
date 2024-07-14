def menu():
    menu = """\n******** MENU ********
    
    [1]. Realizar depósito
    [2]. Realizar saque
    [3]. Visualizar extrato
    [4]. Cadastrar usuário
    [5]. Cadastrar conta
    [6]. Listar usuários
    [7]. Listar contas
    [8]. Remover usuário
    [9]. Remover conta
    [0]. Encerrar operação"""
    print(menu)
    return input(f"\nEscolha uma opção: ")

def sistema():
    saldo = 0
    limite_saque = 500
    extrato = ""
    usuarios = []
    contas = []
    quantidade_saques = 0
    LIMITE_QUANTIDADE_SAQUES = 3
    
    while True:
        opcao = menu()

        if opcao == "1":
            print(f"DEPÓSITO\n")
            valor = float(input(f"Insira o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "2":
            print(f"SAQUE\n")
            valor = float(input(f"Insira o valor do saque: "))
            saldo, extrato, quantidade_saques = saque(saldo, valor, extrato, quantidade_saques, LIMITE_QUANTIDADE_SAQUES)
        elif opcao == "3":
            visualizar_extrato(saldo, extrato)
        elif opcao == "4":
            cadastrar_usuario(usuarios)
        elif opcao == "5":
            cadastrar_conta(usuarios, contas)
        elif opcao == "6":
            listar_usuarios(usuarios)
        elif opcao == "7":
            listar_contas(contas)
        elif opcao == "8":
            remover_usuario(usuarios, contas)
        elif opcao == "9":
            remover_conta(contas)
        elif opcao == "0":
            break
        else:
            print(f"ERRO: Opção inválida! Por favor, escolha uma das opções disponibilizadas.")

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor;
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado!")
    else:
        print(f"ERRO: Valor inválido. Por favor, tente novamente.\n")
    return saldo, extrato

def saque(saldo, valor, extrato, quantidade_saques, LIMITE_QUANTIDADE_SAQUES):
    if quantidade_saques >= LIMITE_QUANTIDADE_SAQUES:
            print("ERRO: O número máximo de saques diários já foi realizado.\n")
    elif valor > saldo:
        print("ERRO: O valor do saque não pode ser maior que o saldo em conta.")
    elif valor > 0 and valor <= 500 and valor <= saldo and quantidade_saques < LIMITE_QUANTIDADE_SAQUES:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        quantidade_saques += 1
        print(f"Saque realizado!")
    elif valor > 500:
        print(f"ERRO: O valor solicitado excede o limite desta transação.")
    else:
        print(f"ERRO: Valor inválido! Por favor, tente novamente.")
    return saldo, extrato, quantidade_saques

def visualizar_extrato(saldo, extrato):
    print(f"VISUALIZAR HISTÓRICO\n")
    print(extrato)
    print(f"SALDO: R$ {saldo:.2f}")

def cadastrar_usuario(usuarios):
    cpf = input(f"Insira o CPF do usuário (apenas números): ")
    usuario = pesquisar_usuario(usuarios, cpf)
    
    if pesquisar_usuario(usuarios, cpf):
        print(f"ERRO: O CPF já está cadastrado no sistema.\n")
        return
    
    nome = input(f"Insira o nome do usuário: ")
    data_de_nascimento = input(f"Insira a data de nascimento do usuário (dia/mês/ano): ")
    endereco = input(f"Insira o endereço do usuário (logradouro, número - bairro - cidade/estado): ")

    usuario = {"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)

    print(f"Usuário cadastrado com sucesso!")

def pesquisar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
    
def cadastrar_conta(usuarios, contas):
    cpf = input(f"Insira o CPF do usuário (apenas números): ")
    usuario = pesquisar_usuario(usuarios, cpf)

    if not usuario:
        print(f"ERRO: Nenhum usuário identificado com o CPF informado! Por favor, cadastre o usuário ou tente novamente.")
        return
    
    numero_agencia = input(f"Insira o número da agência: ")
    numero_conta = "0001"
    numero_conta = f"{len(contas) + 1:04}"
    
    conta = {"numero_agencia": numero_agencia, "numero_conta": numero_conta, "usuario": cpf}
    contas.append(conta)

    print(f"Conta cadastrada com sucesso!")

def pesquisar_conta(contas, numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None

def listar_usuarios(usuarios):
    print(f"LISTA DE USUÁRIOS\n")
    for usuario in usuarios:
        print(f"NOME: {usuario['nome']} | CPF: {usuario['cpf']} | DATA DE NASCIMENTO: {usuario['data_de_nascimento']} | ENDEREÇO: {usuario['endereco']}")
    print("\n")

def listar_contas(contas):
    print(f"LISTA DE CONTAS\n")
    for conta in contas:
        print(f"NÚMERO DA AGÊNCIA: {conta['numero_agencia']} | NÚMERO DA CONTA: {conta['numero_conta']} | USUÁRIO: {conta['usuario']}")

def remover_usuario(usuarios, contas):
    cpf = input(f"Insira o CPF do usuário que será removido (apenas números): ")
    usuario = pesquisar_usuario(usuarios, cpf)
    
    if not usuario:
        print(f"ERRO: Nenhum usuário identificado pelo CPF informado! Por favor, tente novamente.\n")
        return
    else:
        contas[:] = [conta for conta in contas if conta['usuario'] != cpf]
        usuarios.remove(usuario)
    
    print(f"Usuário e respectiva(s) conta(s) removido(s) com sucesso!")

def remover_conta(contas):
    numero_conta = input(f"Insira o número da conta que será removida: ")

    conta = pesquisar_conta(contas, numero_conta)
    
    if conta:
        contas.remove(conta)
        print(f"Conta {numero_conta} encerrada com sucesso!\n")
    else:
        print(f"ERRO: Nenhuma conta identificada pelo número informado! Por favor, tente novamente.\n")

sistema()