import random
import csv

superheroes = []



def agregar_superheroe():
    nombre = input("Ingrese el nombre del super heroe: ")
    while len(nombre) <= 3:
        print("El nombre debe tener más de 3 caracteres")
        nombre = input("Ingrese el nombre del super heroe")
    
    año= int(input("Ingresa el año de aparicion: "))
    while año <= 1930:
        print("El super heroe debe ser despues de los años 30")
        año = int(input("Ingresa el año de aparicion: "))
    superheroes.append({"Nombre: ",nombre,"Año:",año, "popularidad: ", None})
    print(f"el super heroe {nombre} agregado a la coleccion")



def menu():
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    opcion = int(input("Por favor ingrese una opcion: "))
    if opcion == 1:
        agregar_superheroe()
    else:
        print("Opcion incorrecta")
    
menu()