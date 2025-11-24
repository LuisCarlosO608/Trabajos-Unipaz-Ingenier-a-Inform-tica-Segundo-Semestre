import tkinter as tk
from Backend_Calculadora_Convencional import suma,resta, lista
root=tk.Tk()
root.title("Calculadora")
root.geometry("800x600")
root.configure(bg="lightblue")

textbox1=tk.Entry(root,width=20)
textbox1.grid(row=0,column=0,padx=5,pady=10)
textbox2=tk.Entry(root,width=20)
textbox2.grid(row=0,column=4,padx=5,pady=10)

label=tk.Label(root,text="")
label.grid(row=1,column=2,columnspan=2,pady=5)

btn=tk.Button(root,text="sumar", command=lambda:suma(textbox1,textbox2,label))
btn.grid(row=2,column=2,columnspan=2,pady=10)

btn2=tk.Button(root,text="restar", command=lambda:resta(textbox1,textbox2,label2))
btn2.grid(row=2,column=3,columnspan=2,pady=5)

label2=tk.Label(root,text="")
label2.grid(row=1,column=3,columnspan=2,pady=5)
btn3=tk.Button(root,text="historial", command=lambda: lista(label3))
btn3.grid(row=4,column=2,columnspan=2,pady=10)

label3=tk.Label(root,text="")
label3.grid(row=5,column=2,columnspan=2,pady=10)

root.mainloop()

