import sqlite3


DB_NAME = "banco.db"


def obtener_conexion():
    conexion = sqlite3.connect(DB_NAME)

    # Permite utilizar claves foráneas en SQLite
    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion


def crear_tablas():
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS clientes (
            rut TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            tiene_mora INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS empleados (
            rut TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cuentas (
            numero TEXT PRIMARY KEY,
            rut_cliente TEXT NOT NULL,
            tipo TEXT NOT NULL,
            saldo REAL NOT NULL DEFAULT 0,
            fecha_apertura TEXT NOT NULL,
            tasa_interes REAL DEFAULT 0,
            limite_sobregiro REAL DEFAULT 0,

            FOREIGN KEY (rut_cliente)
                REFERENCES clientes(rut)
        );

        CREATE TABLE IF NOT EXISTS creditos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut_cliente TEXT NOT NULL,
            monto REAL NOT NULL,
            fecha TEXT NOT NULL,
            estado TEXT NOT NULL,

            FOREIGN KEY (rut_cliente)
                REFERENCES clientes(rut)
        );

        CREATE TABLE IF NOT EXISTS transacciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_cuenta TEXT NOT NULL,
            tipo TEXT NOT NULL,
            total REAL NOT NULL,
            fecha TEXT NOT NULL,

            FOREIGN KEY (numero_cuenta)
                REFERENCES cuentas(numero)
        );

        CREATE TABLE IF NOT EXISTS detalles_transaccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaccion_id INTEGER NOT NULL,
            concepto TEXT NOT NULL,
            monto REAL NOT NULL,

            FOREIGN KEY (transaccion_id)
                REFERENCES transacciones(id)
                ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_cuenta TEXT NOT NULL,
            tipo TEXT NOT NULL,
            monto REAL NOT NULL,
            descripcion TEXT,
            fecha TEXT NOT NULL,

            FOREIGN KEY (numero_cuenta)
                REFERENCES cuentas(numero)
        );
    """)

    conexion.commit()
    conexion.close()