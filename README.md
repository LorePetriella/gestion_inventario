
# Sistema de Gestión de Inventario

Este proyecto es un sistema de gestión de inventario que permite realizar operaciones básicas como:

- Agregar productos.
- Mostrar productos.
- Actualizar la cantidad de un producto.
- Eliminar productos.
- Buscar productos específicos.
- Generar reportes de bajo stock.

## Ejecución del Programa

1. Asegúrate de estar en el directorio que contiene los archivos `menu.py` y `funciones.py`.
2. Ejecuta el programa con el siguiente comando:
   ```bash
   python menu.py
   ```

## Opciones del Menú

### Agregar Producto

Permite ingresar un nuevo producto al inventario. Deberás ingresar los siguientes datos:

- **Nombre**
- **Descripción**
- **Cantidad** (número entero)
- **Precio** (número decimal)
- **Categoría**

**Ejemplo de entrada:**

```plaintext
Nombre: Laptop
Descripción: Portátil de 15 pulgadas
Cantidad: 5
Precio: 1200.50
Categoría: Electrónica
```

### Mostrar Productos

Muestra una lista de todos los productos registrados en el inventario.

**Ejemplo de salida:**

```yaml
ID: 1, Nombre: Laptop, Descripción: Portátil de 15 pulgadas, Cantidad: 5, Precio: 1200.5, Categoría: Electrónica
```

### Actualizar Cantidad de Producto

Permite actualizar la cantidad de un producto existente. Necesitarás proporcionar el **ID** del producto y la nueva cantidad.

### Eliminar Producto

Elimina un producto del inventario proporcionando su **ID**.

### Buscar Producto

Busca un producto en el inventario utilizando su **ID**.

**Ejemplo de salida:**

```yaml
Producto encontrado:
ID: 1, Nombre: Laptop, Descripción: Portátil de 15 pulgadas, Cantidad: 5, Precio: 1200.5, Categoría: Electrónica
```

### Reporte de Bajo Stock

Genera un informe de productos con cantidad igual o menor a 10 unidades.

**Ejemplo de salida:**

```yaml
Productos con stock menor o igual a 10:
ID: 2, Nombre: Teclado, Cantidad: 3
```

### Salir

Finaliza la ejecución del programa.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **`menu.py`**: Archivo principal que gestiona la interacción con el usuario.
- **`funciones.py`**: Contiene las funciones que implementan las operaciones del sistema de inventario.
- **`inventario.db`**: Archivo SQLite generado automáticamente para almacenar los datos del inventario.




