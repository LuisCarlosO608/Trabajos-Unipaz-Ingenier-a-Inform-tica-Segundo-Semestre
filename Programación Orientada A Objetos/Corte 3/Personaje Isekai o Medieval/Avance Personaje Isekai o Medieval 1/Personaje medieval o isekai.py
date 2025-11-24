class personaje:
    def __init__(self,rol,nombre,fuerza,resistencia,salud,agilidad,potencial_oculto):
        self.rol=rol
        self.nombre=nombre
        self.fuerza=fuerza
        self.resistencia=resistencia
        self.salud=salud
        self.agilidad=agilidad
        self.potencial_oculto=potencial_oculto
    
    def descripcion(self):
        print(f" el personaje {self.rol}, llamado {self.nombre} tiene una fuerza {self.fuerza} al inicio pero con potencial de crecimiento")
        print(f"tiene una resistencia {self.resistencia} ya que lleva mas de 8 años siendo {self.rol}")
        print(f"su salud es {self.salud} debido a que muchos de sus dueños lo han dejado sin comer ")
        print(f"tiene una agilidad {self.agilidad} ya que ha logrado escapar en varias ocasiones")
        print(f"su potencial oculto es {self.potencial_oculto}. No es necesario explicaciones para eso.")
    
    def Trabajar(self):
        print("´realiza la tarea encargada´")
    
    def obedecer(self):
        print("si señor hare lo que tu pidas")
   
    def huir(self):
        print(f"piensa en huir pero se rinde, razones: rol actual {self.rol}, salud {self.salud}")





yo_personaje=personaje("Esclavo","Luis","baja","media","debil","alta","Resistencia al dolor")

yo_personaje.descripcion()

yo_personaje.obedecer()
yo_personaje.Trabajar()
yo_personaje.huir()  



        