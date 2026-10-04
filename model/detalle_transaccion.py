class DetalleTransaccion:

    def __init__(self, concepto, monto):
        self.concepto = concepto
        self.monto = monto

    @property
    def concepto(self):
        return self.__concepto

    @concepto.setter
    def concepto(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El concepto no puede estar vacío.")
        self.__concepto = valor.strip()

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.__monto = float(valor)

    def __str__(self):
        return f"{self.concepto} | ${self.monto:,.0f}"