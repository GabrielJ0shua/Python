class Conta:
    __numConta = None
    __nome = None
    __saldo = None
    __idade = None
    __endereco = None

    def __init__(self, conta: int, nome: str, idade: int, endereco: dict) -> None:
        self.numConta = conta
        self.nome = nome
        self.saldo = 0
        self.idade = idade
        self.endereco = endereco

    @property
    def getNumConta(self):
        return self.__numConta

    @property
    def getNome(self):
        return self.__nome

    @property
    def getSaldo(self):
        return self.__saldo

    @property
    def getIdade(self):
        return self.__idade

    @property
    def getEndereco(self):
        return self.__endereco

    @numConta.setter
    def setNumConta(self, value):
        if isinstance(value, int):
            self.__numConta = value

    @nome.setter
    def setNome(self, value):
        if isinstance(value, str):
            self.nome = value

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
        if(value >= self.getSaldo):
            self.setSaldo = self.getSaldo - value

    @property
    def depositar(self, value: float):
        if(value > 0):
            self.setSaldo = self.getSaldo + value

class Banco:

    __
    