usuariosR={"luis":"4050",
           "carlos":"8090"
    } 
def menu():
    OPC=("1. iniciar sesion ", "2. registrar nuevo usuario ", "3. salir")
    print(OPC)
def inicioS():
    while True:
        usu = input("Ingrese usuario: ")
        contra = input("Ingrese contraseña: ")
        if usu in usuariosR:
            if usuariosR[usu] == contra:
                print(f"Bienvenido, {usu}")
                return
            else:
                print("Usuario y/o contraseña incorrectos")
        else:
            print("Usuario no encontrado")
        opc2 = input("¿Desea intentar de nuevo? (Si/No): ")
        if opc2.lower() != "si":
            return

def registroU():
    while True:
        usu1 = input("Ingrese usuario a registrar: ")
        if usu1 in usuariosR:
            print("Este usuario ya existe. Use otro nombre de usuario.")
        else:
            contra1 = input("Ingrese contraseña a registrar: ")
            usuariosR[usu1] = contra1
            print("Usuario registrado correctamente.")
            return

def menu2():
    while True:
        print("Bienvenido, ¿Qué desea hacer?")
        menu()
        opc = input("Introduzca opción: ")
        if opc == "1":
            inicioS()
        elif opc == "2":
            registroU()
        elif opc == "3":
            print("Gracias, hasta pronto.")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu2()
  