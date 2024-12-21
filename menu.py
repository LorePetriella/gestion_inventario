from funciones import (
    inicializar_tabla, agregar_producto, mostrar_productos,
    actualizar_producto, eliminar_producto, buscar_producto, reporte_bajo_stock
)
from colorama import Fore, Style, init
init(autoreset=True)


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print(Fore.MAGENTA + "\nMenú de Gestión de Inventario" + Style.RESET_ALL)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Actualizar cantidad de producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("0. Salir")

def main():
    """Ejecuta el menú interactivo."""
    inicializar_tabla()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "0":
            print(Fore.GREEN + "Saliendo del programa. ¡Hasta la próxima!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
