from frontend.productos import mostrarMenuDeProductos

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Productos")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrarMenuDeProductos()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
