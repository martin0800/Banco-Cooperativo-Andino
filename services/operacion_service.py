from model.transaccion import Transaccion
from model.detalle_transaccion import DetalleTransaccion
from model.movimiento import Movimiento
from model.enums import TipoMovimiento

from exceptions.saldo_insuficiente_error import SaldoInsuficienteError


class OperacionService:

    def __init__(
        self,
        cuenta_dao,
        transaccion_dao,
        movimiento_dao
    ):
        self.cuenta_dao = cuenta_dao
        self.transaccion_dao = transaccion_dao
        self.movimiento_dao = movimiento_dao

    def depositar(self, numero_cuenta, monto, concepto="Depósito"):
        cuenta = self.cuenta_dao.buscar_por_numero(numero_cuenta)

        if cuenta is None:
            raise ValueError("La cuenta no existe.")

        cuenta.depositar(monto)

        self.cuenta_dao.actualizar_saldo(
            cuenta.numero,
            cuenta.saldo
        )

        transaccion = Transaccion(
            None,
            cuenta,
            "DEPOSITO"
        )

        transaccion.agregar_detalle(
            DetalleTransaccion(concepto, monto)
        )

        id_transaccion = self.transaccion_dao.crear(
            transaccion
        )

        movimiento = Movimiento(
            cuenta,
            TipoMovimiento.DEPOSITO,
            monto,
            concepto
        )

        self.movimiento_dao.crear(movimiento)

        return cuenta, id_transaccion

    def girar(self, numero_cuenta, monto, concepto="Giro"):
        cuenta = self.cuenta_dao.buscar_por_numero(numero_cuenta)

        if cuenta is None:
            raise ValueError("La cuenta no existe.")

        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError(
                "El monto del giro debe ser mayor que cero."
            )

        if hasattr(cuenta, "limite_sobregiro"):
            disponible = (
                cuenta.saldo +
                cuenta.limite_sobregiro
            )
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

        transaccion = Transaccion(
            None,
            cuenta,
            "GIRO"
        )

        transaccion.agregar_detalle(
            DetalleTransaccion(concepto, monto)
        )

        id_transaccion = self.transaccion_dao.crear(
            transaccion
        )

        movimiento = Movimiento(
            cuenta,
            TipoMovimiento.GIRO,
            monto,
            concepto
        )

        self.movimiento_dao.crear(movimiento)

        return cuenta, id_transaccion