"""
# Inicio
#   Escribir "ingrese un año: "
#   Leer año

#   si (año divisible por 4 y no divisible por 100) o año divisible por 400, entonces si es año bisiesto
#       Escribir "El año," año "es bisiesto."
#   sino
#       Escribir "El año", año, "no es bisiesto."
#   fin si
# fin
"""

# pregunta por el año
year = int(input("Por favor, ingrese el año: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This year " + str(year) + " is  Bisiesto")
else:
    print("This year, " + str(year) + " is not bisiesto")
