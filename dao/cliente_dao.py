from dao.database import obtener_conexion
from model.cliente import Cliente


class ClienteDAO:

    def crear(self, cliente):
        conexion = obtener_conexion()

        try:
            conexion.execute(
                """
                INSERT INTO clientes (rut, nombre, tiene_mora)
                VALUES (?, ?, ?)
                """,
                (
                    cliente.rut,
                    cliente.nombre,
                    int(cliente.tiene_mora)
                )
            )

            conexion.commit()

        finally:
            conexion.close()

    def listar(self):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                SELECT rut, nombre, tiene_mora
                FROM clientes
                ORDER BY nombre
                """
            )

            filas = cursor.fetchall()

            clientes = []

            for fila in filas:
                clientes.append(
                    Cliente(
                        rut=fila[0],
                        nombre=fila[1],
                        tiene_mora=bool(fila[2])
                    )
                )

            return clientes

        finally:
            conexion.close()

    def buscar_por_rut(self, rut):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                SELECT rut, nombre, tiene_mora
                FROM clientes
                WHERE rut = ?
                """,
                (rut,)
            )

            fila = cursor.fetchone()

            if fila is None:
                return None

            return Cliente(
                rut=fila[0],
                nombre=fila[1],
                tiene_mora=bool(fila[2])
            )

        finally:
            conexion.close()

    def actualizar(self, cliente):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                UPDATE clientes
                SET nombre = ?, tiene_mora = ?
                WHERE rut = ?
                """,
                (
                    cliente.nombre,
                    int(cliente.tiene_mora),
                    cliente.rut
                )
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()

    def eliminar(self, rut):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                DELETE FROM clientes
                WHERE rut = ?
                """,
                (rut,)
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()