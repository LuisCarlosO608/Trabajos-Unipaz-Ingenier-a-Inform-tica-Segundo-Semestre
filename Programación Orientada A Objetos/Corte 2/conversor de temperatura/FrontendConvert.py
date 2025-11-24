# se importa el Tkinter y se nombra Tk
import tkinter as Tk
# del backend del conversor se importa las funciones 
from BackendConvert import convert1,convert2,convert3,convert4,convert5,convert6

# se crea la ventana del frontend
ventana=Tk.Tk()
# le añadimos titulo a esa ventana creada
ventana.title("Conversor de temperatura")
# le damos un ancho y alto a la ventana para que se vea mas estetico
ventana.geometry("600x480")
# le añadimos un fondo que no desgaste tanto la vista
ventana.configure(bg="lightblue")

# se crea una etiqueta que de la bienvenida
Bienvenida=Tk.Label(ventana,text="Bienvenido,¿Qué desea hacer?")
Bienvenida.grid(row=1,column=2,rowspan=1,columnspan=1,pady=5)

# se crean etiquetas para separar e identificar cada proceso de conversión
etq_F_C = Tk.Label(ventana,text="Farenheit a Celsius")
etq_F_C.grid(row=2,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

etq_C_F = Tk.Label(ventana,text="Celsius a Farenheit")
etq_C_F.grid(row=3,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

etq_K_F = Tk.Label(ventana,text="Kelvin a Farenheit")
etq_K_F.grid(row=4,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

etq_F_K=Tk.Label(ventana,text="Farenheit a Kelvin")
etq_F_K.grid(row=5,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

etq_K_C=Tk.Label(ventana,text="Kelvin a Celsius")
etq_K_C.grid(row=6,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

etq_C_K=Tk.Label(ventana,text="Celsius a Kelvin")
etq_C_K.grid(row=7,column=2,rowspan=1,columnspan=1,pady=5,sticky=Tk.W)

# se crean otras etiquetas que indiquen en donde ingresar los datos en cada proceso de conversion
flecha_F_C=Tk.Label(ventana,text="ingrese dato -->")
flecha_F_C.grid(row=2,column=3,rowspan=1,columnspan=1,pady=5)

FlechaC_F=Tk.Label(ventana,text="ingrese dato -->")
FlechaC_F.grid(row=3,column=3,rowspan=1,columnspan=1,pady=5)

Flecha_K_F=Tk.Label(ventana,text="ingrese dato -->")
Flecha_K_F.grid(row=4,column=3,rowspan=1,columnspan=1,pady=5)

Flecha_F_K=Tk.Label(ventana,text="ingrese dato -->")
Flecha_F_K.grid(row=5,column=3,rowspan=1,columnspan=1,pady=5)

Flecha_K_C=Tk.Label(ventana,text="ingrese dato-->")
Flecha_K_C.grid(row=6,column=3,rowspan=1,columnspan=1,pady=5)

Flecha_C_K=Tk.Label(ventana,text="ingrese dato -->")
Flecha_C_K.grid(row=7,column=3,rowspan=1,columnspan=1,pady=5)

# se crean cajas de texto para asi poder ingresar el dato a transformar
dato_F1=Tk.Entry(ventana,width=20)
dato_F1.grid(row=2,column=4,rowspan=1,columnspan=1,pady=10)

dato_C1=Tk.Entry(ventana,width=20)
dato_C1.grid(row=3,column=4,rowspan=1,columnspan=1,pady=10)

dato_K1=Tk.Entry(ventana,width=20)
dato_K1.grid(row=4,column=4,rowspan=1,columnspan=1,pady=10)

dato_F2=Tk.Entry(ventana,width=20)
dato_F2.grid(row=5,column=4,rowspan=1,columnspan=1,pady=10)

dato_K2=Tk.Entry(ventana,width=20)
dato_K2.grid(row=6,column=4,rowspan=1,columnspan=1,pady=10)

dato_C2=Tk.Entry(ventana,width=20)
dato_C2.grid(row=7,column=4,rowspan=1,columnspan=1,pady=10)

# se crean botones para que asi se identifique cual es cada conversión
BtnConvert1=Tk.Button(ventana,text="conversion -->",command=lambda:convert1(dato_F1,etq_Result1))
BtnConvert1.grid(row=2,column=5,rowspan=1,columnspan=1,pady=10)

BtnConvert2=Tk.Button(ventana,text="conversion -->",command=lambda:convert2(dato_C1,etq_Result2))
BtnConvert2.grid(row=3,column=5,rowspan=1,columnspan=1,pady=10)

BtnConvert3=Tk.Button(ventana,text="conversion -->",command=lambda:convert3(dato_K1,etq_Result3))
BtnConvert3.grid(row=4,column=5,rowspan=1,columnspan=1,pady=10)

BtnConvert4=Tk.Button(ventana,text="conversion -->",command=lambda:convert4(dato_F2,etq_Result4))
BtnConvert4.grid(row=5,column=5,rowspan=1,columnspan=1,pady=10)

BtnConvert5=Tk.Button(ventana,text="conversion -->",command=lambda:convert5(dato_K2,etq_Result5))
BtnConvert5.grid(row=6,column=5,rowspan=1,columnspan=1,pady=10)

BtnConvert6=Tk.Button(ventana,text="conversion -->",command=lambda:convert6(dato_C2,etq_Result6))
BtnConvert6.grid(row=7,column=5,rowspan=1,columnspan=1,pady=10)


# estas etiquetas indican el resultado de las conversiones
etq_Result1=Tk.Label(ventana,text="")
etq_Result1.grid(row=2,column=6,rowspan=1,columnspan=1,pady=10)

etq_Result2=Tk.Label(ventana,text="")
etq_Result2.grid(row=3,column=6,rowspan=1,columnspan=1,pady=10)

etq_Result3=Tk.Label(ventana,text="")
etq_Result3.grid(row=4,column=6,rowspan=1,columnspan=1,pady=10)

etq_Result4=Tk.Label(ventana,text="")
etq_Result4.grid(row=5,column=6,rowspan=1,columnspan=1,pady=10)

etq_Result5=Tk.Label(ventana,text="")
etq_Result5.grid(row=6,column=6,rowspan=1,columnspan=1,pady=10)

etq_Result6=Tk.Label(ventana,text="")
etq_Result6.grid(row=7,column=6,rowspan=1,columnspan=1,pady=10)



ventana.mainloop()
