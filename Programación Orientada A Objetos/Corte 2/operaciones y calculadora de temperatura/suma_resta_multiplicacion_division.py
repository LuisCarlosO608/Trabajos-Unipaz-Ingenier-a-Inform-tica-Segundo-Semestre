# aqui creo una funcion para sumar
def sumar():
    num1=int(input(" ingrese numero 1: "))
    num2= int(input(" ingrese numero 2: "))
    suma= num1 + num2
    print(suma)
def restar():
    num1= int(input(" ingrese numero 1: "))
    num2= int(input(" ingrese numero 2: "))    
    resta= num1 - num2
    print(resta)
def multiplicar():
    num1=int(input(" ingrese numero 1: "))
    num2= int(input(" ingrese numero 2: "))
    multiplicar= num1 * num2
    print(multiplicar)
def dividir():
    num1= int(input(" ingrese numero 1: "))
    num2= int(input(" ingrese numero 2: "))
    dividir= num1//num2
    print(dividir)

print("1.sumar")
print("2.restar")
print("3. multiplicar")
print("4. dividir")
opc= int(input(" ingrese opcion: "))
if opc== 1:
    sumar()
if opc== 2:
        restar()
if opc== 3:
            multiplicar()
if opc== 4:
      dividir()
            