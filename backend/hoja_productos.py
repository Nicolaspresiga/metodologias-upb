from backend.excel import obtenerLibro

libro = obtenerLibro()
titulo_hoja = "productos"

def inicializarHoja():
    hoja = libro.create_sheet(title=titulo_hoja)

    hoja.column_dimensions['A'].width = 15
    hoja.column_dimensions['B'].width = 15
    hoja.column_dimensions['C'].width = 15
    hoja.column_dimensions['D'].width = 15

    cabeceras = ("ID", "Nombre", "Precio", "Cantidad")

    hoja.append (cabeceras)

    return hoja

def obtenerHojaDeProductos():
    if titulo_hoja in libro.sheetnames:
        return libro[titulo_hoja]
    else:
        return inicializarHoja