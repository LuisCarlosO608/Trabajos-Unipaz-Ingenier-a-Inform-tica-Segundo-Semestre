class Vehiculo:
    def __init__(self,tipo_vehiculo,modelo,marca,año):
        self.tipo_vehiculo=tipo_vehiculo
        self.modelo=modelo
        self.marca=marca
        self.año=año
        self.velocidad_actual=0
    def acelerar(self,cantidad):
        self.velocidad_actual+=cantidad
        print(f"{self.marca} modelo:{self.modelo} aceleró {self.velocidad_actual} km/h")
    def frenar(self,cantidad):
        self.velocidad_actual-=cantidad
        if self.velocidad_actual<0:
            self.velocidad_actual=0
        print(f"{self.marca} modelo: {self.modelo} frenó y su velocidad es de {self.velocidad_actual} km/h")
    def mostrar_info(self):
        return print(f" vehiculo de marca:{self.marca}, modelo:{self.modelo} y año:{self.año} | velocidad:{self.velocidad_actual} km/h")
        
class auto(Vehiculo):
    def __init__(self,tipo_vehiculo,modelo,marca,año,numero_puertas):
        super().__init__(tipo_vehiculo,modelo,marca,año)
        self.numero_puertas=numero_puertas
    def mostrar_info(self):
        informacion_base=super().mostrar_info()
        return print(f"[carro] {informacion_base} | Puertas: {self.numero_puertas}")
    
class moto(Vehiculo):
    def __init__(self, tipo_vehiculo, modelo, marca, año,cilindraje):
        super().__init__(tipo_vehiculo, modelo, marca, año)
        self.cilindraje=cilindraje
    def mostrar_info(self):
        informacion_base=super().mostrar_info()
        return print(f"[moto] {informacion_base} | cilindraje: {self.cilindraje}")

class bicicleta(Vehiculo):
    def __init__(self, tipo_vehiculo, modelo, marca,año,numero_velocidades):
        super().__init__(tipo_vehiculo, modelo, marca,año)
        self.numero_velocidades=numero_velocidades
    def mostrar_info(self):
        informacion_base=super().mostrar_info()
        return print(f"[bici] {informacion_base} | tipo de uso: {self.numero_velocidades}")


carro1=auto("Sedán","Corolla","Toyota","2022","4 puertas")
carro2=auto("SUV","Explorer","Ford","2021","5 puertas")

moto1=moto("Naked / Deportiva","MT-07","Yamaha","2023","689 cc")
moto2=moto("Enduro / Dual Sport","CRF300L","Honda","2024","286 cc")

bici1=bicicleta("Montaña(MTB)","Rockhopper Elite","Specialized","2024","1x12")
bici2=bicicleta("Urbana/Fitness","Quick 4","Cannondale","2023","2x9")

print("Simulación")

carro1.acelerar(60)
carro1.frenar(40)
carro2.acelerar(90)

moto1.acelerar(50)
moto2.acelerar(75)
moto2.frenar(45)

bici1.acelerar(25)
bici2.acelerar(30)
bici2.frenar(15)

vehiculos_en_ciudad=[carro1,carro2,moto1,moto2,bici1,bici2]

print("reporte de los vehiculos")
for i in vehiculos_en_ciudad:
    i.mostrar_info()
    


        