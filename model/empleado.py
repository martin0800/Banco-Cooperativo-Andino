from abc import ABC, abstractmethod


class Empleado(ABC):

    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El RUT del empleado no puede estar vacío.")
        self.__rut = valor.strip()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del empleado no puede estar vacío.")
        self.__nombre = valor.strip()

    @abstractmethod
    def obtener_permisos(self):
        pass

    def __str__(self):
        return f"Empleado: {self.nombre} | RUT: {self.rut}"