'''
Tecnológico de Costa Rica

Escuela de Ingeniería en Computación

Taller de programación

William Mata Rodríguez

Programa 3: FUTOSHIKI

Joctan Antonio Porras Esquivel

Fecha de realización: 24-06-2021
'''


######################################################################################
# Módulos
######################################################################################

from tkinter import *
import random
from tkinter import messagebox
import pickle



######################################################################################
# Clases
######################################################################################

class menu():
    
    def jugar():
        
        boton_jugar = Button(ventana_config,background="#EC7D36", border="1" , text="Jugar",font="times 25")
        boton_jugar.place(x=350, y=180, width=200, height=40)
        
        
    def configuracion():
        
        boton_config = Button(ventana_config,background="#EC7D36", border="1" , text="Configuración",font="times 25")
        boton_config.place(x=350, y=228, width=200, height=40)
        
        
    def ayuda():
        
        boton_ayuda = Button(ventana_config,background="#EC7D36", border="1" , text="Ayuda",font="times 25")
        boton_ayuda.place(x=350, y=276, width=200, height=40)
        
    def acerca_de():
        
        boton_acerca = Button(ventana_config,background="#EC7D36", border="1" , text="Acerca de",font="times 25")
        boton_acerca.place(x=350, y=324, width=200, height=40)
        
    
        
    def salir():
        
        boton_salir = Button(ventana_config,command=menu.advertencia_salir,background="#EC7D36", border="1" , text="Salir",font="times 25")
        
        boton_salir.place(x=350, y=372, width=200, height=40)
        
    
    def advertencia_salir():
        
        mensaje_salir = messagebox.askyesno("Salir","¿Está seguro que desea salir?")
        
        if mensaje_salir:
            exit()
        
        else:
            pass
    
    
    

######################################################################################
# Funciones
######################################################################################

def configuracion():
    
    configuracion = open("futoshiki2021configuración.dat","wb")
    
    


######################################################################################
# Funciones
######################################################################################

######################################################################################
# Programa Principal
######################################################################################

ventana_config = Tk()
ventana_config.geometry("900x600")
ventana_config.title("FUTOSHIKI")
ventana_config.config(background="#3A8D38")
ventana_config.resizable(width=False, height=False)



menu.jugar()
menu.configuracion()
menu.ayuda()
menu.acerca_de()
menu.salir()



ventana_config.mainloop()