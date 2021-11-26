import time
import os
  
def Quitarresp(Respuesta):
    if(Respuesta[-1]==" "):
        Respuesta=Respuesta[:-1]
        #print(Respuesta)
        if(Respuesta[-1]==" "):
            Respuesta=Quitarresp(Respuesta)   
    return Respuesta
    
def formpreg(instruccion,pista,solucion):
    solcorr=True
    while(solcorr):
        print(instruccion)
        resp=input()
        resp=Quitarresp(resp)
        if(solucion == resp):
            print("Correcto")
            solcorr=False
            time.sleep(3)
            os.system("cls") 
        elif("pista"== resp ):
            print(pista)
        elif("respuesta" == resp):
            print("La respuesta es: ", solucion)
            solcorr=False
            time.sleep(3)
            os.system("cls") 
        else:
            print("Intenta de nuevo :c o pide una pista")
            time.sleep(3)
            os.system("cls")

def Mostarinfo(texto):
    entendio="no"
    while(entendio!="si"): 
        print(texto)
        entendio=Quitarresp(input("\nDesea continuar? (si o no): ").lower())
        os.system("cls")