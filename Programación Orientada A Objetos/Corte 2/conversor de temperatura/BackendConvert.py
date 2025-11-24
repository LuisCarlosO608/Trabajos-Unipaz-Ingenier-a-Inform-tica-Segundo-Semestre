# se separan las conversiones en funciones para que asi sea mas facil diferenciar los datos ingresados
# y tambien identificar cada proceso de conversión


#convert1 es la conversion de farenheit a celsius
def convert1(dato_F1,etq_Result1):
    #se crea una variable que guarde el dato
    temp=float(dato_F1.get())
    #se hace el proceso de division y multiplicación
    resul=5/9*(temp-32)
    #en ocasiones python muestra muchos decimales esto sirve para redondear
    resulR=round(resul,1)
    #se muestra el resultado en la etiqueta correspondiente
    etq_Result1.configure(text=str(resulR)+"°C")

#en lo que escribí en el convert1 se aplica lo mismo en todos los converts  
def convert2(dato_C1,etq_Result2):
    temp=float(dato_C1.get())
    resul=(9/5*temp)+32
    resulR=round(resul,1)
    etq_Result2.configure(text=str(resulR)+"°F")

def convert3(dato_K1,etq_Result3):
    temp=float(dato_K1.get())
    resul=9/5*(temp-273)+32
    resulR=round(resul,1)
    etq_Result3.configure(text=str(resulR)+"°F")

def convert4(dato_F2,etq_Result4):
    temp=float(dato_F2.get())
    resul=5/9*(temp-32)+273
    resulR=round(resul,1)
    etq_Result4.configure(text=str(resulR)+"°K")

def convert5(dato_K2,etq_Result5):
    temp=float(dato_K2.get())
    resul=temp-273
    resulR=round(resul,1)
    etq_Result5.configure(text=str(resulR)+"°C")

def convert6(dato_C2,etq_Result6):
    temp=float(dato_C2.get())
    resul=temp+273
    resulR=round(resul,1)
    etq_Result6.configure(text=str(resulR)+"°K")
