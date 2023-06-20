class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
            
            
    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")