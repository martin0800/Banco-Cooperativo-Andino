from dao.database import obtener_conexion


class TransaccionDAO:

    def crear(self, transaccion):
        conexion = obtener_conexion()

        try:
            total = transaccion.calcular_total()

            cursor = conexion.execute(
                """
                INSERT INTO transacciones (
                    numero_cuenta,
                    tipo,
                    total,
                    fecha
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    transaccion.cuenta.numero,
                    transaccion.tipo,
                    total,
                    transaccion.fecha.isoformat()
                )
            )

            id_transaccion = cursor.lastrowid

            for detalle in transaccion.detalles:
                conexion.execute(
                    """
                    INSERT INTO detalles_transaccion (
                        transaccion_id,
                        concepto,
                        monto
                    )
                    VALUES (?, ?, ?)
                    """,
                    (
                        id_transaccion,
                        detalle.concepto,
                        detalle.monto
                    )
                )

            conexion.commit()

            return id_transaccion

        except Exception:
            conexion.rollback()
            raise

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
                    total,
                    fecha
                FROM transacciones
                WHERE numero_cuenta = ?
                ORDER BY fecha DESC
                """,
                (numero_cuenta,)
            )

            return cursor.fetchall()

        finally:
            conexion.close()

    def obtener_detalles(self, id_transaccion):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                SELECT
                    id,
                    concepto,
                    monto
                FROM detalles_transaccion
                WHERE transaccion_id = ?
                ORDER BY id
                """,
                (id_transaccion,)
            )

            return cursor.fetchall()

        finally:
            conexion.close()