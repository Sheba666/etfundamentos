import random
import csv

superheroes = []

def guardar_csv():
    archivocsv=open('Lista.csv', 'w')
    for superheroe in superheroes:
        archivocsv.write(str(superheroes))
    archivocsv.close

def agregar_superheroe():
    nombre=input("Ingrese el nombre del super heroe: ")
    while len(nombre) <= 3:
        print("Nombre menor o igual a 3 digitos no permitido")
        nombre=input("Ingrese el nombre del super heroe: ")

    año=int(input("Ingrese el año de aparicion: "))
    while año <= 1930:
        print("El año no puede sér menor o igual a 1930")
        año=int(input("Ingrese el año de aparicion: "))
        
    superheroes.append({'Nombre: ':nombre,'Año: ':año})
    print(f"Se ha añadido {nombre} a los super heroes")
    guardar_csv()


def asignar_popularidad():
    ubicacion=int(input("Ingrese la ubicacion del super heroe "))
    if 0 <= ubicacion < len(superheroes):
        popularidad= random.randint(1,10)
        superheroes[ubicacion]['Popularidad'] = popularidad
        print(f"Se ha establecido en {popularidad} la popularidad del heroe {superheroes[ubicacion]['Nombre: ']}")
    else:
        print("Ubicacion no valida")
    guardar_csv()





while True:
    print("\n--- Menú ---")
    print("1. Agregar un superhéroe")
    print("2. Asignar popularidad")
    opcion=int(input("Ingrese una opcion: "))

    if opcion == 1:
        agregar_superheroe()
        print(superheroes)
    elif opcion == 2:
        asignar_popularidad()
else:
    print("opcion no valida")