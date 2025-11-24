class Ejercito:
    def __init__(self,rango,ID,nombre,peloton):
        self.nombre=nombre
        self.rango=rango
        self.ID=ID
        self.peloton=peloton

class soldado_Razo(Ejercito):
    def __init__(self, rango, ID, nombre, peloton,alias,tiempo_servicio):
        super().__init__(rango, ID, nombre, peloton)
        self.alias=alias
        self.tiempo_servicio=tiempo_servicio

class cabo(Ejercito):
    def __init__(self, rango, ID, nombre, peloton,tiempo_serivicio):
        super().__init__(rango, ID, nombre, peloton)
        self.tiempo_servicio=tiempo_serivicio

class sargento(Ejercito):
    def __init__(self, rango, ID, nombre, peloton):
        super().__init__(rango, ID, nombre, peloton)
        self.peloton=peloton
        
class teniente(Ejercito):
    def __init__(self, rango, ID, nombre, peloton,numero_oficiales):
        super().__init__(rango, ID, nombre, peloton)
        self.numero_oficiales=numero_oficiales

class general(Ejercito):
    def __init__(self, rango, ID, nombre, peloton,batallon):
        super().__init__(rango, ID, nombre, peloton)
        self.batallon=batallon


soldado_razo1=soldado_Razo("Razo","1020","daniel","alfa","postobon","3 años")

cabo1=cabo("cabo","3080","Fernando","omega","6 años")

sargento1=sargento("sargento","8090","sergio","2 pelotones")

teniente1=teniente("teniente","7096","hector","","8 oficiales")

general1=general("general","5088","hector","","artilleria de campaña No. 6")

print(f" el alias del soldado {soldado_razo1.nombre} es {soldado_razo1.alias} y su tiempo de servicio es {soldado_razo1.tiempo_servicio}")

print(f"el soldado {cabo1.nombre} cuyo rango es {cabo1.rango} y tiene un serivicio prestado de {cabo1.tiempo_servicio}")

print(f"el {sargento1.rango} de nombre {sargento1.nombre} con ID {sargento1.ID} maneja {sargento1.peloton}")

print(f"el {teniente1.rango} de nombre {teniente1.nombre} y ID {teniente1.ID} tiene {teniente1.numero_oficiales} a su mando")

print(f"el {general1.rango} maneja un batallon de {general1.batallon}")