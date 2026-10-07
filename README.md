# Banco Cooperativo Andino

## Proyecto de Programación Orientada a Objeto Seguro

Sistema bancario desarrollado en **Python** para gestionar clientes, cuentas bancarias y operaciones financieras, aplicando principios de Programación Orientada a Objetos, persistencia de datos, validaciones y manejo de excepciones.

---

## Integrantes

* Martin Castro
* Fabian Pedregal Araya

**Sección:** 114-2A-F2
**Docente:** Michael Arjel
**Curso:** Programación Orientada a Objeto Seguro - TI3V21

---

## Tecnologías utilizadas

* Python 3
* SQLite
* Requests
* Programación Orientada a Objetos (POO)
* Git
* GitHub

---

## Funcionalidades principales

### Gestión de clientes

El sistema permite:

* Crear clientes.
* Listar clientes.
* Modificar clientes.
* Eliminar clientes.
* Validar RUT chileno.
* Registrar si un cliente posee mora.

### Gestión de cuentas

El sistema trabaja con tres tipos de cuentas:

* Cuenta de Ahorro.
* Cuenta Corriente.
* Cuenta Vista.

Cada tipo de cuenta posee un comportamiento diferente al realizar operaciones.

### Operaciones bancarias

El sistema permite:

* Realizar depósitos.
* Realizar giros.
* Actualizar saldos.
* Registrar movimientos.
* Generar transacciones.
* Registrar detalles de las transacciones.
* Consultar la cartola de una cuenta.

### Indicadores económicos

El sistema consulta información externa mediante API:

* Valor de la UF.
* Valor del dólar.

Las consultas utilizan `requests`, tiempo máximo de espera mediante `timeout` y manejo de errores cuando no existe conexión o la API no responde correctamente.

---

## Reglas de negocio

El sistema implementa reglas que bloquean operaciones cuando no se cumplen las condiciones establecidas.

### 1. Cliente con mora

Un cliente que posee mora activa no puede abrir una nueva cuenta.

Se utiliza la excepción personalizada:

```text
ClienteEnMoraError
```

### 2. Saldo insuficiente

Las cuentas que no permiten sobregiro no pueden realizar un giro superior al saldo disponible.

Se utiliza la excepción personalizada:

```text
SaldoInsuficienteError
```

La Cuenta Corriente posee un límite de sobregiro configurado.

---

## Programación Orientada a Objetos

### Encapsulamiento

Se utilizan atributos privados y propiedades mediante:

```python
@property
```

y:

```python
@setter
```

Los setters permiten validar los datos antes de almacenarlos.

### Herencia

Las cuentas específicas heredan de la clase base `Cuenta`.

```text
Cuenta
├── CuentaAhorro
├── CuentaCorriente
└── CuentaVista
```

También se utilizan clases relacionadas con empleados y sus permisos.

### Polimorfismo

Cada tipo de cuenta implementa su propio comportamiento para operaciones como:

```python
girar()
calcular_interes()
```

Por ejemplo:

* `CuentaAhorro` no permite retirar más que el saldo.
* `CuentaVista` no permite sobregiro.
* `CuentaCorriente` permite utilizar un límite de sobregiro.

---

## Persistencia de datos

El proyecto utiliza **SQLite** para almacenar la información del sistema.

Entre las entidades almacenadas se encuentran:

* Clientes.
* Cuentas.
* Movimientos.
* Transacciones.
* Detalles de transacciones.

Las operaciones de acceso a datos se encuentran separadas mediante clases DAO.

---

## Seguridad y validaciones

El proyecto incorpora diferentes medidas de validación:

* Validación del RUT chileno.
* Validación de nombres.
* Validación de montos positivos.
* Validación de cuentas existentes.
* Validación de clientes existentes.
* Validación de tipos de movimiento.
* Control de saldo insuficiente.
* Control de clientes con mora.
* Excepciones personalizadas.
* Manejo de errores de conexión con APIs externas.
* Uso de consultas SQL parametrizadas para evitar insertar directamente valores proporcionados por el usuario en las consultas SQL.

---

## Arquitectura del proyecto

```text
Banco-Cooperativo-Andino/
│
├── dao/
│   ├── cliente_dao.py
│   ├── cuenta_dao.py
│   ├── database.py
│   ├── movimiento_dao.py
│   └── transaccion_dao.py
│
├── exceptions/
│   ├── cliente_en_mora_error.py
│   └── saldo_insuficiente_error.py
│
├── model/
│   ├── cliente.py
│   ├── cuenta.py
│   ├── cuenta_ahorro.py
│   ├── cuenta_corriente.py
│   ├── cuenta_vista.py
│   ├── detalle_transaccion.py
│   ├── empleado.py
│   ├── enums.py
│   ├── ejecutivo.py
│   ├── cajero.py
│   ├── indicador_uf.py
│   ├── movimiento.py
│   └── transaccion.py
│
├── services/
│   ├── dolar_service.py
│   ├── operacion_service.py
│   └── uf_service.py
│
├── banco.db
├── main.py
├── .gitignore
└── README.md
```

---

## Ejecución del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/martin0800/Banco-Cooperativo-Andino.git
```

### 2. Entrar al proyecto

```bash
cd Banco-Cooperativo-Andino
```

### 3. Instalar Requests

```bash
pip install requests
```

### 4. Ejecutar el sistema

```bash
python main.py
```

---

## API externa

El proyecto utiliza la API de **mindicador.cl** para consultar indicadores económicos.

Se consultan:

* UF.
* Dólar.

Las solicitudes utilizan un tiempo máximo de espera para evitar que el programa quede esperando indefinidamente.

Si la API no responde o existe un problema de conexión, el sistema captura el error y continúa funcionando sin provocar un cierre inesperado del programa.

---

## Pruebas realizadas

Durante las pruebas del sistema se verificaron, entre otros, los siguientes casos:

* Inicio correcto del programa.
* Creación y listado de clientes.
* Validación de RUT inválido.
* Modificación y eliminación de clientes.
* Creación de Cuenta Ahorro.
* Creación de Cuenta Corriente.
* Creación de Cuenta Vista.
* Sobregiro de Cuenta Corriente.
* Bloqueo de giro por saldo insuficiente.
* Bloqueo de apertura de cuenta para cliente con mora.
* Depósitos.
* Giros.
* Registro de transacciones.
* Registro de detalles de transacciones.
* Consulta de cartola.
* Consulta de UF.
* Consulta de dólar.
* Manejo de errores de conexión con la API.

---

## Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó Inteligencia Artificial como herramienta de apoyo al aprendizaje y desarrollo.

La IA se utilizó principalmente para:

* Comprender conceptos de Programación Orientada a Objetos.
* Revisar y explicar errores de código.
* Apoyar la estructura del proyecto.
* Sugerir mejoras de validación.
* Explicar el funcionamiento de SQLite y consultas SQL.
* Apoyar la implementación y revisión de excepciones.
* Preparar casos de prueba.
* Apoyar la documentación del proyecto.

La implementación fue ejecutada, probada y revisada por los integrantes del proyecto.

La Inteligencia Artificial fue utilizada como herramienta de apoyo y no como sustituto de la comprensión del código.

---

## Objetivo del proyecto

El objetivo es desarrollar un sistema bancario funcional que permita aplicar los principales conceptos de Programación Orientada a Objetos Segura, incorporando:

* Encapsulamiento.
* Herencia.
* Polimorfismo.
* Abstracción.
* Persistencia de datos.
* Validación de información.
* Excepciones personalizadas.
* Consultas SQL parametrizadas.
* Consumo de APIs externas.
* Manejo de errores.
* Control de reglas de negocio.

---

## Repositorio

Proyecto disponible públicamente en GitHub:

**Banco Cooperativo Andino**

https://github.com/martin0800/Banco-Cooperativo-Andino
