class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.empleados = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del banco no puede estar vacío.")

        self.__nombre = valor.strip()

    def agregar_cliente(self, cliente):
        if cliente is None:
            raise ValueError("El cliente no puede ser vacío.")

        self.clientes.append(cliente)

    def agregar_empleado(self, empleado):
        if empleado is None:
            raise ValueError("El empleado no puede ser vacío.")

        self.empleados.append(empleado)

    def buscar_cliente(self, rut):
        for cliente in self.clientes:
            if cliente.rut == rut:
                return cliente

        return None

    def mostrar_clientes(self):
        return self.clientes

    def mostrar_empleados(self):
        return self.empleados

    def __str__(self):
        return (
            f"Banco: {self.nombre} | "
            f"Clientes: {len(self.clientes)} | "
            f"Empleados: {len(self.empleados)}"
        )