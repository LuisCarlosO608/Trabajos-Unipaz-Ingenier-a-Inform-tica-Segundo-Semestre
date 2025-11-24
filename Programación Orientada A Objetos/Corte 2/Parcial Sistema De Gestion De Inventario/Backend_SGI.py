

class invent:
    def __init__(self):
        self.P={}
        self.C=[]
    def añadir_C(self,cat):
        if cat in self.C:
            raise ValueError ("esta categoria ya existe")
        self.C.append(cat)
    def registro_P(self,ID,n,cat,cant,pre):
        if cat not in self.C:
            raise ValueError("esta categoria no existe")
        self.P[ID]={
            "nombre":n,
            "categoria":cat,
            "cantidad":cant,
            "precio":pre
            
        }
    def edit_P(self,ID,n=None,cat=None,cant=None,pre=None):
        if ID in self.P:
            if n:self.P[ID]["nombre"]= n
            if cat:self.P[ID]["categoria"]=cat
            if cant is not None :self.P[ID]["cantidad"]=cant
            if pre is not None :self.P[ID]["precio"]=pre
    def gen_F(self,orden):
        fac=[]
        total=0
        for ID,cant in orden.items():
            prod=self.P[ID]
            subt=prod["precio"]*cant
            fac.append((prod["nombre"],cant,prod["precio"],subt))
            total+=subt
        return fac,total
            
        

