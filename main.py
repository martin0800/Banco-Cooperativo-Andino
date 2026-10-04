from dao.transaccion_dao import TransaccionDAO
from dao.movimiento_dao import MovimientoDAO
from dao.database import crear_tablas
from dao.cliente_dao import ClienteDAO
from dao.cuenta_dao import CuentaDAO
from services.operacion_service import OperacionService
from services.uf_service import UFService
from services.dolar_service import DolarService
from model.cliente import Cliente
from model.cuenta_ahorro import CuentaAhorro
from model.cuenta_corriente import CuentaCorriente
from model.cuenta_vista import CuentaVista

from exceptions.cliente_en_mora_error import ClienteEnMoraError
from exceptions.saldo_insuficiente_error import SaldoInsuficienteError

cliente_dao = ClienteDAO()
cuenta_dao = CuentaDAO()


# ==========================================================
# MENÃš PRINCIPAL
# ==========================================================

def mostrar_menu():
    print("\n" + "=" * 50)
    print("       BANCO COOPERATIVO ANDINO")
    print("=" * 50)
    print("1. Gestión de clientes")
    print("2. Gestión de cuentas")
    print("3. Operaciones bancarias")
    print("4. Cartola")
    print("5. Consultar indicador UF")
    print("6. Consultar valor del dólar")
    print("0. Salir")
    print("=" * 50)


# ==========================================================
# GESTIÓN DE CLIENTES
# ==========================================================

def menu_clientes():

    while True:

        print("\n" + "=" * 40)
        print("        GESTIÓN DE CLIENTES")
        print("=" * 40)
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver")
        print("=" * 40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cliente()

        elif opcion == "2":
            listar_clientes()

        elif opcion == "3":
            modificar_cliente()

        elif opcion == "4":
            eliminar_cliente()

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


def crear_cliente():
    print("\n--- CREAR CLIENTE ---")

    try:
        rut = input("Ingrese RUT: ").strip()
        nombre = input("Ingrese nombre: ").strip()

        mora = input("¿El cliente tiene mora? (s/n): ").strip().lower()

        if mora not in ("s", "n"):
            print("Respuesta inválida. Debe ingresar s o n.")
            return

        tiene_mora = mora == "s"

        cliente = Cliente(rut, nombre, tiene_mora)
        cliente_dao.crear(cliente)

        print("\nCliente creado correctamente.")
        print(f"RUT: {cliente.rut}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Mora: {'Sí' if cliente.tiene_mora else 'No'}")

    except ValueError as e:
        print(f"\nError de validación: {e}")

    except Exception as e:
        print(f"\nNo se pudo crear el cliente: {e}")


def listar_clientes():

    print("\n--- LISTADO DE CLIENTES ---")

    try:

        clientes = cliente_dao.listar()

        if not clientes:
            print("No existen clientes registrados.")
            return

        for cliente in clientes:
            print(cliente)

    except Exception as e:
        print(f"\nError al listar clientes: {e}")


def modificar_cliente():

    print("\n--- MODIFICAR CLIENTE ---")

    try:

        rut = input("Ingrese RUT del cliente: ").strip()
        nombre = input("Ingrese nuevo nombre: ").strip()

        cliente = Cliente(rut, nombre)

        cliente_dao.actualizar(cliente)

        print("\nCliente actualizado correctamente.")

    except ValueError as e:
        print(f"\nError de validación: {e}")

    except Exception as e:
        print(f"\nNo se pudo modificar el cliente: {e}")


def eliminar_cliente():

    print("\n--- ELIMINAR CLIENTE ---")

    try:

        rut = input("Ingrese RUT del cliente: ").strip()

        eliminado = cliente_dao.eliminar(rut)

        if eliminado:
            print("\nCliente eliminado correctamente.")
        else:
            print("\nNo existe un cliente con ese RUT.")

    except Exception as e:
        print(f"\nNo se pudo eliminar el cliente: {e}")


# ==========================================================
# GESTIÓN DE CUENTAS
# ==========================================================

def menu_cuentas():

    while True:

        print("\n" + "=" * 40)
        print("         GESTIÓN DE CUENTAS")
        print("=" * 40)
        print("1. Crear cuenta")
        print("2. Listar cuentas")
        print("3. Buscar cuenta")
        print("4. Eliminar cuenta")
        print("0. Volver")
        print("=" * 40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cuenta()

        elif opcion == "2":
            listar_cuentas()

        elif opcion == "3":
            buscar_cuenta()

        elif opcion == "4":
            eliminar_cuenta()

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


def crear_cuenta():

    print("\n--- CREAR CUENTA ---")

    try:

        rut = input("Ingrese RUT del cliente: ").strip()

        cliente = cliente_dao.buscar_por_rut(rut)

        if cliente is None:
            print("\nNo existe un cliente con ese RUT.")
            return

        # Regla de negocio 1
        if cliente.tiene_mora:
            raise ClienteEnMoraError(
                "El cliente tiene mora activa y no puede abrir una cuenta."
            )

        print("\nTipos de cuenta:")
        print("1. Cuenta Ahorro")
        print("2. Cuenta Corriente")
        print("3. Cuenta Vista")

        tipo = input("Seleccione tipo de cuenta: ").strip()

        numero = input("Ingrese número de cuenta: ").strip()

        saldo_texto = input("Ingrese saldo inicial: ").strip()

        saldo = float(saldo_texto)

        if saldo < 0:
            print("\nEl saldo inicial no puede ser negativo.")
            return

        if tipo == "1":

            tasa_ahorro = UFService.calcular_tasa_ahorro()

            cuenta = CuentaAhorro(
                numero=numero,
                cliente=cliente,
                saldo=saldo,
                tasa_interes=tasa_ahorro
            )

            print(
                f"Tasa de interés calculada con UF: "
                f"{tasa_ahorro * 100:.2f}%"
            )

        elif tipo == "2":

            cuenta = CuentaCorriente(
                numero=numero,
                cliente=cliente,
                saldo=saldo
            )

        elif tipo == "3":

            cuenta = CuentaVista(
                numero=numero,
                cliente=cliente,
                saldo=saldo
            )

        else:

            print("\nTipo de cuenta inválido.")
            return

        cuenta_dao.crear(cuenta)

        print("\nCuenta creada correctamente.")
        print(cuenta)

    except ClienteEnMoraError as e:

        print(f"\nOperación bloqueada: {e}")

    except ValueError as e:

        print(f"\nError de validación: {e}")

    except Exception as e:

        print(f"\nNo se pudo crear la cuenta: {e}")

def listar_cuentas():

    print("\n--- LISTADO DE CUENTAS ---")

    try:

        cuentas = cuenta_dao.listar()

        if not cuentas:
            print("No existen cuentas registradas.")
            return

        for cuenta in cuentas:
            print(cuenta)

    except Exception as e:

        print(f"\nError al listar cuentas: {e}")


def buscar_cuenta():

    print("\n--- BUSCAR CUENTA ---")

    try:

        numero = input("Ingrese número de cuenta: ").strip()

        cuenta = cuenta_dao.buscar_por_numero(numero)

        if cuenta is None:
            print("\nCuenta no encontrada.")
            return

        print("\nCuenta encontrada:")
        print(cuenta)

    except Exception as e:

        print(f"\nError al buscar cuenta: {e}")


def eliminar_cuenta():

    print("\n--- ELIMINAR CUENTA ---")

    try:

        numero = input("Ingrese número de cuenta: ").strip()

        eliminado = cuenta_dao.eliminar(numero)

        if eliminado:
            print("\nCuenta eliminada correctamente.")
        else:
            print("\nNo existe una cuenta con ese número.")

    except Exception as e:

        print(f"\nNo se pudo eliminar la cuenta: {e}")


# ==========================================================
# OPERACIONES BANCARIAS
# ==========================================================

def menu_operaciones():
    cuenta_dao = CuentaDAO()
    transaccion_dao = TransaccionDAO()
    movimiento_dao = MovimientoDAO()

    operacion_service = OperacionService(
        cuenta_dao,
        transaccion_dao,
        movimiento_dao
    )

    while True:
        print('\n==========================================')
        print('       OPERACIONES BANCARIAS')
        print('==========================================')
        print('1. Realizar depósito')
        print('2. Realizar giro')
        print('3. Consultar cuenta')
        print('0. Volver')
        print('==========================================')

        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            print('\n--- REALIZAR DEPÓSITO ---')
            numero_cuenta = input('Ingrese número de cuenta: ').strip()
            try:
                monto = float(input('Ingrese monto del depósito: ').strip())
                if monto <= 0:
                    print('El monto debe ser mayor que cero.')
                    continue
                concepto = input('Ingrese concepto: ').strip() or 'Depósito'
                cuenta, id_transaccion = operacion_service.depositar(numero_cuenta, monto, concepto)
                print('\\nDepósito realizado correctamente.')
                print(f'Cuenta: {cuenta.numero}')
                print(f'Nuevo saldo: ${cuenta.saldo:,.0f}')
                print(f'Transacción registrada: #{id_transaccion}')
            except ValueError as error:
                print(f'Error: {error}')
            except Exception as error:
                print(f'No se pudo realizar el depósito: {error}')

        elif opcion == '2':
            print('\n--- REALIZAR GIRO ---')
            numero_cuenta = input('Ingrese número de cuenta: ').strip()
            try:
                monto = float(input('Ingrese monto del giro: ').strip())
                if monto <= 0:
                    print('El monto debe ser mayor que cero.')
                    continue
                concepto = input('Ingrese concepto: ').strip() or 'Giro'
                cuenta, id_transaccion = operacion_service.girar(numero_cuenta, monto, concepto)
                print('\nGiro realizado correctamente.')
                print(f'Cuenta: {cuenta.numero}')
                print(f'Nuevo saldo: ')
                print(f'Transacción registrada: #{id_transaccion}')
            except SaldoInsuficienteError as error:
                print(f'\nOPERACIÓN BLOQUEADA: {error}')
            except ValueError as error:
                print(f'Error: {error}')
            except Exception as error:
                print(f'No se pudo realizar el giro: {error}')

        elif opcion == '3':
            numero_cuenta = input('Ingrese número de cuenta: ').strip()
            try:
                cuenta = cuenta_dao.buscar_por_numero(numero_cuenta)
                if cuenta is None:
                    print('La cuenta no existe.')
                else:
                    print('\nCuenta encontrada:')
                    print(cuenta)
            except Exception as error:
                print(f'Error: {error}')

        elif opcion == '0':
            break
        else:
            print('Opción inválida. Intente nuevamente.')

def menu_cartola():
    print("\n--- CARTOLA ---")

    try:
        numero_cuenta = input("Ingrese número de cuenta: ").strip()

        cuenta = cuenta_dao.buscar_por_numero(numero_cuenta)

        if cuenta is None:
            print("\nLa cuenta no existe.")
            return

        movimiento_dao = MovimientoDAO()
        movimientos = movimiento_dao.listar_por_cuenta(numero_cuenta)

        print("\n" + "=" * 85)
        print("                              CARTOLA")
        print("=" * 85)
        print(f"Cuenta : {cuenta.numero}")
        print(f"Cliente: {cuenta.cliente.nombre}")
        print(f"Saldo  : ${cuenta.saldo:,.0f}".replace(",", "."))
        print("-" * 85)

        if not movimientos:
            print("No existen movimientos registrados para esta cuenta.")
            print("=" * 85)
            return

        print(
            f"{'Fecha':<20}"
            f"{'Tipo':<12}"
            f"{'Monto':>14}   "
            f"Descripción"
        )
        print("-" * 85)

        for movimiento in movimientos:
            fecha = movimiento[4]
            tipo = movimiento[1]
            monto = movimiento[2]
            descripcion = movimiento[3]

            fecha_formateada = fecha[:16].replace("T", " ")
            monto_formateado = f"${monto:,.0f}".replace(",", ".")

            print(
                f"{fecha_formateada:<20}"
                f"{tipo:<12}"
                f"{monto_formateado:>14}   "
                f"{descripcion}"
            )

        print("=" * 85)

    except Exception as error:
        print(f"\nNo se pudo consultar la cartola: {error}")


# ==========================================================
# INDICADOR UF
# ==========================================================
def consultar_uf():

    print("\n--- INDICADOR UF ---")

    try:
        indicador = UFService.obtener_uf()

        if indicador is None:
            print("No fue posible consultar el valor de la UF.")
            return

        print("\nInformación actual de la UF")
        print("-" * 40)
        print(f"Valor UF: ${indicador.valor:,.2f}")
        print(f"Fecha: {indicador.fecha}")
        print("-" * 40)

    except Exception as error:
        print(f"\nError al consultar la UF: {error}")

def consultar_dolar():

    print("\n--- VALOR DEL DÓLAR ---")

    try:
        indicador = DolarService.obtener_dolar()

        if indicador is None:
            print("No fue posible consultar el valor del dólar.")
            return

        print("\nInformación actual del dólar")
        print("-" * 40)
        print(f"Valor dólar: ${indicador.valor:,.2f}")
        print(f"Fecha: {indicador.fecha}")
        print("-" * 40)

    except Exception as error:
        print(f"\nError al consultar el dólar: {error}")        


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    crear_tablas()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            menu_clientes()

        elif opcion == "2":

            menu_cuentas()

        elif opcion == "3":

            menu_operaciones()

        elif opcion == "4":

            menu_cartola()

        elif opcion == "5":

            consultar_uf()

        elif opcion == "6":
              
            consultar_dolar()    

        elif opcion == "0":

            print("\nPrograma finalizado.")
            break

        else:

            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()

