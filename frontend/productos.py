from tabulate import tabulate
from backend.productos import listarProductos, consultarProducto

def mostrarMenu():
    print("\n--- MENU DE PRODUCTOS ---")
    print("1. Listar productos")
    print("2. Consultar producto por ID")
    print("3. Salir")

def main():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            productos = listarProductos()
            if productos:
                print("\n--- LISTA DE PRODUCTOS ---")
                header = ["ID", "Nombre", "Precio", "cantidad"]
                print(tabulate(productos, headers=header, tablefmt="rounded_grid"))
            else:
                print("No hay productos disponibles.")
        
        elif opcion == "2":
            ID = input("Ingrese el ID del producto a consultar: ").strip()
            resultado = consultarProducto(ID)
            if resultado:
                print(f"\nProducto encontrado:")
                header = ["ID", "Nombre", "Precio", "Cantidad"]
                print(tabulate([resultado], headers=header, tablefmt="rounded_grid"))
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

    if __name__ == "__main__":
        main()