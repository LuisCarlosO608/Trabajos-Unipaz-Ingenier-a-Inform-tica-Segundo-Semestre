listaR=[]

def suma(textbox1, textbox2,label):
    global listaR
    
    num1=int(textbox1.get())
    num2=int(textbox2.get())
    suma=num1+num2
    
    listaR.append(suma)
    
    label.configure(text=str(suma))

def resta(textbox1,textbox2,label2):
    global listaR
    num1=int(textbox1.get())
    num2=int(textbox2.get())
    resta=num1-num2
    listaR.append(resta)
    
    label2.configure(text=str(resta))
def lista(label3):
    global listaR
    label3.configure(text=str(listaR))
    
       
    
    