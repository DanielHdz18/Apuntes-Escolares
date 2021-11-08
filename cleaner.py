import os
import send2trash

extensiones = ['.aux', '.bbl', '.bcf', '.blg', '.run.xml', '.synctex.gz', '.log', '.toc', '.tkzfonct.gnuplot', '.out', '.synctex(busy)']

def main():
    print('Modulo de limpieza para archivos compilados de latex')
    print('Creado por Daniel Hernandez')
    print('Buscando archivos')
    incluir_pdfs = input('Desea incluir los pdfs? (S/N)\n')
    if incluir_pdfs == 'S':
        extensiones.append('.pdf')
    print('Los siguientes archivos seran borrados:')
    Archivos_eliminables = Buscar_archivos_eliminables()
    if len(Archivos_eliminables) == 0:
        print('\x1b[2K\r')
        print('Felicidades no tienes ningun archivo por eliminar')
    else:
        confirmacion_borrado = input('¿Desea continuar con el borrado de estos archivos? (S/N)\n')
        if confirmacion_borrado != 'S':
            print('Ningun archivo borrado')
        else:
            for archivo in Archivos_eliminables:
                send2trash.send2trash(archivo)
            print('Archivos movidos a la papelera con exito')    

def Buscar_archivos_eliminables():
    Archivos = list()
    Carpetas = [os.getcwd()]
    archivos_padre = os.listdir(str(os.getcwd()))

    for nombre in archivos_padre:
        if os.path.isdir(nombre):
            Carpetas.append(nombre)

    for extension in extensiones:
        for carpeta in Carpetas:
            for archivo in os.listdir(carpeta):
                if archivo.endswith(extension):
                    print(f'El archivo {archivo} sera eliminado')
                    Archivos.append(os.path.join(carpeta, archivo))
    return Archivos

main()