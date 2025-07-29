import openpyxl
import os

archivo = "backend/datos_productos.xlsx"

def obtenerLibro ():
    if os.path.exists(archivo):
        return openpyxl.load_workbook(archivo)
    else:
        return openpyxl.Workbook()
    
def guardarHoja(hoja):
    libro = hoja.parent

    libro.save(archivo)