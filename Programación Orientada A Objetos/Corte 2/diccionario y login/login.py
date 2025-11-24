
def menu():
    print("bienvenido,¿que desea hacer?")
    opc= ("1. iniciar sesion","2.salir","3.usuarios registrados")
    print(opc)
    
usuariosR=["luis","carlos"]

usuarios={"luis":"2040","carlos":"3040"}

while "true":
    menu()
    opc=int(input(" ingrese opcion:  "))
    if opc == 1:
       usu= str(input("ingrese usuario:  "))
       contra= str(input("ingrese contraseña:  "))  
       if usu in usuarios:
                if usuarios[usu]==contra:
                  print("bienvenido", usu)
                  break
                else:
                  print("contraseña incorrecta intentalo nuevamente")
                  
       else:
             print("usuario no encontrado")
             print("intente de nuevo")
   
    if opc== 2:
            print("hasta pronto")
            break
            
    if opc== 3:
        print("estos son los usuarios registrados")
        print(usuariosR)
        print("¿desea hacer algo mas? ")
        op=str(input("si/no"))
        if op=="si":
                   print("este es el menu")
        else:
                   print("hasta pronto")
                   break