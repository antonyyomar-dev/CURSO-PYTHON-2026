EJERCICIO 1

Escribir una clase llamada CuentaBancaria que tiene lo siguiente:

• Un campo llamado nombre que almacena el nombre del titular de la 
cuenta.

• Un campo llamado saldo que almacena la cantidad de dinero en la cuenta.

• Un campo llamado tasaInteres que almacena la tasa de interés de la 
cuenta (como un porcentaje).

• Un constructor que simplemente establece los valores de los tres campos 
anteriores.

• Un método llamado aplicaInteres() que no acepta argumentos y aplica el 
interés a la cuenta. Solo debe modificar el campo de saldo y no devolver 
nada. 

Por ejemplo, si la cuenta tiene 1000 y la tasa de interés es del 3%, 
entonces la cantidad variable debe cambiarse a 1030 (1000 + 3% de 
interés).

A continuación, pruebe la clase, mediante la creación de un nuevo objeto 
llamado CuentaBancaria Para un usuario nombrado Juan De Arona que tiene 
1000 al 3% de interés. A continuación, haga lo siguiente:

• Utilice el método aplicaInteres() para aplicar los intereses a la cuenta.

• Imprima cuánto dinero hay ahora en la cuenta después de aplicar los 
intereses.

• Cambie la tasa de interés de la cuenta a 2%.

• Utilice el método aplicaInteres() para volver a aplicar los intereses a la 
cuenta.

• Imprima cuánto dinero hay ahora en la cuenta después de aplicar el interés 
nuevamente.

```python

```

EJERCICIO 2

Desarrollar un programa en Python para la clase estudiante, que tendrá como 
atributos, el código del alumno, su nombre, el curso, la notal del examen 
parcial y la nota del examen final. La clase, además del constructor y el str(), 
tendrá un método para calcula la nota fila, según la siguiente fórmula:

Nota final = parcial * 0.4 + final * 0.6

```python

```

EJERCICIO 3 

Desarrollar una aplicación que pueda gestionar los clientes (registrar, 
actualizar, eliminar y reportar información sobre clientes). Cada cliente debe 
tener:

* Un DNI
* un nombre
* una dirección
* un número de teléfono
* una dirección de correo electrónico. 
* Una indicación de cliente preferente: True o False

El sistema debe permitir generar dos reportes: uno con todos los clientes y otro 
con clientes filtrados por nombre.

Los clientes están almacenados en una baseCLientes (la baseClientes tiene 
como atributo una lista de clientes)

Clase cliente (con los atributos descritos y el método verCliente [muestra los 
datos de un cliente] )

Clase baseCLientes (listaClientes (lista que almacena objetos Cliente) y los 
métodos: registrarCliente [agrega un cliente a la baseCLientes], 
actualizarCliente [actualiza la información de un cliente preexistente], 
eliminarCliente [elimina cliente, se busca por su DNI para eliminar], 
visualizarClientes [ver listado de clientes], busquedaCliente [buscar cliente 
por nombre]).

El programa debe preguntar al usuario por una opción del siguiente menú: 

* (1) Añadir cliente
* (2) Buscar cliente
* (3) Actualizar cliente
* (4) Eliminar cliente
* (5) Listar todos los clientes
* (6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:

*En la opción 1, preguntar los datos del cliente, según el diseño presentado. 
o Se valida que DNI sea un string de 8 números
o El nombre no puede tener números
o El teléfono son 9 dígitos (tip: considere que es un string de 9 dígitos)
o El correo se forma con la inicial en minúscula del nombre seguido del 
apellido, luego @ seguido del dominio empsac y terminando con .com
o Para el preferente se debe ingresar 1 o 0, si es uno se graba True, en caso 
contrario False
* En la opción 2, preguntar por el DNI del cliente y eliminar al cliente. Debe 
verificar que el cliente exista
* Para la Opción 5 mostrar un reporte en donde se muestre el DNI y otros datos, 
similar al siguiente:

DNI| Nombre| Dirección|Teléfono| Email| Preferente|
---|-------|----------|--------|------|-----------|
08804832|Robert Fischer| Arges 141| 945025205| rFischer@empsac.com| True
12345678|Boris Spassky| Apeliotas 361| 998325782| bSpassky@empsac.com| False

```python

```

EJERCICIO 4 

### Enunciado: Programa de Créditos — FinanTek
La administradora de la entidad financiera “FinanTek” requiere un programa orientado a objetos para otorgar créditos a familias emprendedoras en Lima.

Cada representante debe registrarse con:
- DNI  
- Edad  
- Número de hijos menores de 18 años  
- Ingreso familiar mensual (S/.)  
- Metros cuadrados de propiedad (m²)  
  - Si no tiene bienes → valor = 0

### Cálculo de calificación
calificación = edad + número de hijos + (ingreso mensual) / (m² de propiedad + 1)

### Rangos de crédito
| Calificación      | Monto Máximo (S/.) |
|-------------------|---------------------|
| 0 < 150           | 35,000              |
| 151 – 350         | 45,000              |
| > 350             | 60,000              |

### Requerimientos
- Elaborar el diagrama de clases.  
- Crear una clase **Representante** y una clase **Base**, donde la clase Base mantenga una lista de objetos Representante.  
- Ingresar datos de varios representantes.  
- Generar un listado completo (incluyendo la calificación de cada uno).  
- Dado un monto de crédito, mostrar qué representantes califican para dicho monto.  
- Implementar un método que calcule el **monto total** a desembolsar para los representantes con **más de 2 hijos**.  
- Implementar un método para **buscar un representante por DNI** y mostrar:
  - Sus datos  
  - Monto de crédito que le corresponde  
  - Si no existe → “No encontrado”  
- Crear un menú que permita administrar todas las funciones anteriores.  
- Usar atributos privados y decoradores (getters/setters).

```python

```

EJERCICIO 5

### Enunciado: Gestión de Bicicletas
Una tienda requiere un programa para gestionar bicicletas. Todas cuentan con:
- Material (aluminio, carbono, titanio)
- Tamaño de ruedas
- Cantidad de platos

Tipos disponibles:
- Montañera
- Ruta
- Urbana

### Especificaciones adicionales
**Montañeras:** suspensión rígida, delantera o doble  
**Ruta:** manubrio drop-bar o regular-bar  
**Urbanas:** pueden incluir canastilla

### Precio base
| Tipo        | Precio |
|-------------|--------|
| Montañera   | S/ 1450 |
| Ruta        | S/ 2500 |
| Urbana      | S/ 900 |

### Variaciones del precio final
**Montañera = base + suspensión**
| Suspensión | Costo |
|------------|--------|
| Rígidas    | S/ 250 |
| Delantera  | S/ 295 |
| Doble      | S/ 600 |

**Ruta = base + porcentaje por manubrio**
| Manubrio     | Monto |
|--------------|--------|
| Drop-bar     | +5% base |
| Regular-bar  | +7.5% base |

**Urbana = base + canastilla (opcional)**
| Adicional  | Costo |
|------------|--------|
| Canastilla | S/ 115 |

### Requerimientos
a. Implementar clases con herencia y registrar 6 bicicletas (2 por tipo).  
b. Listar todas las bicicletas mostrando todas sus características y el precio final.  
c. Crear un método que indique cuántas bicicletas hay por tipo.  
d. Mostrar la bicicleta con mayor y menor precio final.

```python

```

EJERCICIO 6 

Enunciado: Gestión de Pasteles e Ingredientes

Diseñar un modelo orientado a objetos e implementar un programa en Python para administrar un pastel junto con sus ingredientes. Considere que un mismo ingrediente puede ser utilizado en varios pasteles.

Datos del pastel
- Nombre  
- Cantidad de personas  
- Precio  

Datos del ingrediente
- Nombre  
- Unidad de medida (gramos, piezas, mililitros, etc.)  
- Cantidad  
- Calorías por porción  

Métodos requeridos
- Contar la cantidad total de ingredientes del pastel.  
- Calcular las calorías totales del pastel (sumando las calorías de cada ingrediente).

```python

```

EJERCICIO 7 

Caso: Sistema de Almacén — Empresa FlowerFull S.A.C

La empresa FlowerFull S.A.C., dedicada a la venta de productos 100% naturales, ha incrementado significativamente sus ventas. Debido a ello, requiere un sistema orientado a objetos que permita administrar productos y proveedores dentro del almacén.

Reglas del negocio

Datos del proveedor
- RUC  
- Razón social  
- Categoría  
- Dirección  
- Teléfono  

Datos del producto
- IdProducto  
- Nombre  
- Tipo (polvo o líquido)  
- Cantidad  
- Categoría (A, B, C)  
- Año  
- Precio  
- Proveedor (objeto proveedor asociado)

*Los métodos internos de cada clase quedan a criterio del desarrollador según las necesidades del sistema.*

---

Requerimientos del programa
1. Registrar productos conforme llegan de los proveedores.  
2. Implementar las clases necesarias utilizando POO.  
3. Usar listas para almacenar “N” productos.  
4. Modificar los datos de un producto existente.  
5. Mostrar los productos de categoría **A** cuyo proveedor sea **Natura**.  
6. Eliminar todos los productos del proveedor **Herbalife**.  
7. Eliminar todos los productos vencidos (año < 2025).

---

Menú del sistema
1. Insertar producto  
2. Insertar proveedor  
3. Modificar producto  
4. Eliminar productos vencidos  
5. Reportes (mostrar todos los productos en stock)

```python

```

