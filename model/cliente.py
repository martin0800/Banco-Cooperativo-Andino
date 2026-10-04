class Cliente:
    def __init__(self, rut, nombre, tiene_mora=False):
        self.rut = rut
        self.nombre = nombre
        self.tiene_mora = tiene_mora

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, valor):
        if not self.validar_rut(valor):
            raise ValueError("RUT inválido.")
        self.__rut = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def tiene_mora(self):
        return self.__tiene_mora

    @tiene_mora.setter
    def tiene_mora(self, valor):
        self.__tiene_mora = bool(valor)

    @staticmethod
    def validar_rut(rut):
        """
        Valida el formato y dígito verificador de un RUT chileno.
        Ejemplo válido: 12.345.678-5
        """

        if not isinstance(rut, str):
            return False

        rut = rut.replace(".", "").replace("-", "").upper().strip()

        if len(rut) < 2:
            return False

        cuerpo = rut[:-1]
        digito = rut[-1]

        if not cuerpo.isdigit():
            return False

        if not (digito.isdigit() or digito == "K"):
            return False

        suma = 0
        multiplicador = 2

        for numero in reversed(cuerpo):
            suma += int(numero) * multiplicador
            multiplicador += 1

            if multiplicador > 7:
                multiplicador = 2

        resto = 11 - (suma % 11)

        if resto == 11:
            esperado = "0"
        elif resto == 10:
            esperado = "K"
        else:
            esperado = str(resto)

        return digito == esperado

    def __str__(self):
        estado = "Con mora" if self.tiene_mora else "Sin mora"
        return f"Cliente: {self.nombre} | RUT: {self.rut} | {estado}"