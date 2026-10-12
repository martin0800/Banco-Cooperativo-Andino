from datetime import datetime


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
            raise ValueError("El valor del indicador debe ser mayor que cero.")
        self.__valor = float(valor)

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La fecha del indicador no puede estar vacía.")

        fecha_limpia = valor.strip()

        try:
            fecha_objeto = datetime.fromisoformat(
                fecha_limpia.replace("Z", "+00:00")
            )
            self.__fecha = fecha_objeto.strftime("%d-%m-%Y")
        except ValueError:
            try:
                fecha_objeto = datetime.strptime(
                    fecha_limpia, "%Y-%m-%d"
                )
                self.__fecha = fecha_objeto.strftime("%d-%m-%Y")
            except ValueError:
                raise ValueError("El formato de la fecha del indicador no es válido.")

    def __str__(self):
        return f"Valor: ${self.valor:,.2f} | Fecha: {self.fecha}"