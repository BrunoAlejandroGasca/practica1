print("Hola Mundo")




#Ejercicio  1
numero = int(input("Número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

#Ejercicio  2
numero = float(input("Número: "))
if numero >= 0:
    print("Positivo")
else:
    print("Negativo")

#Ejercicio  3
edad = int(input("Edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#Ejercicio  4
calificacion = float(input("Calificación: "))
if calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#Ejercicio  5
calificacion = float(input("Calificación: "))

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")

#Ejercicio  6
temperatura = float(input("Temperatura en °C: "))

if temperatura < 0:
    print("Sólido")
elif temperatura <= 100:
    print("Líquido")
else:
    print("Vapor")

