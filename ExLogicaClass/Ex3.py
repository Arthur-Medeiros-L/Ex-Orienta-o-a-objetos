class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("nao")

    def exibir_saldo(self):
         print(f"Saldo: {self.__saldo}")

conta = Conta_Bancaria('Joao', 50)
conta.depositar(20)
conta.sacar(80) 
conta.exibir_saldo()



