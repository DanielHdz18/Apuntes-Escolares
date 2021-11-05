import os
import shutil

extensiones = ['.aux', '.bbl', '.bcf', '.blg', '.run.xml', '.synctex.gz', '.log', '.toc', '.tkzfonct.gnuplot', '.out']

def Extraer_dir_archivo():
    ruta_archivo = os.path.abspath(__file__)
    ruta, archivo = os.path.split(ruta_archivo)
    return ruta

def Subcarpetas(lista, dir):
    folder = list()
    for nombre in lista:
        if os.path.isdir(nombre):
            folder.append(os.path.join(dir,nombre))
    return folder

directorio = Extraer_dir_archivo()
archivos = os.listdir(directorio)
directorios = Subcarpetas(archivos,directorio)
directorios.insert(0,directorio)

def Archivos_eliminables():
    eliminables = []
    for terminaciones in extensiones:
        for carpetas in directorios:
            for archivos in os.listdir(carpetas):
                if archivos.endswith(terminaciones):
                    eliminables.append(os.path.join(carpetas,archivos))
                    print(f'El archivo {os.path.join(carpetas,archivos)} sera eliminado')
    print(f'Un total de {len(eliminables)} archivos seran quitados')
    return eliminables
print('Modulo de limpieza para archivos compilados de latex')
print('Creado por. Daniel Hernandez')
print('Buscando archivos')
print('Desea incluir los pdfs? (S/N)')
respuesta = input()
if respuesta == 'S':
    extensiones.append('.pdf')
print('Los siguientes archivos seran borrados:')
borrables = Archivos_eliminables()
print('¿Desea continuar con el borrado de estos archivos? (S/N)')
respuesta2 = input()
if respuesta2 != 'S':
    print('Ningun archivo borrado')
else:
    for file in borrables:
        os.unlink(file)
    print('Archivos eliminado con exito')

    


