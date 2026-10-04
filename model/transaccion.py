from datetime import datetime


class Transaccion:

    def __init__(self, id_transaccion, cuenta, tipo, detalles=None):
        self.id_transaccion = id_transaccion
        self.cuenta = cuenta
        self.tipo = tipo
        self.fecha = datetime.now()
        self.detalles = detalles if detalles else []

    @property
    def id_transaccion(self):
        return self.__id_transaccion


    @id_transaccion.setter
    def id_transaccion(self, valor):
        if valor is not None and (
           not isinstance(valor, int) or valor <= 0
    ):
           raise ValueError(
            "El ID de la transacción debe ser positivo."
        )

        self.__id_transaccion = valor

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, valor):
        if valor is None:
            raise ValueError(
                "La transacción debe estar asociada a una cuenta."
            )
        self.__cuenta = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El tipo de transacción no puede estar vacío.")
        self.__tipo = valor.strip().upper()

    def agregar_detalle(self, detalle):
        if detalle is None:
            raise ValueError("El detalle no puede ser vacío.")

        self.detalles.append(detalle)

    def calcular_total(self):
        return sum(detalle.monto for detalle in self.detalles)

    def __str__(self):
        return (
            f"Transacción #{self.id_transaccion} | "
            f"Cuenta: {self.cuenta.numero} | "
            f"Tipo: {self.tipo} | "
            f"Total: ${self.calcular_total():,.0f}"
        )