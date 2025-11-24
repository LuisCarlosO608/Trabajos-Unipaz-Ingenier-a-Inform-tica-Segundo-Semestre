import time

class jugador:
    def __init__(self,nombre,dorsal,posicion,equipo):
        self.nombre=nombre
        self.dorsal=dorsal
        self.posicion=posicion
        self.equipo=equipo
        
        self.goles=0
        
        self.estadistica_especifica=0
    
    def marcar_goles(self):
        self.goles +=1
        print(f"\n¡GOOOOOL de {self.nombre} #{self.dorsal} para {self.equipo}")
        time.sleep(1)
    
    def registrar_estadistica(self,cantidad=1):
        self.estadistica_especifica+=cantidad
        print(f"{self.nombre} suma {cantidad} {self.obtener_nombre_estadistica()}")        
    
    def obtener_nombre_estadistica(self):
        if self.posicion=="arquero":
            return "atajadas"
        elif self.posicion=="lateral":
            return "bloqueos"
        elif self.posicion=="armador":
            return "pases"
        elif self.posicion=="delantero":
            return "tiros al arco"
    
    def resumen_partido(self):
        print(f"jugador:{self.nombre} #{self.dorsal}-{self.equipo}")
        print(f"goles: {self.goles}")
        
        nombre_estadistica=self.obtener_nombre_estadistica()
        print(f"{nombre_estadistica}:{self.estadistica_especifica}")
    


def seleccionar_jugador(jugadores_totales):
    print(f"\n ¿que jugador realizo la accion?")
    print("-"*30)
    for i, jugador in enumerate(jugadores_totales):
        print(f"[{i+1}]{jugador.nombre} #{jugador.dorsal}-{jugador.equipo}")
    print("-"*30)
    
    while True:
        try:
            opcion=int(input("seleccione el nunero del jugador:"))
            if 1<=opcion<=len(jugadores_totales):
                return jugadores_totales[opcion-1]
            else:
                print("numero fuera de rango")
        except ValueError:
            print("entrada invalida intente de nuevo")

def mostrar_resumen_final(jugadores_totales):
    print("\n"+"="*35)
    print("Resumen final del partido")
    print("="*35)
    
    total_golesA=0
    total_golesB=0
    
    for jugador in jugadores_totales:
        jugador.resumen_partido()
        print("-"*25)
        
        if jugador.equipo=="Los Fenix":
            total_golesA+=jugador.goles
        else:
            total_golesB+=jugador.goles
    
    print("\n===Marcador Final===")
    print(f"los fenix: {total_golesA}")
    print(f"los titanes: {total_golesB}")

def simular_partido(jugadores_totales):
    print("Comienza El Partido")
    
    while True:
        print("\n-Menu Del Partido-")
        print("1. registrar gol")
        print("2. registrar estadistica especifica(atajada,bloqueo,pase,tiro)")
        print("3. terminar partido(mostrar resumen)")
        
        opcion=input("selecciones opcion:(1,2 0 3): ")
        
        if opcion=="1":
            jugador_seleccionado=seleccionar_jugador(jugadores_totales)
            jugador_seleccionado.marcar_goles()
        
        elif opcion=="2":
            jugador_seleccionado=seleccionar_jugador(jugadores_totales)
            
            try:
                estadistica_nombre=jugador_seleccionado.obtener_nombre_estadistica()
                cantidad=int(input(f"¿cuantos {estadistica_nombre} registro {jugador_seleccionado.nombre}?"))
                jugador_seleccionado.registrar_estadistica(cantidad)
            except ValueError:
                print("cantidad invalida.registrando 1 por defecto")
                jugador_seleccionado.registrar_estadistica(1)
        elif opcion=="3":
            print("el usuario ha acabado el partido")
            break
        else:
            print("opcion invalida elija 1,2 o 3")
    mostrar_resumen_final(jugadores_totales)


if __name__ == "__main__":
    
    a1 = jugador("Pedro", 1, "arquero", "Los Fénix")
    a2 = jugador("Luis", 4, "lateral", "Los Fénix")
    a3 = jugador("Juan", 5, "lateral", "Los Fénix")
    a4 = jugador("Memo", 10, "armador", "Los Fénix")
    a5 = jugador("Cristiano Ronaldo", 9, "delantero", "Los Fénix")
    
    b1 = jugador("David", 12, "arquero", "Los Titanes")
    b2 = jugador("Carlos", 3, "lateral", "Los Titanes")
    b3 = jugador("Raul", 2, "lateral", "Los Titanes")
    b4 = jugador("Leonel Messi", 8, "armador", "Los Titanes")
    b5 = jugador("Pipo", 7, "delantero", "Los Titanes")

    jugadores_totales = [a1, a2, a3, a4, a5, b1, b2, b3, b4, b5]

    simular_partido(jugadores_totales)
    
    

        
        
        
        






