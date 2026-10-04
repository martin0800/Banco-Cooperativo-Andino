from dao.database import obtener_conexion
from model.cuenta_ahorro import CuentaAhorro
from model.cuenta_corriente import CuentaCorriente
from model.cuenta_vista import CuentaVista


class CuentaDAO:

    def crear(self, cuenta):
        conexion = obtener_conexion()

        try:
            tipo = self._obtener_tipo(cuenta)

            tasa_interes = getattr(cuenta, "tasa_interes", 0)
            limite_sobregiro = getattr(cuenta, "limite_sobregiro", 0)

            conexion.execute(
                """
                INSERT INTO cuentas (
                    numero,
                    rut_cliente,
                    tipo,
                    saldo,
                    fecha_apertura,
                    tasa_interes,
                    limite_sobregiro
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cuenta.numero,
                    cuenta.cliente.rut,
                    tipo,
                    cuenta.saldo,
                    cuenta.fecha_apertura.isoformat(),
                    tasa_interes,
                    limite_sobregiro
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
                SELECT
                    numero,
                    rut_cliente,
                    tipo,
                    saldo,
                    fecha_apertura,
                    tasa_interes,
                    limite_sobregiro
                FROM cuentas
                ORDER BY numero
                """
            )

            filas = cursor.fetchall()

            cuentas = []

            for fila in filas:
                cuenta = self._crear_objeto(fila)

                if cuenta is not None:
                    cuentas.append(cuenta)

            return cuentas

        finally:
            conexion.close()

    def buscar_por_numero(self, numero):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                SELECT
                    numero,
                    rut_cliente,
                    tipo,
                    saldo,
                    fecha_apertura,
                    tasa_interes,
                    limite_sobregiro
                FROM cuentas
                WHERE numero = ?
                """,
                (numero,)
            )

            fila = cursor.fetchone()

            if fila is None:
                return None

            return self._crear_objeto(fila)

        finally:
            conexion.close()

    def actualizar_saldo(self, numero, nuevo_saldo):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                UPDATE cuentas
                SET saldo = ?
                WHERE numero = ?
                """,
                (nuevo_saldo, numero)
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()

    def eliminar(self, numero):
        conexion = obtener_conexion()

        try:
            cursor = conexion.execute(
                """
                DELETE FROM cuentas
                WHERE numero = ?
                """,
                (numero,)
            )

            conexion.commit()

            return cursor.rowcount > 0

        finally:
            conexion.close()

    @staticmethod
    def _obtener_tipo(cuenta):
        if isinstance(cuenta, CuentaAhorro):
            return "AHORRO"

        if isinstance(cuenta, CuentaCorriente):
            return "CORRIENTE"

        if isinstance(cuenta, CuentaVista):
            return "VISTA"

        raise ValueError("Tipo de cuenta no reconocido.")

    @staticmethod
    def _crear_objeto(fila):
        numero = fila[0]
        rut_cliente = fila[1]
        tipo = fila[2]
        saldo = fila[3]
        tasa_interes = fila[5]
        limite_sobregiro = fila[6]

        # Para reconstruir la cuenta necesitamos al cliente.
        from dao.cliente_dao import ClienteDAO

        cliente = ClienteDAO().buscar_por_rut(rut_cliente)

        if cliente is None:
            return None

        if tipo == "AHORRO":
            return CuentaAhorro(
                numero=numero,
                cliente=cliente,
                saldo=saldo,
                tasa_interes=tasa_interes
            )

        if tipo == "CORRIENTE":
            return CuentaCorriente(
                numero=numero,
                cliente=cliente,
                saldo=saldo,
                limite_sobregiro=limite_sobregiro
            )

        if tipo == "VISTA":
            return CuentaVista(
                numero=numero,
                cliente=cliente,
                saldo=saldo
            )

        return None