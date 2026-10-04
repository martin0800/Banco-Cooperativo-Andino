from enum import Enum


class EstadoCredito(Enum):
    PENDIENTE = "PENDIENTE"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"


class TipoMovimiento(Enum):
    DEPOSITO = "DEPOSITO"
    GIRO = "GIRO"
    CARGO = "CARGO"