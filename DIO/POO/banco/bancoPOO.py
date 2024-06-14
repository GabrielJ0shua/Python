from datetime import date
from abc import ABC, abstractproperty, abstractclassmethod

class Cliente:
    __endereco: str = None
    __contas: list = None

    def __init__(self, endereco: str) -> None:
        self.__contas = []
        self.endereco = endereco

    @property
    def endereco(self):
        return self.__endereco  

    @property
    def contas(self):
        return self.__contas
    
    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    @contas.setter
    def contas(self, valor):
        self.__contas.append(valor)

    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionarConta(self, valor):
        self.contas = valor

class PessoaFisica(Cliente):
    __cpf : str = ""
    __nome: str = ""
    __dataNascimento: date = None

    def __init__(self, cpf: str, nome: str, dataNascimento: date, endereco: str) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    @property
    def nome(self)-> str:
        return self.__nome
    @property
    def cpf(self)-> str:
        return self.__cpf
    @property
    def dataNascimento(self)-> date:
        return self.__dataNascimento
    
    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(str, nome):
            self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if isinstance(str, cpf):
            self.__cpf = cpf

    @dataNascimento.setter
    def nome(self, dataNascimento: date) -> None:
        if isinstance(date, dataNascimento):
            self.__dataNascimento = dataNascimento    

class Conta:
    __saldo:float = None
    __numero: int = None
    __agencia: str = None
    __cliente: Cliente = None
    __historico = None

    def __init__(self, numero: int, agencia: str, cliente: Cliente) -> None:
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = []


    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    @agencia.setter
    def agencia(self, valor):
        self.__agencia = valor

    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @historico.setter
    def historico(self, valor):
        self.__historico = valor

    def novaConta(self, cliente: Cliente, numero: int):
        self.cliente = cliente
        self.numero = numero

    def sacar(self, valor: float):
        if(isinstance(valor, float) and valor > 0 and valor <= self.saldo):
            self.saldo -= valor
            return 1
        else:
            return 0
        
    def depositar(self, valor: float):
        if(isinstance(valor, float) and valor > 0):
            self.saldo += valor
            return 1
        else:
            return 0

class ContaCorrente(Conta):
    __limite : float = 0
    __limiteSaques: int = 0

    def __init__(self, limite: float, limiteSaques: int,  numero: int, agencia: str, cliente: Cliente) -> None:
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limiteSaque = limiteSaques
        
    @property
    def limite(self):
        return self.__limite
    @property
    def limiteSaques(self):
        return self.__limiteSaques
    
    @limite.setter
    def limite(self, limite: float) -> None:
        if isinstance(float, limite):
            self.__limite = license

    @limiteSaques.setter
    def limiteSaque(self, limiteSaques) -> None:
        if isinstance(float, limiteSaques):
            self.__limiteSaques = limiteSaques

class Historico:
    __transacao = None

    def __init__(self) -> None:
        self.transacao = []

    @property
    def transacao(self):
        return self.__transacao
    
    @transacao.setter
    def transacao(self, valor):
        self.__transacao.append(valor)

class Transacao(ABC):  
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta:Conta):
        pass

class Deposito(Transacao):
    __valor: float = 0

    def __init__(self, valor: float) -> None:
        self.valor = valor

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float) -> None:
        if isinstance(float, valor):
            self.__valor = valor

class Saque(Transacao):
    __valor: float = 0

    def __init__(self, valor: float) -> None:
        self.valor = valor

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor) -> None:
        if isinstance(float, valor):
            self.__valor = valor

menu = """

[c] Criar conta
[v] Ver contas
[p] Pegar uma conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def molde(nro: int):
    return {
        "cliente": 
        {
            "nome": "",
            "data": "",
            "cpf": 0,
            "endereco": {
                "logradouro": "",
                "numero": 0,
                "bairro": "",
                "cidade": "",
                "siglaDoEstado": "",
            }
        },
        "info": 
        {
            "saldo" : 0,
            "limite" : 500,
            "extrato" : "",
            "numero_saques" : 0,
            "LIMITE_SAQUES" : 3
    },
        "ag": "0001",
        "nro": nro
    }

contaBancaria = []
aux = -1

def depositar(valor, info):
    if valor > 0:
        info['info']["saldo"] += valor
        info['info']["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        return info
    else:
        print("Operação falhou! O valor informado é inválido.")
        return info

def sacar(valor, info):
    if(valor > info['info']["saldo"]):
        print("Operação falhou! Você não tem saldo suficiente.")
    elif(valor > info['info']["limite"]):
        print("Operação falhou! O valor do saque excede o limite.")
    elif(info['info']["numero_saques"] >= info['info']["LIMITE_SAQUES"]):
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        info['info']["saldo"] -= valor
        info['info']["extrato"] += f"Saque: R$ {valor:.2f}\n"
        info['info']["numero_saques"] += 1
    
    return info

def extrato(info):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not info['info']["extrato"] else info['info']["extrato"])
    print(f"\nSaldo: R$ {info['info']['saldo']}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        if(aux > -1):
            valor = float(input("Informe o valor do depósito: "))
            contaBancaria[aux] = depositar(valor, contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "s":
        if(aux > -1):
            valor = float(input("Informe o valor do saque: "))
            contaBancaria[aux] = sacar(valor, contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "e":
        if(aux > -1):
            extrato(contaBancaria[aux])
        else:
            print("Não foi ninguém selecionado.")

    elif opcao == "c":
        try:
            cliente = molde(len(contaBancaria))

            cliente["cliente"]["nome"] = input("Qual é o nome? \n")
            cliente["cliente"]["data"] = input("Data de nascimento? \n")
            cliente["cliente"]["cpf"] = int(input("Qual o cpf (somente números)? \n"))
            cliente["cliente"]["endereco"]["logradouro"] = input("Qual é a rua?\n")
            cliente["cliente"]["endereco"]["numero"] = int(input("Qual é o número?\n"))
            cliente["cliente"]["endereco"]["bairro"] = input("Qual é o bairro?\n")
            cliente["cliente"]["endereco"]["cidade"] = input("Qual é a cidade?\n")
            cliente["cliente"]["endereco"]["siglaDoEstado"] = input("Qual é a sigla do estado?\n")

            contaBancaria.append(cliente)

            print("Adicionado com sucesso!!!\n")
        except:
            print("Erro!!!\n")

    elif opcao == "v":
        for i in contaBancaria:
            print(f"Nome: {i['cliente']['nome']}\n")
            print(f"CPF: {i['cliente']['cpf']}\n")
            print(f"Número de conta: {i['nro']}\n\n")
            
    elif opcao == "p":
        aux = int(input("\nQual o número da conta: "))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")