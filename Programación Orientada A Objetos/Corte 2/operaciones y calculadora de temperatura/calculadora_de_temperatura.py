def menu():
    opc=("1.convertir °F a °C","2. convertir °C a °F","3. convertir °K a °F",
         "4.convertir °F a °K","5. convertir °C a °K","6. convertir °K a °C", "7. SALIR")
    print("¿que desea hacer?")
    print(opc)
def convert1():
    Temp= float(input("ingrese la temperatura en °F: "))
    Resul=5/9*(Temp-32)
    print(" la temperatura en celsius es: ", Resul)
def convert2():
    temp= float(input("ingrese temperatura en °C: "))
    resul= (9/5*temp)+32
    print(" la temperatura en Fahrenheit es: ", resul)
def convert3():
    temp= float(input("ingrese temperatura en °F: "))
    resul=(9/5* temp-273)+32
    print("la temperatura en Fahrenheit es: ", resul)
def convert4():
    temp= float(input("ingrese temperatura en °F: "))
    resul=(5/9*temp-32)+273
    print("la temperatura en kelvin es: ", resul)
def convert5():
    temp= float(input("ingrese temperatura en °C: "))
    resul= temp+273
    print(" la temperatura en kelvin es: ", resul)
def convert6():
    temp= float(input("ingrese temperatura en °K: "))
    resul= temp-273
    print("la temperatura en celsius es: ", resul)


while "true":
    menu()
    OPC= int(input("ingrese opcion"))
    if OPC== 1:
        convert1()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
            print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break 
    if OPC== 2:
        convert2()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
             print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break
    if OPC==3:
        convert3()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
             print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break
    if OPC==4:
        convert4()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
             print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break
    if OPC==5:
        convert5()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
             print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break
    if OPC==6:
        convert6()
        opc= str(input("¿desea hacer algo mas?"))
        if opc== "si":
             print("aqui tienes el menu")
        else:
            print("hasta pronto")
            break
    if OPC== 7:
        print("Gracias hasta pronto")
        break   