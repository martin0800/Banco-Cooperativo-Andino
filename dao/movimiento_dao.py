from dao.database import obtener_conexion


class MovimientoDAO:

    def crear(self, movimiento):
        conexion = obtener_conexion()

        try:
            conexion.execute(
                """
                INSERT INTO movimientos (
                    numero_cuenta,
                    tipo,
                    monto,
                    descripcion,
                    fecha
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    movimiento.cuenta.numero,
                    movimiento.tipo.value,
                    movimiento.monto,
                    movimiento.descripcion,
                    movimiento.fecha.isoformat()
                )
            )

            conexion.commit()

        finally:
            conexion.close()

    def listar_por_cuenta(self, numero_cuenta):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                SELECT
                    id,
                    tipo,
                    monto,
                    descripcion,
                    fecha
                FROM movimientos
                WHERE numero_cuenta = ?
                ORDER BY fecha DESC
                """,
                (numero_cuenta,)
            )

            return cursor.fetchall()

        finally:
            conexion.close()