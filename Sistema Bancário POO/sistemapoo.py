from abc import ABC, abstractproperty, abstractclassmethod
from datetime import datetime

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
            Deposito(Transacao)
        elif opcao == "2":
            Saque(Transacao)
        elif opcao == "3":
            Historico()
        elif opcao == "4":
            Cliente()
        elif opcao == "5":
            Conta()
        elif opcao == "0":
            break
        else:
            print(f"ERRO: Opção inválida! Por favor, escolha uma das opções disponibilizadas.")

class Cliente:
    def __init__ (self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__ (self, saldo, numero_conta, numero_agencia, cliente, historico):
        self.saldo = 0
        self.numero_conta = numero_conta
        self.numero_agencia = numero_agencia
        self.cliente = Cliente
        self.historico = historico
        

    @property
    def saldo(self):
        return self.saldo
    
    def nova_conta(cliente, numero_conta):
        return numero_conta
    
    def sacar(self, valor):
        saldo = self.saldo
        if valor > self.saldo:
            print("ERRO: O valor solicitado excede o saldo em conta. Por favor, tente novamente.")
            return False
        elif valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
            numero_saques += 1
        elif valor <= 0:
            print("ERRO: Valor inválido! Por favor, tente novamente.")
            return False
        elif valor > 500:
            print("ERRO: O valor excede o limite de saque único. Por favor, tente novamente.")
            return False
        return True
    
    def depositar(valor):
        return bool

class PessoaFisica(Cliente):
    def __init__ (self, cpf, nome, data_de_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        super().__init__(endereco)

class ContaCorrente(Conta):
    def __init__ (self, numero_conta, numero_agencia, cliente, limite):
        super().__init__(numero_conta, cliente)
        self.numero_conta = numero_conta
        self.numero_agencia = numero_agencia
        self.cliente = cliente
        self.limite = 500

    def sacar(self, valor):
        LIMITE_QUANTIDADE_SAQUES = 3
        numero_saques = len()
        saldo = self.saldo

        if numero_saques >= LIMITE_QUANTIDADE_SAQUES:
            print("ERRO: O limite diário de saques já foi atingido.")
            return False
        elif valor > 500:
            print("ERRO: O valor excede o limite de saque único. Por favor, tente novamente.")
            return False
        else:
            super().sacar(valor)

class Historico:
    def __init__ (self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(f"Tipo: {transacao.__class__.__name__} | Valor: {transacao.valor} | Data: {datetime.now().strftime("%d-%m-%Y - %H:%M-%s")}")

class Transacao(ABC):
    @property
    @abstractproperty
    def __init__ (self, valor):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__ (self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        deposito = conta.depositar(self.valor)

        if deposito:
            conta.historico.append(self)
            print("Depósito realizado com sucesso!")
        else:
            print("ERRO: A transação não pôde ser finalizada.")

class Saque(Transacao):
    def __init__ (self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        saque = conta.sacar(self.valor)

        if saque:
            conta.historico.append(self)
            print("Saque realizado com sucesso!")
        else:
            print("ERRO: A transação não pôde ser finalizada.")

sistema()