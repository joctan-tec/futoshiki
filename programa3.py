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

from os import close
from tkinter import *
from tkinter import font 
import random
from tkinter import messagebox
import pickle



######################################################################################
# Clases
######################################################################################

class menu():
    
    def jugar():
        
        boton_jugar = Button(ventana_menu,background="#EC7D36", border="1" , text="Jugar",font="times 25")
        boton_jugar.place(x=350, y=180, width=200, height=40)
        
        
    def configuracion():
        
        boton_config = Button(ventana_menu,command=configuracion_window, background="#EC7D36", border="1" , text="Configuración",font="times 25")
        boton_config.place(x=350, y=228, width=200, height=40)
        
    
        
        
    def ayuda():
        
        boton_ayuda = Button(ventana_menu,background="#EC7D36", border="1" , text="Ayuda",font="times 25")
        boton_ayuda.place(x=350, y=276, width=200, height=40)
        
    def acerca_de():
        
        boton_acerca = Button(ventana_menu,background="#EC7D36", border="1" , text="Acerca de",font="times 25", command=acerca_de)
        boton_acerca.place(x=350, y=324, width=200, height=40)
        
        
        
    
        
    
        
    def salir():
        
        boton_salir = Button(ventana_menu,command=menu.advertencia_salir,background="#EC7D36", border="1" , text="Salir",font="times 25")
        
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

def configuracion_window():
    
    ventana_configuracion = Toplevel()
    
    ventana_configuracion.geometry("900x600")
    ventana_configuracion.title("Configuración FUTOSHIKI ")
    ventana_configuracion.config(background="#3A8D38")
    ventana_configuracion.resizable(width=False, height=False)
    
    
    etiqueta_nivel = Label(ventana_configuracion,text="Nivel", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_nivel.place(x=129, y=111,width=121,height=36)
    
    
    seleccionado_dificultad = StringVar()
    boton_facil = Radiobutton(ventana_configuracion,text="Fácil",variable=seleccionado_dificultad, value="Fácil",bg="#FFBF95", font="times 14", )
    boton_facil.place(x=150,y=165)
   
    boton_medio = Radiobutton(ventana_configuracion,text="Medio", variable=seleccionado_dificultad,value="Medio", bg="#FFBF95", font="times 14", )
    boton_medio.place(x=150,y=220)
    
    boton_dificil = Radiobutton(ventana_configuracion,text="Difícil", variable=seleccionado_dificultad,value="Difícil", bg="#FFBF95", font="times 14", )
    boton_dificil.place(x=150,y=275)
    
    
    
    
    
    
    etiqueta_reloj = Label(ventana_configuracion,text="Reloj", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_reloj.place(x=388, y=111,width=121,height=36)
    
    
    
    seleccionado_reloj = StringVar()
    boton_facil = Radiobutton(ventana_configuracion,text="Sí",variable=seleccionado_reloj, value="Sí",bg="#FFBF95", font="times 14", )
    boton_facil.place(x=408,y=165)
   
    boton_medio = Radiobutton(ventana_configuracion,text="No",variable=seleccionado_reloj,value="No", bg="#FFBF95", font="times 14", )
    boton_medio.place(x=408,y=220)
    
    boton_medio = Radiobutton(ventana_configuracion,text="Timer",variable=seleccionado_reloj,value="Timer", bg="#FFBF95", font="times 14", )
    boton_medio.place(x=408,y=275)
    
    etiqueta_posicion_digitos = Label(ventana_configuracion,text="Posicion de dígitos", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_posicion_digitos.place(x=648, y=111,width=170,height=36)
    
    
    seleccionado_posicion = StringVar()
    boton_izquierda = Radiobutton(ventana_configuracion,text="Izquierda",variable=seleccionado_posicion, value="Izquierda",bg="#FFBF95", font="times 14", )
    boton_izquierda.place(x=675,y=165)
   
    boton_derecha = Radiobutton(ventana_configuracion,text="Derecha",variable=seleccionado_posicion,value="Derecha", bg="#FFBF95", font="times 14", )
    boton_derecha.place(x=675,y=220)
    
    
    def salvar_datos_config():
    
    
        dificultad, reloj, posicion = seleccionado_dificultad.get(),seleccionado_reloj.get(),seleccionado_posicion.get()
        
        datos_configuracion = open("futoshiki2021configuración.dat","wb")
        
        tupla_informacion = (dificultad, reloj, posicion)
        
        pickle.dump(tupla_informacion, datos_configuracion)
        
        datos_configuracion.close()
        
        ventana_configuracion.destroy()
        
        ventana_menu.deiconify()
    
    
    boton_aceptar_config = Button(ventana_configuracion,text="Aceptar",font="times 16",command=salvar_datos_config)
    boton_aceptar_config.place(x=415,y=345,width=70,height=25)

    
    
    
    
    ventana_menu.iconify()
    
    
    
    
    ventana_configuracion.mainloop()
    
    
    
def acerca_de():
    
    ventana_acerca_de = Toplevel()
    ventana_menu.iconify()
    
    ventana_acerca_de.geometry("900x600")
    ventana_acerca_de.title("Acerca de - FUTOSHIKI ")
    ventana_acerca_de.config(background="#3A8D38")
    ventana_acerca_de.resizable(width=False, height=False)
    
    
    titulo = Label(ventana_acerca_de, text = "FUTOSHIKI", font="times 23", bg ="#3A8D38", foreground="#FFF",justify=CENTER)
    titulo.place(x=325, y=26, width=250,height=48)
    
    
    creacion = Label(ventana_acerca_de, text = "Fecha de creacion: 24-06-2021", font="times 17", bg ="#3A8D38", foreground="#FFF")
    creacion.place(x=219, y=118, width=460,height=48)
    
    autor = Label(ventana_acerca_de, text = "Autor: Joctan Antonio Porras Esquivel", font="times 14", bg ="#3A8D38", foreground="#FFF")
    autor.place(x=219, y=214, width=460,height=48)
    
    def destruir_ventana():
        ventana_menu.deiconify()
        ventana_acerca_de.destroy()
    
    
    boton_aceptar_acerca = Button(ventana_acerca_de,text="Aceptar",font="times 16",command=destruir_ventana)
    boton_aceptar_acerca.place(x=415,y=345,width=70,height=25)
    
    
    
    
    
    ventana_acerca_de.mainloop()
    
    
    

    
    
    


    
    
    
    
    




######################################################################################
# Programa Principal
######################################################################################

#ventana principal donde esta el menú
ventana_menu = Tk()
ventana_menu.geometry("900x600")
ventana_menu.title("FUTOSHIKI")
ventana_menu.config(background="#3A8D38")
ventana_menu.resizable(width=False, height=False)


#pongo la configuracion por defecto
datos_configuracion = open("futoshiki2021configuración.dat","w")
lista_configuracion = ("facil","si","derecha")
datos_configuracion = open("futoshiki2021configuración.dat","wb")
pickle.dump(lista_configuracion,datos_configuracion)
datos_configuracion.close()


#despliega los botones del menu, los cuales son metodos de la clase menú
menu.jugar()
menu.configuracion()
menu.ayuda()
menu.acerca_de()
menu.salir()



ventana_menu.mainloop()