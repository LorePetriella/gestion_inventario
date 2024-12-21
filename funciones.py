import sqlite3

from colorama import Fore, Style, init
init(autoreset=True)




def conectar_base_datos():
    """Establece la conexión con la base de datos SQLite."""
    return sqlite3.connect("inventario.db")

def inicializar_tabla():
    """Crea la tabla productos si no existe."""
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_producto():
    """Agrega un producto al inventario."""
    nombre = input("Introduce el nombre del producto: ").strip()
    descripcion = input("Introduce la descripción del producto: ").strip()
    cantidad = input("Introduce la cantidad: ").strip()
    precio = input("Introduce el precio: ").strip()
    categoria = input("Introduce la categoría: ").strip()

    if not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
        print(Fore.RED + "Cantidad y precio deben ser números válidos." + Style.RESET_ALL)
        return

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, int(cantidad), float(precio), categoria))
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + f"Producto '{nombre}' agregado correctamente." + Style.RESET_ALL)

def mostrar_productos():
    """Muestra todos los productos en el inventario."""
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print(Fore.CYAN + "\nInventario de productos:" + Style.RESET_ALL)
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
    else:
        print(Fore.YELLOW + "El inventario está vacío." + Style.RESET_ALL)

def actualizar_producto():
    """Actualiza la cantidad de un producto específico."""
    id_producto = input("Introduce el ID del producto a actualizar: ").strip()
    nueva_cantidad = input("Introduce la nueva cantidad: ").strip()

    if not id_producto.isdigit() or not nueva_cantidad.isdigit():
        print(Fore.RED + "ID y cantidad deben ser números válidos." + Style.RESET_ALL)
        return

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (int(nueva_cantidad), int(id_producto)))
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + "Cantidad actualizada correctamente." + Style.RESET_ALL)

def eliminar_producto():
    """Elimina un producto del inventario por su ID."""
    id_producto = input("Introduce el ID del producto a eliminar: ").strip()

    if not id_producto.isdigit():
        print(Fore.RED + "El ID debe ser un número válido." + Style.RESET_ALL)
        return

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (int(id_producto),))
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + "Producto eliminado correctamente." + Style.RESET_ALL)

def reporte_bajo_stock():
    """Genera un reporte de productos con bajo stock."""
    limite = 10
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print(Fore.CYAN + f"\nProductos con stock menor o igual a {limite}:" + Style.RESET_ALL)
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
    else:
        print(Fore.YELLOW + "No hay productos con bajo stock." + Style.RESET_ALL)

def buscar_producto():
    """Busca un producto por su ID."""
    id_producto = input("Introduce el ID del producto a buscar: ").strip()

    if not id_producto.isdigit():
        print(Fore.RED + "El ID debe ser un número válido." + Style.RESET_ALL)
        return

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (int(id_producto),))
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        print(Fore.CYAN + f"\nProducto encontrado:\nID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "No se encontró un producto con ese ID." + Style.RESET_ALL)
