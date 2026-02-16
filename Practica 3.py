# Clase Coche
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0  # Velocidad inicial

    def acelerar(self, velocidad):
        if velocidad > 0:
            self.velocidad += velocidad
            print(f"El coche aceleró {velocidad} km/h.")
        else:
            print("La velocidad debe ser positiva.")

    def frenar(self, velocidad):
        if velocidad > 0:
            self.velocidad -= velocidad
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El coche frenó {velocidad} km/h.")
        else:
            print("La velocidad debe ser positiva.")

    def mostrar_info(self):
        print("Información del coche:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad actual: {self.velocidad} km/h")


# Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0  # Saldo inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron ${cantidad}.")
        else:
            print("La cantidad debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se retiraron ${cantidad}.")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad debe ser positiva.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo}")


# Clase Rectangulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        print("Información del rectángulo:")
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")


