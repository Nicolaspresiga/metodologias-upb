from backend.hoja_productos import obtenerHojaDeProductos


hoja = obtenerHojaDeProductos()

def listarProductos():
    filas = []

    refFilas = hoja.iter_rows(min_row=2, min_col=1, max_col=4)

    for idx, refFila in enumerate(refFilas, start=2):
        valores = [celda.value for celda in refFila]

        if any(valores): 
            filas.append([idx] + valores)
    return filas
    

def consultarProducto(ID):
    refFilas = hoja.iter_rows(min_row=2, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if str(refFila[0].value).strip() == str(ID).strip():
            valores = [idx]
            for celda in refFila:
                valores.append(celda.value)
            return valores
    return None