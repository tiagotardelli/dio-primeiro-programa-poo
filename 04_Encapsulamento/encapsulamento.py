class Conta:
    def __init__(self, numero_agencia, saldo = 0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        #----
        self._saldo += valor

    def sacar(self, valor):
        #----
        self._saldo -= valor

    def mostrar_saldo(self):
        #-
        return self._saldo

if __name__ == "__main__":
    conta = Conta(100)
    print(conta)
    # fora de convenção, errado:
    conta._saldo += 100
    print(conta._saldo)
    # fim
    conta.depositar(100)

    conta = Conta("0001", 100)
    conta.depositar(100)
    print(conta._saldo)
    print(conta.numero_agencia)
    print(conta.numero_agencia)
    print(conta.mostrar_saldo())