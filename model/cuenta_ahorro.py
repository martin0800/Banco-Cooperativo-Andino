from .cuenta import Cuenta


class CuentaAhorro(Cuenta):

    def __init__(self, numero, cliente, saldo=0, tasa_interes=0.01):
        super().__init__(numero, cliente, saldo)
        self.tasa_interes = tasa_interes

    def girar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto del giro debe ser mayor que cero.")

        if monto > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el giro.")

        self._Cuenta__saldo -= monto

    def calcular_interes(self):
        interes = self.saldo * self.tasa_interes
        return interes

    def __str__(self):
        return (
            f"Cuenta Ahorro | Número: {self.numero} | "
            f"Saldo: ${self.saldo:,.0f} | "
            f"Tasa: {self.tasa_interes * 100:.2f}%"
        )