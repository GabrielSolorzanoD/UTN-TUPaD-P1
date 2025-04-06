
#---Actividad 1---

edad = int(input("Ingrese la edad del usuario:"))

if edad < 18:
    print("El ususario es menor de edad")
elif edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("el valor ingresado no es válido")

#---Actividad 2---

nota = int(input("Ingrese la nota:"))

if nota >= 6:
    print("Aprobado")
elif nota < 6:
    print ("Desaprobado") 
    

#---Actividad 3---
numero = int(input("Ingrese un número"))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")
     


#---Actividad 4---
edad = int(input("Ingrese una edad:"))
if edad < 12 :
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >=18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

  
#---Actividad 5---
contraseña = input("Ingrese una contraseñas de entre 8 y 14 caracteres:")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    

#---Actividad 6---
from statistics import mode, median, mean 

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

media =  mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")


#---Actividad 7---

frase = input("Ingrese una frase o palabra:")
#frase = frase.upper()
vocales = "aeiou"
l = frase[-1]

if l.lower() in vocales :
    print( f"{frase}!")
else:
    print(frase)


#---Actividad 8---
nombre = input("Ingrese su nombre:")
numero = int(input("Ingrese un número del 1 al 3:"))

if numero == 1:
    nombre = nombre.upper()
    print(nombre)
elif numero == 2:
    nombre = nombre.lower()
    print(nombre)
elif numero == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print("Lea la instrucciones con cuidado e intentelo nuevamente")

#---Actividad 9---
mag = int(input("Ingrese la magnitud del terremoto:"))

if mag < 3:
    print("Muy leve")
elif mag == 3 :
    print("leve")
elif mag == 4 :
    print("Moderado")
elif mag == 5 :
    print("Fuerte")
elif mag == 6 :
    print("Muy Fuerte")
elif mag >= 7 :
    print("Extremo")


#---Actividad 10---

def obtener_estacion(hemisferio, mes, dia):
    fecha = (mes, dia)

    estaciones_norte = {
        "invierno": [((12, 21), (3, 20))],
        "primavera": [((3, 21), (6, 20))],
        "verano": [((6, 21), (9, 20))],
        "otoño": [((9, 21), (12, 20))]
    }

    estaciones_sur = {
        "verano": estaciones_norte["invierno"],
        "otoño": estaciones_norte["primavera"],
        "invierno": estaciones_norte["verano"],
        "primavera": estaciones_norte["otoño"]
    }

    if hemisferio.upper() == 'N':
        estaciones = estaciones_norte
    elif hemisferio.upper() == 'S':
        estaciones = estaciones_sur
    else:
        return "Hemisferio no válido."


    for estacion, rangos in estaciones.items():
        for inicio, fin in rangos:
            if inicio <= fin:
                if inicio <= fecha <= fin:
                    return estacion
            else:
                if fecha >= inicio or fecha <= fin:
                    return estacion

    return "Fecha no válida."

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

estacion = obtener_estacion(hemisferio, mes, dia)
print(f"La estación del año es: {estacion.capitalize()}")