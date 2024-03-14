"""
Esta funcion compara dos numeros y devuelve el mayor.

Parametros:
num1 (int): El primer numero a comparar.
num2 (int): El segundo numero a comparar.

Return:
int: El numero mayor de los dos.
"""


def numero_mayor(num1, num2):
    if num1 > num2:
        return num1
    return num2


num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

mayor = numero_mayor(num1, num2)
print(f"El numero mayor es: {mayor}")
