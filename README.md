# Banco Cooperativo Andino

## Proyecto de Programación Orientada a Objeto Seguro

Sistema bancario desarrollado en Python para gestionar clientes, cuentas bancarias y operaciones financieras, aplicando principios de Programación Orientada a Objetos, persistencia de datos y validaciones de seguridad.

### Integrantes

- Martin Castro
- Fabian Pedregal Araya

### Sección

114-2A-F2

### Docente

Michael Arjel

### Curso

Programación Orientada a Objeto Seguro - TI3V21

---

## Tecnologías utilizadas

- Python 3
- SQLite
- Requests
- Programación Orientada a Objetos
- Git
- GitHub

---

## Funcionalidades principales

### Gestión de clientes

El sistema permite:

- Crear clientes.
- Listar clientes.
- Modificar clientes.
- Eliminar clientes.
- Validar RUT chileno.
- Registrar si un cliente posee mora.

### Gestión de cuentas

El sistema permite trabajar con tres tipos de cuentas:

- Cuenta de Ahorro.
- Cuenta Corriente.
- Cuenta Vista.

Cada tipo de cuenta posee un comportamiento diferente al realizar operaciones.

### Operaciones bancarias

El sistema permite:

- Realizar depósitos.
- Realizar giros.
- Registrar movimientos.
- Generar transacciones.
- Registrar detalles de las transacciones.
- Consultar la cartola de una cuenta.

### Indicadores económicos

El sistema consulta información externa mediante una API:

- Valor de la UF.
- Valor del dólar.

La consulta utiliza `requests`, tiempo máximo de espera (`timeout`) y manejo de errores cuando no existe conexión o la API no responde correctamente.

---

## Programación Orientada a Objetos

El proyecto utiliza diferentes conceptos de POO.

### Encapsulamiento

Se utilizan atributos privados y propiedades mediante `@property` y `@setter`.

Los setters permiten validar los datos antes de almacenarlos.

### Herencia

Las cuentas específicas heredan de la clase base `Cuenta`.

```text
Cuenta
├── CuentaAhorro
├── CuentaCorriente
└── CuentaVista