#Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.")

# Leer de un archivo
with open("D:/blockchain/python/tutorial/ejercicios python/contract.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)