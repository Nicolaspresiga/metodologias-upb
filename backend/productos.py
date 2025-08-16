from backend.hoja_productos import obtenerHojaDeProductos

from backend.excel import guardarHoja

hoja = obtenerHojaDeProductos()

def listarProductos():
    filas = []

    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)

    for idx, refFila in enumerate(refFilas, start=2):
        valores = [celda.value for celda in refFila]

        if any(valores): 
            filas.append([idx] + valores)

    return filas

def consultarProducto(ID, soloValores = True):
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == ID:
            if soloValores:
                valores = []
                valores.append(idx)
                
                for celda in refFila:
                    valores.append(celda.value)
                
                return valores
            else:
                return refFila
    else:
        return None

def crearProducto(ID, Nombre, Precio, Cantidad):
    if consultarProducto(ID) != None:
        return False
    
    productos = (ID, Nombre, Precio, Cantidad)

    hoja.append(productos)

    guardarHoja (hoja)

    return True

def eliminarProducto(ID):
    producto = consultarProducto (ID)

    if producto == None:
        return False
    
    hoja.delete_rows(producto[0]+2)

    guardarHoja(hoja)

    return True

def actualizarProducto(ID, Nombre, Precio, Cantidad):
    nuevos_valores = (ID, Nombre, Precio, Cantidad)

    refFila = consultarProducto(ID, False)

    if refFila == None:
        return False
    
    for celda, nuevo_valor in zip (refFila, nuevos_valores):
        celda.value = nuevo_valor

    guardarHoja(hoja)

    return True