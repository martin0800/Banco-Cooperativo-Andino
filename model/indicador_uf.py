class IndicadorUF:

    def __init__(self, valor, fecha):
        self.valor = valor
        self.fecha = fecha

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El valor de la UF debe ser mayor que cero.")
        self.__valor = float(valor)

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La fecha de la UF no puede estar vacía.")
        self.__fecha = valor.strip()

    def __str__(self):
        return f"UF: ${self.valor:,.2f} | Fecha: {self.fecha}"