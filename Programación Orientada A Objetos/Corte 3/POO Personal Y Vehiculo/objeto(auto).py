class Carro:
    def __init__(self,marca,color,motor,carroceria,sistema_transmision,sistema_frenos,):
        self.marca=marca
        self.color=color
        self.motor=motor
        self.carroceria=carroceria
        self.sistema_transmision=sistema_transmision
        self.sistema_frenos=sistema_frenos
    def funciones(self,velocidad_maxima,sistema_seguridad):
        print(f"es un medio de transporte tiene una velocidad maxima de {velocidad_maxima} y un sistema de seguridad {sistema_seguridad}")


auto=Carro("kia","rojo","gasolina"," hatchback","manual","tambor")



print(f"el modelo del auto es: {auto.marca}")
print(f"el color del auto es: {auto.color}")
print(f"el motor del auto es: {auto.motor}")
print(f"la carroceria del auto es: {auto.carroceria}")
print(f"el sistema de transmision del auto es: {auto.sistema_transmision}")
print(f"el sistema de frenos es: {auto.sistema_frenos}")

auto.funciones("80 km/h","pasiva")

