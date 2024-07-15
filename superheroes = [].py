import random
import csv

superheroes = []

def agregar_superheroes():
    nombre=input("Ingrese el nombre del super heroe: ")
    while len(nombre) <= 3:
        print("El nombre debe contener más de 3 caracteres")
        nombre=input("Ingrese el nombre del super heroe: ")

    año=int(input("Ingrese el año de aparicion: "))
    while año <= 1930:
        print("El año de aparicion debe ser superior a 1930")
        año=int(input("Ingrese el año de aparicion: "))

    superheroes.append({"Nombre: ":nombre,"Año: ":año,"Popularidad: ": None})
    print(f"El super hero {nombre} se ha añadido a la lista")

def asignar_popularidad():
    clasificacion_de_superheroe = int(input("Ingrese la clasificacion actual del heroe"))
    if 0 <= clasificacion_de_superheroe < len(superheroes):
        popularidad= random.randint(1,10)
        superheroes[clasificacion_de_superheroe]["Popularidad"] = popularidad
        print(f"Popularidad de {superheroes[clasificacion_de_superheroe]['Nombre: ']} asignada: {popularidad}")



def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar un superhéroe")
        print("2. Asignar popularidad")
        print("3. Mostrar superhéroes más populares")
        print("4. Buscar popularidad por nombre")
        print("5. Guardar datos en un archivo CSV")
        print("6. Salir")

        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_superheroes()
        elif opcion == 2:
            asignar_popularidad()
menu()