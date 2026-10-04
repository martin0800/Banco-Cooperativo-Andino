from .cuenta import Cuenta


class CuentaVista(Cuenta):

    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)

    def girar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto del giro debe ser mayor que cero.")

        if monto > self.saldo:
            raise ValueError(
                "La cuenta vista no permite sobregiro. Saldo insuficiente."
            )

        self._Cuenta__saldo -= monto

    def calcular_interes(self):
        # La cuenta vista no genera intereses.
        return 0

    def __str__(self):
        return (
            f"Cuenta Vista | Número: {self.numero} | "
            f"Saldo: ${self.saldo:,.0f}"
        )