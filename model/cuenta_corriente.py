from .cuenta import Cuenta


class CuentaCorriente(Cuenta):

    def __init__(self, numero, cliente, saldo=0, limite_sobregiro=100000):
        super().__init__(numero, cliente, saldo)
        self.limite_sobregiro = limite_sobregiro

    def girar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto del giro debe ser mayor que cero.")

        if monto > self.saldo + self.limite_sobregiro:
            raise ValueError(
                "El giro supera el saldo disponible y el límite de sobregiro."
            )

        self._Cuenta__saldo -= monto

    def calcular_interes(self):
        # La cuenta corriente no genera interés.
        return 0

    def __str__(self):
        return (
            f"Cuenta Corriente | Número: {self.numero} | "
            f"Saldo: ${self.saldo:,.0f} | "
            f"Limite sobregiro: ${self.limite_sobregiro:,.0f}"
        )