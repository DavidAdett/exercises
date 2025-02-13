class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"El coche {self.marca} {self.modelo} ha frenado a {self.velocidad} km/h")

    def mostrarVelocidad(self):
        print(f"La velocidad del coche {self.marca} {self.modelo} es de {self.velocidad} km/h")

# Crear un objeto de la clase Coche
#coche1 = Coche("Ford", "Fiesta")
#coche1.acelerar(50)
#coche1.mostrarVelocidad()
#coche1.frenar(20)
#coche1.mostrarVelocidad()

# Crear una lista de 3 coches
coches = [
    Coche("Ford", "Fiesta"),
    Coche("Renault", "Clio"),
    Coche("Volkswagen", "Golf"),
]

# Mostrar la marca y modelo de cada coche
for coche in coches:
    print(f"Marca: {coche.marca}, Modelo: {coche.modelo}")

# Aceleramos todos los coches a 100 km/h"
for coche in coches:
    coche.acelerar(100)

# Frenamos los coches a 40 km/h
for coche in coches:
    coche.frenar(60)

# Creamos otra clase, para practicar la herencia que se llame CocheElectrico que herede de la clase Coche y tenga un atributo bateria y un metodo cargarBateria
class CocheElectrico(Coche):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria
    
    # metodo para mostrar la carga de bateria
    def mostrarBateria(self):
        print(f"La batería del coche {self.marca} {self.modelo} es de {self.bateria}%")
    
    def cargarBateria(self):
        self.bateria = 100
        print(f"La batería del coche {self.marca} {self.modelo} ha sido cargada al 100%")

# Crear un objeto de la clase CocheElectrico
cocheElectrico1 = CocheElectrico("Tesla", "Model S", 0)
cocheElectrico1.mostrarBateria()
cocheElectrico1.cargarBateria()
cocheElectrico1.acelerar(50)
cocheElectrico1.mostrarVelocidad()