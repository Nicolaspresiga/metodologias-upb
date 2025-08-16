import os

def limpiar():
    if os.name == 'nt': #Para Windows
        os.system('cls')
    else: #Para Unix
        os.system('clear')
    
