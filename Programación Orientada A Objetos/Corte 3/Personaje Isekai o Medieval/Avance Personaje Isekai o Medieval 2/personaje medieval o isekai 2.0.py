class personaje:
    def __init__(self,rol,nombre,fuerza,resistencia,salud,agilidad,potencial_oculto,tipo_personaje,vidas,habilidades,oficio):
        self.rol=rol
        self.nombre=nombre
        self.fuerza=fuerza
        self.resistencia=resistencia
        self.salud=salud
        self.agilidad=agilidad
        self.potencial_oculto=potencial_oculto
        self.tipo_personaje=tipo_personaje
        self.vidas=vidas
        self.habilidades=habilidades
        self.oficio=oficio  
    def descripcion(self):
        print(f" el personaje {self.rol}, llamado {self.nombre} es un {self.tipo_personaje} y tiene una fuerza  {self.fuerza} pts al inicio pero con potencial de crecimiento" )
        print(f"tiene una resistencia {self.resistencia} pts ya que lleva mas de 8 años siendo {self.rol}")
        print(f"su salud es {self.salud} pts debido a que muchos de sus dueños lo han dejado sin comer ")
        print(f"tiene una agilidad {self.agilidad} pts ya que ha logrado escapar en varias ocasiones")
        print(f"su potencial oculto es {self.potencial_oculto}. No es necesario explicaciones para eso.")
    
    def Trabajar(self):
        print("´realiza la tarea encargada´")
    
    def obedecer(self):
        print("´si señor hare lo que tu pidas´")
   
    def huir(self):
        print(f"´piensa en huir pero se rinde´, razones: rol actual {self.rol}, salud {self.salud} pts")

class personaje_arma:
    def __init__(self,equipo_especial,poder_equipo,tipo_arma,daño,nivel_arma,):
        self.equipo_especial=equipo_especial
        self.poder_equipo=poder_equipo
        self.tipo_arma=tipo_arma
        self.daño=daño
        self.nivel_arma=nivel_arma
    
    def Descripcion_arma(self):
        print(f"{yo_personaje.nombre} tiene un arma {yo_personaje_arma.equipo_especial} de tipo {yo_personaje_arma.tipo_arma}")
        print(f"esta arma cuenta con un daño de {yo_personaje_arma.daño} pts")
        print(f"el poder del quipo es de {yo_personaje_arma.poder_equipo} pts")
        print(f"el nivel del arma es de clase {yo_personaje_arma.nivel_arma}")
    
    def defenderse(self):
        print(f"{yo_personaje.nombre} usa el arma {yo_personaje_arma.equipo_especial} para intentar bloquear ataque")    
    def atacar(self):
        print(f"{yo_personaje.nombre} ataca usando el arma {yo_personaje_arma.equipo_especial}")



yo_personaje=personaje(
    "Esclavo",
    "Luis",
    250,
    800,
    90,
    1200,
    "Resistencia al dolor",
    "Semi humano: Gato Negro",
    3,
    "Robo Silencioso",
    "Boticario"
    )

yo_personaje_arma=personaje_arma(
    "Daga",
    550,
    "Corta",
    180,
    "Ordinario"
)

yo_personaje.descripcion()

yo_personaje.obedecer()
yo_personaje.Trabajar()
yo_personaje.huir()  

yo_personaje_arma.Descripcion_arma()
yo_personaje_arma.defenderse()
yo_personaje_arma.atacar()
    
