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


#se importan todos los modulos necesarios
from os import close
from tkinter import *
from tkinter import font 
import random
from tkinter import messagebox
import pickle



######################################################################################
# Clases
######################################################################################

#clase con todos los elementos del menu
class menu():
    
    #boton conectado a la ventana de jugar
    def jugar():
        
        boton_jugar = Button(ventana_menu,background="#EC7D36", command=jugar, border="1" , text="Jugar",font="times 25")
        boton_jugar.place(x=350, y=180, width=200, height=40)
        
     #boton conectado a la ventana de ajustes
    def configuracion():
        
        boton_config = Button(ventana_menu,command=configuracion_window, background="#EC7D36", border="1" , text="Configuración",font="times 25")
        boton_config.place(x=350, y=228, width=200, height=40)
        
    
        
     #boton conectado al pdf de ayuda    
    def ayuda():
        
        boton_ayuda = Button(ventana_menu,background="#EC7D36", border="1" , text="Ayuda",font="times 25",command=ayuda)
        boton_ayuda.place(x=350, y=276, width=200, height=40)
     
      #boton conectado a la ventana de informacion   
    def acerca_de():
        
        boton_acerca = Button(ventana_menu,background="#EC7D36", border="1" , text="Acerca de",font="times 25", command=acerca_de)
        boton_acerca.place(x=350, y=324, width=200, height=40)
        
        
    #boton para salir
        
    def salir():
        
        boton_salir = Button(ventana_menu,command=menu.advertencia_salir,background="#EC7D36", border="1" , text="Salir",font="times 25")
        
        boton_salir.place(x=350, y=372, width=200, height=40)
    
     
        
    #mensaje para salir
    def advertencia_salir():
        
        mensaje_salir = messagebox.askyesno("Salir","¿Está seguro que desea salir?")
        
        #evalua si quiere salir o no
        if mensaje_salir:
            exit()
        
        else:
            pass
        
        
        



    
    
    

######################################################################################
# Funciones
######################################################################################

# contiene la ventana de la configuracion 
def configuracion_window():
    
    #elementos necesarios para que la ventana aparezca y tenga tamaño fijo
    ventana_configuracion = Toplevel()
    #elemento que oculta el menu principal
    ventana_menu.iconify()
    ventana_configuracion.geometry("900x600")
    ventana_configuracion.title("Configuración FUTOSHIKI ")
    ventana_configuracion.config(background="#3A8D38")
    ventana_configuracion.resizable(width=False, height=False)
    
    #etiqueta simple
    etiqueta_nivel = Label(ventana_configuracion,text="Nivel", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_nivel.place(x=129, y=111,width=121,height=36)
    
    
    
    #variable que va a contener el valor del boton seleccionado.
    seleccionado_dificultad = StringVar()
    boton_facil = Radiobutton(ventana_configuracion,text="Fácil",variable=seleccionado_dificultad, value=1,bg="#FFBF95", font="times 14", )
    boton_facil.place(x=150,y=165)
    seleccionado_dificultad.set("1")
   
    boton_medio = Radiobutton(ventana_configuracion,text="Medio", variable=seleccionado_dificultad,value=2, bg="#FFBF95", font="times 14", )
    boton_medio.place(x=150,y=220)
    
    boton_dificil = Radiobutton(ventana_configuracion,text="Difícil", variable=seleccionado_dificultad,value=3, bg="#FFBF95", font="times 14", )
    boton_dificil.place(x=150,y=275)
    
    
    
    
    #etiqueta simple
    
    etiqueta_reloj = Label(ventana_configuracion,text="Reloj", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_reloj.place(x=388, y=111,width=121,height=36)
    
    #variable que va a contener el valor del boton seleccionado.
    
    seleccionado_reloj = StringVar()
    seleccionado_reloj.set("1")
    boton_facil = Radiobutton(ventana_configuracion,text="Sí",variable=seleccionado_reloj, value=1,bg="#FFBF95", font="times 14", )
    boton_facil.place(x=408,y=165)
   
    boton_medio = Radiobutton(ventana_configuracion,text="No",variable=seleccionado_reloj,value=2, bg="#FFBF95", font="times 14", )
    boton_medio.place(x=408,y=220)
    
    boton_medio = Radiobutton(ventana_configuracion,text="Timer",variable=seleccionado_reloj,value=3, bg="#FFBF95", font="times 14", )
    boton_medio.place(x=408,y=275)
    
    #etiqueta simple
    etiqueta_posicion_digitos = Label(ventana_configuracion,text="Posicion de dígitos", justify=CENTER,font="times 16",bg="#EC7D36")
    etiqueta_posicion_digitos.place(x=648, y=111,width=170,height=36)
    
    #variable que va a contener el valor del boton seleccionado.
    seleccionado_posicion = StringVar()
    seleccionado_posicion.set("2")
    boton_izquierda = Radiobutton(ventana_configuracion,text="Izquierda",variable=seleccionado_posicion, value=1,bg="#FFBF95", font="times 14", )
    boton_izquierda.place(x=675,y=165)
   
    boton_derecha = Radiobutton(ventana_configuracion,text="Derecha",variable=seleccionado_posicion,value=2, bg="#FFBF95", font="times 14", )
    boton_derecha.place(x=675,y=220)
    
    #guarda los datos en el archivo
    def salvar_datos_config():
    
    
        dificultad, reloj, posicion = seleccionado_dificultad.get(),seleccionado_reloj.get(),seleccionado_posicion.get()
        
        datos_configuracion = open("futoshiki2021configuración.dat","wb")
        
        tupla_informacion = (dificultad, reloj, posicion)
        
        pickle.dump(tupla_informacion, datos_configuracion)
        
        datos_configuracion.close()
        
        #cierro la ventana
        ventana_configuracion.destroy()
        
        #vuelvo a traer la ventana del menu
        ventana_menu.deiconify()
    
    
    boton_aceptar_config = Button(ventana_configuracion,text="Aceptar",font="times 16",command=salvar_datos_config)
    boton_aceptar_config.place(x=415,y=345,width=70,height=25)

    
    ventana_configuracion.mainloop()
    
    
# contiene la ventana de acerca de
def acerca_de():
    #elementos necesarios para que la ventana aparezca y tenga tamaño fijo
    ventana_acerca_de = Toplevel()
     #elemento que oculta el menu principal
    ventana_menu.iconify()
    
    ventana_acerca_de.geometry("900x600")
    ventana_acerca_de.title("Acerca de - FUTOSHIKI ")
    ventana_acerca_de.config(background="#3A8D38")
    ventana_acerca_de.resizable(width=False, height=False)
    
    
    #variables con los objetos que apareceran en pantalla
    titulo = Label(ventana_acerca_de, text = "FUTOSHIKI", font="times 23", bg ="#3A8D38", foreground="#FFF",justify=CENTER)
    titulo.place(x=325, y=26, width=250,height=48)
    
    
    creacion = Label(ventana_acerca_de, text = "Fecha de creacion: 24-06-2021", font="times 17", bg ="#3A8D38", foreground="#FFF")
    creacion.place(x=219, y=118, width=460,height=48)
    
    autor = Label(ventana_acerca_de, text = "Autor: Joctan Antonio Porras Esquivel", font="times 14", bg ="#3A8D38", foreground="#FFF")
    autor.place(x=219, y=190, width=460,height=48)
    
    version = Label(ventana_acerca_de, text = "Versión: 1.0", font="times 14", bg ="#3A8D38", foreground="#FFF")
    version.place(x=219, y=245, width=460,height=48)
    
    def destruir_ventana():
        ventana_menu.deiconify()
        ventana_acerca_de.destroy()
    
    
    boton_aceptar_acerca = Button(ventana_acerca_de,text="Aceptar",font="times 16",command=destruir_ventana)
    boton_aceptar_acerca.place(x=415,y=345,width=70,height=25)
    
    
    
    
    
    ventana_acerca_de.mainloop()
    
    
    
def ayuda():
    
    #Abre pdf de ayuda
        
            
    import subprocess
    path = 'manual_de_usuario_futoshiki.pdf'
    subprocess.Popen([path], shell=True)
    
    
    
    
def jugar():
    # contiene la ventana de juego
    ventana_juego = Toplevel()
     #elemento que oculta el menu principal
    ventana_menu.iconify()
    
    ventana_juego.geometry("900x640")
    ventana_juego.title("Jugar - FUTOSHIKI ")
    ventana_juego.config(background="#3A8D38")
    ventana_juego.resizable(width=False, height=False)
    
    
    titulo = Label(ventana_juego, text = "FUTOSHIKI", font="times 23", bg ="#FF0000", foreground="#FFF",justify=CENTER)
    titulo.place(x=325, y=22, width=250,height=48)
    
    #abro archivo para poner el nivel segun la opcion seleccionada
    archivo = open("futoshiki2021configuración.dat","rb")
    
    nivel = pickle.load(archivo)
    
    if nivel[0] == "1" or nivel[0]==1:
        dificultad_juego = "FÁCIL"
        
    elif nivel[0] == "2":
        dificultad_juego = "MEDIO"
        
    elif nivel[0] == "3":
        dificultad_juego = "DIFÍCIL"
        
    archivo.close()
    
    nivel_label = Label(ventana_juego,
                        text="NIVEL "+dificultad_juego,font="times 14"
                        ,justify=CENTER, foreground="#fff", bg="#3A8D38")
    nivel_label.place(x=386,y=74,width=129,height=21)
    
    
    nombre_jugador_label = Label(ventana_juego, text="Nombre del jugador: ",font="times 14"
                        ,justify=CENTER, foreground="#fff",bg="#3A8D38")

    nombre_jugador_label.place(x=47,y=105,width=188,height=24)
    
    
    nombre_entry = Entry(ventana_juego,background="#8FF98D",border=4)
    nombre_entry.place(x=247,y=105,width=404,height=24)
    
    #fila 1
    cuadros_centro1 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro1.place(x=246,y=169,width=50,height=50)
    
    cuadros_centro2 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro2.place(x=310,y=169,width=50,height=50)
    
    cuadros_centro3 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro3.place(x=374,y=169,width=50,height=50)
    
    cuadros_centro4 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro4.place(x=438,y=169,width=50,height=50)
    
    cuadros_centro5 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro5.place(x=502,y=169,width=50,height=50)
    
    #fila 2
    
    
    cuadros_centro6 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro6.place(x=246,y=233,width=50,height=50)
    
    cuadros_centro7 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro7.place(x=310,y=233,width=50,height=50)
    
    cuadros_centro8 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro8.place(x=374,y=233,width=50,height=50)
    
    cuadros_centro9 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro9.place(x=438,y=233,width=50,height=50)
    
    cuadros_centro10 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro10.place(x=502,y=233,width=50,height=50)
    
    
    #fila 3
    
    cuadros_centro11 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro11.place(x=246,y=297,width=50,height=50)
    
    cuadros_centro12 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro12.place(x=310,y=297,width=50,height=50)
    
    cuadros_centro13 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro13.place(x=374,y=297,width=50,height=50)
    
    cuadros_centro14 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro14.place(x=438,y=297,width=50,height=50)
    
    cuadros_centro15 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro15.place(x=502,y=297,width=50,height=50)
    
    
    #fila 4
    
    cuadros_centro16 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro16.place(x=246,y=361,width=50,height=50)
    
    cuadros_centro17 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro17.place(x=310,y=361,width=50,height=50)
    
    cuadros_centro18 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro18.place(x=374,y=361,width=50,height=50)
    
    cuadros_centro19 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro19.place(x=438,y=361,width=50,height=50)
    
    cuadros_centro20 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro20.place(x=502,y=361,width=50,height=50)
    
    
    #fila 5
    
    cuadros_centro21 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro21.place(x=246,y=425,width=50,height=50)
    
    cuadros_centro22 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro22.place(x=310,y=425,width=50,height=50)
    
    cuadros_centro23 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro23.place(x=374,y=425,width=50,height=50)
    
    cuadros_centro24 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro24.place(x=438,y=425,width=50,height=50)
    
    cuadros_centro25 = Button(ventana_juego, bg="#C1FFA0")
    cuadros_centro25.place(x=502,y=425,width=50,height=50)
    
    
    
    
    # botones derecha
    
    
    boton_derecha1 = Button(ventana_juego,text="1",font="times 20", bg="#C1FFA0")
    boton_derecha1.place(x=764,y=169,width=50,height=50)
    
    boton_derecha2 = Button(ventana_juego,text="2",font="times 20", bg="#C1FFA0")
    boton_derecha2.place(x=764,y=233,width=50,height=50)
    
    boton_derecha3 = Button(ventana_juego,text="3",font="times 20", bg="#C1FFA0")
    boton_derecha3.place(x=764,y=297,width=50,height=50)
    
    boton_derecha4 = Button(ventana_juego,text="4",font="times 20", bg="#C1FFA0")
    boton_derecha4.place(x=764,y=361,width=50,height=50)
    
    boton_derecha5 = Button(ventana_juego,text="5",font="times 20", bg="#C1FFA0")
    boton_derecha5.place(x=764,y=425,width=50,height=50)
    
    
    
    def cerrar_ventana():
        ventana_juego.destroy()
        ventana_menu.deiconify()
    
    #botones de abajo
    
    boton_iniciar = Button(ventana_juego,text="INICIAR \n JUEGO",justify=CENTER,font="times 13", bg="#F6FF69")
    boton_iniciar.place(x=40,y=490,width=125,height=40)
    
    boton_borrar = Button(ventana_juego,text="BORRAR \n JUGADA",justify=CENTER,font="times 13", bg="#FF7FDC")
    boton_borrar.place(x=175,y=490,width=125,height=40)
    
    boton_terminar = Button(ventana_juego,command=cerrar_ventana,text="TERMINAR \n JUEGO",justify=CENTER,font="times 13", bg="#7FE6FF")
    boton_terminar.place(x=310,y=490,width=125,height=40)
    
    boton_borrar_juego = Button(ventana_juego,text="BORRAR \n JUEGO",justify=CENTER,font="times 13", bg="#817FFF")
    boton_borrar_juego.place(x=445,y=490,width=125,height=40)
    
    boton_top = Button(ventana_juego,text="TOP \n 10",justify=CENTER,font="times 13", bg="#FFB17F")
    boton_top.place(x=580,y=490,width=125,height=40)
    
    
    # ultimos botones de abajo
    
    ultimos_botones_abajo = Button(ventana_juego, text = "GUARDAR JUEGO",justify=CENTER,font="times 13", bg="#FFF160")
    ultimos_botones_abajo.place(x=360,y=560,width=150,height=42)
    
    ultimos_botones_abajo2 = Button(ventana_juego, text = "CARGAR JUEGO",justify=CENTER,font="times 13", bg="#B060FF")
    ultimos_botones_abajo2.place(x=520,y=560,width=150,height=42)

    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    




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
lista_configuracion = (1,1,2)
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