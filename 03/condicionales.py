""""
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

   """
#---Actividad 5---
contraseña = input("Ingrese una contraseñas de entre 8 y 14 caracteres:")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#---Actividad 6---
#---Actividad 7---
#---Actividad 8---
#---Actividad 9---
#---Actividad 10---