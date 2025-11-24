class empleado:
    def __init__(self,nombre,rol,identificación):
        self.nombre=nombre
        self.identificación=identificación
        self.rol=rol

class gerente(empleado):
    def __init__(self,nombre,rol,identificación,salario):
        super().__init__(nombre,rol,identificación)
        self.identificación=identificación
        self.rol=rol
        self.nombre=nombre
        self.salario=salario

class empleado_ordinario(empleado):
    def __init__(self, nombre, rol,identificación,salario,horas_trabajo):
        super().__init__(nombre, rol, identificación)
        self.horas_trabajo=horas_trabajo
        self.salario=salario
    
gerente1=gerente("jose","gerente","102040","35 SMVL")
empleado_or=empleado_ordinario("Freddy","empleado ordinario","304050","25 SMVL","50 horas semanales")

print(f"el {gerente1.rol} de nombre {gerente1.nombre} identifciado con ID {gerente1.identificación} gana $ {gerente1.salario}")

print(f"el {empleado_or.rol} de nombre {empleado_or.nombre} identificado con ID {empleado_or.identificación} gana un salario de $ {empleado_or.salario} y tiene {empleado_or.horas_trabajo}")