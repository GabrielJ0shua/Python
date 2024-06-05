
class Conta:
    __account = None
    __nome = None
    __saldo = None
    __idade = None
    __endereco = None

    def __init__(self, conta: int, nome: str, idade: int, endereco: dict) -> None:
        self.setAccount = conta
        self.setNome = nome
        self.setSaldo = 0
        self.setIdade = idade
        self.setEndereco = endereco

    @property
    def account(self):
        return self.__account

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def idade(self):
        return self.__idade

    @property
    def endereco(self):
        return self.__endereco

    @account.setter
    def setAccount(self, value: int) -> None:
        if isinstance(value, int):
            self.__account = value

    @nome.setter
    def setNome(self, value):
        if isinstance(value, str):
            self.__nome = value

    @saldo.setter
    def setSaldo(self, value):
        if isinstance(value, float):
            self.__saldo = value

    @idade.setter
    def setIdade(self, value):
        if (isinstance(value, int) and value > 17):
            self.__idade = value

    @endereco.setter
    def setEndereco(self, value):
        if isinstance(value, dict):
            self.__endereco = value

    @property
    def sacar(self, value: float):
        if(value >= self.saldo):
            self.setSaldo = self.saldo - value

    @property
    def depositar(self, value: float):
        if(value > 0):
            self.setSaldo = self.saldo + value

class Banco:

    __contas = None
    __numberAccount = None

    def __init__(self) -> None:
        self.setContas = []
        self.setPoint = 0

    @property
    def contas(self):
        return self.__contas
    
    @property
    def numberAccount(self):
        return self.__numberAccount
    
    @contas.setter
    def setContas(self, value: list):
        if isinstance(value, list):
            self.__contas = value

    @numberAccount.setter
    def setPoint(self, value: int):
        if isinstance(value, int):
            self.__numberAccount = value

    
    def addConta(self, conta: Conta):
        if isinstance(conta, Conta) and self.contas != None:
            self.__contas.append(conta)
            self.__numberAccount += 1
            return (f"Criado com sucesso. Conta de número: {(self.numberAccount-1)}")
        
    @property
    def remConta(self, value: int):
        if(len(self.numberAccount) < value):
            return ("Não é possivel!")
        else:
            self.__contas.pop(value)
            return ("Sucesso!")