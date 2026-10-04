from model.cuenta_ahorro import CuentaAhorro
from model.cuenta_corriente import CuentaCorriente
from model.cuenta_vista import CuentaVista

from exceptions.cliente_en_mora_error import ClienteEnMoraError
from exceptions.saldo_insuficiente_error import SaldoInsuficienteError


class BancoService:

    def __init__(self, cliente_dao, cuenta_dao):
        self.cliente_dao = cliente_dao
        self.cuenta_dao = cuenta_dao

    def abrir_cuenta(
        self,
        cliente,
        tipo,
        numero,
        saldo_inicial=0
    ):
        # REGLA DE NEGOCIO 1:
        # Un cliente con mora no puede abrir una cuenta.
        if cliente.tiene_mora:
            raise ClienteEnMoraError(
                "No se puede abrir una cuenta: "
                "el cliente tiene una mora activa."
            )

        tipo = tipo.strip().upper()

        if tipo == "AHORRO":
            cuenta = CuentaAhorro(
                numero,
                cliente,
                saldo_inicial
            )

        elif tipo == "CORRIENTE":
            cuenta = CuentaCorriente(
                numero,
                cliente,
                saldo_inicial
            )

        elif tipo == "VISTA":
            cuenta = CuentaVista(
                numero,
                cliente,
                saldo_inicial
            )

        else:
            raise ValueError(
                "Tipo de cuenta inválido. "
                "Use AHORRO, CORRIENTE o VISTA."
            )

        self.cuenta_dao.crear(cuenta)

        return cuenta

    def realizar_giro(self, numero_cuenta, monto):
        cuenta = self.cuenta_dao.buscar_por_numero(numero_cuenta)

        if cuenta is None:
            raise ValueError("La cuenta no existe.")

        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError(
                "El monto del giro debe ser mayor que cero."
            )

        # REGLA DE NEGOCIO 2:
        # Verificamos cuánto puede retirar la cuenta.
        if isinstance(cuenta, CuentaCorriente):
            disponible = cuenta.saldo + cuenta.limite_sobregiro
        else:
            disponible = cuenta.saldo

        if monto > disponible:
            raise SaldoInsuficienteError(
                "Operación bloqueada: "
                "el monto supera el saldo disponible."
            )

        cuenta.girar(monto)

        self.cuenta_dao.actualizar_saldo(
            cuenta.numero,
            cuenta.saldo
        )

        return cuenta

    def realizar_deposito(self, numero_cuenta, monto):
        cuenta = self.cuenta_dao.buscar_por_numero(numero_cuenta)

        if cuenta is None:
            raise ValueError("La cuenta no existe.")

        cuenta.depositar(monto)

        self.cuenta_dao.actualizar_saldo(
            cuenta.numero,
            cuenta.saldo
        )

        return cuenta