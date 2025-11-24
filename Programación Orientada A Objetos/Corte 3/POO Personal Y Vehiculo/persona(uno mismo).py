class persona:
    def __init__(self,nombre,apellido,genero,altura,ocupacion):
        self.nombre=nombre
        self.apellido=apellido
        self.genero=genero
        self.altura=altura
        self.ocupacion=ocupacion
    def explicar_uno_mismo(self):
        print(f"hola soy: {self.nombre}, y mi apellido es: {self.apellido}, mi genero es: {self.genero}")
        print(f"mi altura es: {self.altura} y mi ocupacion es: {self.ocupacion}")
    def funciones_que_yo_hago(self):
        print(f"como mi ocupacion es ser {self.ocupacion}, debo crear programas que solucionen problemas")
        print("tambien debo mejorar mis tecnicas de programación.")
        
        

Yo=persona("luis carlos","ortega medina","masculino","1.80","ingeniero informatico")

Yo.explicar_uno_mismo()
Yo.funciones_que_yo_hago()
        