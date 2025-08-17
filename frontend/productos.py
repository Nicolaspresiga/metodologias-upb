from utils.terminal import limpiar
import backend.productos as Productos
from tabulate import tabulate

headers = ["ID", "Nombre", "Precio", "Cantidad"]

def solicitarProducto():
    id_ = input("Ingrese un ID de producto: ").strip()
    nombre= input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio: ").strip() or 0)
    cantidad = int(input("Ingrese la cantidad: ").strip() or 0)
    return (id_, nombre, precio, cantidad)

def listarProductos():
    limpiar()
    items = Productos.listarProductos()
    if items:
        print(tabulate(items, headers=headers, tablefmt="rounded_grid"))
    else:
        print("No hay productos registrados.")

def consultarProducto():
    limpiar()
    id_ = input("Ingrese el ID del producto: ").strip()
    prod = Productos.consultarProducto(id_)
    if prod:
        print(tabulate([prod], headers=headers, tablefmt="rounded_grid"))
    else:
        print("Producto no encontrado.")

def agregarProducto():
    limpiar()
    nuevo = solicitarProducto()
    creado = Productos.crearProducto(*nuevo)
    if creado:
        print("Producto agregado exitosamente...")
    else:
        print("Error: ya existe un producto con ese ID.")

def actualizarProducto():
    limpiar()
    print("== Actualizar producto (deje vacío lo que no cambie) ==")
    id_ = input("ID del producto: ").strip()
    actual = Productos.consultarProducto(id_)
    if not actual:
        print("No existe un producto con ese ID.")
        return

    nombre= input(f"Nombre [{actual[1]}]: ").strip()
    precio_str = input(f"Precio [{actual[2]}]: ").strip()
    cantidad_str = input(f"Cantidad [{actual[3]}]: ").strip()

    nombre= nombre if nombre != "" else None
    precio = float(precio_str) if precio_str != "" else None
    cantidad = int(cantidad_str) if cantidad_str != "" else None

    ok = Productos.actualizarProducto(id_, nombre, precio, cantidad)

def eliminarProducto():
    limpiar()
    id_ = input("Ingrese el ID del producto a eliminar: ").strip()
    ok = Productos.eliminarProducto(id_)
    if ok:
        print("Producto eliminado exitosamente...")
    else:
        print("Error: verifique que el producto con ese ID exista.")

def mostrarMenuDeProductos():
    while True:
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("1. Listar productos")
        print("2. Consultar producto")
        print("3. Agregar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Volver")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            listarProductos()
        elif opcion == "2":
            consultarProducto()
        elif opcion == "3":
            agregarProducto()
        elif opcion == "4":
            actualizarProducto()
        elif opcion == "5":
            eliminarProducto()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")
