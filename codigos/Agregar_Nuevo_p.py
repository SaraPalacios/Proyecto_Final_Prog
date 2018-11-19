#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 11 2018

@author: Sara Palacios
"""
import tkinter as tk

from clase import *


def Agregar_wn():
    """Ésta función crea una ventana con una interfaz adecuadapara que
        el usuario ingrese los datos de un producto nuevo
    """
    #---Ventana 'Agregar productos'---    
    oother = tk.Tk()
    oother.title("Agregar Producto")
    oother.geometry("840x520")
     
    #---Etiqueta principal---    
    lb1 = tk.Label(master=oother,
                   text="Aquí podrá agregar la información de un nuevo producto",
                   font=("Malgun Gothic Semilight", 10))
    lb1.grid(column=0, row=0, sticky="W")
   
    #---Etiquetas 'producto'---
    lb2 = tk.Label(master=oother, text="- Producto: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb2.grid(column=0, row=1, padx = 20, sticky="W" )
    tipo = tk.Label(master=oother, text="Tipo de producto:",
                    font=("Malgun Gothic Semilight", 10))
    tipo.grid(column=0, row=2, padx = 30, sticky="W")
    marca = tk.Label(master=oother, text="Marca de Producto: ",
                    font=("Malgun Gothic Semilight", 10))
    marca.grid(column=0, row=3, padx=30, sticky="W")
    producto = tk.Label(master=oother, text="Nombre Producto: ",
                    font=("Malgun Gothic Semilight", 10))
    producto.grid(column=0, row=4, padx=30, sticky="W")
    #---Etiquetas 'cantidad'---
    lb4 = tk.Label(master=oother, text="- Cantidad: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb4.grid(column=0, row=5, padx = 20, sticky="W" )
    peso= tk.Label(master=oother, text="Peso Neto: ",
                    font=("Malgun Gothic Semilight", 10))
    peso.grid(column=0, row=6, padx = 30, sticky="W")
    tamaño = tk.Label(master=oother, text="Tamaño porción: ",
                    font=("Malgun Gothic Semilight", 10))
    tamaño.grid(column=0, row=7, padx=30, sticky="W")
    #---Etiquetas'calorías'---
    lb3 = tk.Label(master=oother, text="- Calorias: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb3.grid(column=0, row=8, padx = 20, sticky="W")
    calorías = tk.Label(master=oother, text="Calorías: ",
                    font=("Malgun Gothic Semilight", 10))
    calorías.grid(column=0, row=9, padx = 30, sticky="W")
    calgrass = tk.Label(master=oother, text="Calorías de grasa: ",
                    font=("Malgun Gothic Semilight", 10))
    calgrass.grid(column=0, row=10, padx=30, sticky="W")
    #---Etiquetas 'Grasa Total'---
    lb5 = tk.Label(master=oother, text="- Grasa Total: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb5.grid(column=0, row=11, padx=30, sticky="W")
    grasasat= tk.Label(master=oother, text="Grasa Saturada: ",
                    font=("Malgun Gothic Semilight", 10))
    grasasat.grid(column=0, row=12, padx=30, sticky="W")
    grasatrans = tk.Label(master=oother, text="Grasas trans: ",
                    font=("Malgun Gothic Semilight", 10))
    grasatrans.grid(column=0, row=13, padx=30, sticky="W")    
    #---Etiqueta'Colesterol'---
    lb6 = tk.Label(master=oother, text="- Colesterol: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb6.grid(column=1, row=1, sticky="W")
    #---Etiqueta'sodio'---
    lb7 = tk.Label(master=oother, text="- Sodio: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb7.grid(column=1, row=2, pady= 5, sticky="W")
    #---Etiqueta'Carbohidratos'---
    lb8 = tk.Label(master=oother, text="- Total Carbohidratos: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb8.grid(column=1, row=3, pady= 5, sticky="W")
    fibra = tk.Label(master=oother, text="Fibra Dietaria: ",
                    font=("Malgun Gothic Semilight", 10))
    fibra.grid(column=1, row=4, pady= 5, sticky="W")
    azúcar = tk.Label(master=oother, text="Azúcares: ",
                    font=("Malgun Gothic Semilight", 10))
    azúcar.grid(column=1, row=5, pady= 5, sticky="W")
    #---Etiqueta 'Proteína'---
    lb10 = tk.Label(master=oother, text="- Proteína: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb10.grid(column=1, row=6, pady= 5, sticky="W")
    #Etiquetas 'Vitaminas'---
    lb9 = tk.Label(master=oother, text="- Vitaminas: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb9.grid(column=1, row=7, padx = 0, sticky="W" )
    VitA= tk.Label(master=oother, text="Vitamina A: ",
                    font=("Malgun Gothic Semilight", 10))
    VitA.grid(column=1, row=8, sticky="W")
    VitC = tk.Label(master=oother, text="Vitamina C: ",
                    font=("Malgun Gothic Semilight", 10))
    VitC.grid(column=1, row=9, sticky="W")
    VitD= tk.Label(master=oother, text="Vitamina D: ",
                    font=("Malgun Gothic Semilight", 10))
    VitD.grid(column=1, row=10, sticky="W")
    VitE = tk.Label(master=oother, text="Vitamina E: ",
                    font=("Malgun Gothic Semilight", 10))
    VitE.grid(column=1, row=11, sticky="W")
    #---Etiqueta'Calcio'---
    lb10 = tk.Label(master=oother, text="- Calcio: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb10.grid(column=1, row=12, sticky="W")
    #---Etiqueta'Hierro'---
    lb11 = tk.Label(master=oother, text="- Hierro: ",
                   font=("Malgun Gothic Semilight",10, "bold"))
    lb11.grid(column=1, row=13, sticky="W")

#-----------------------------------------------------------

    #---Entradas 'producto---
    tipop = tk.Entry(master=oother)
    tipop.grid(column=0, row=2, padx = 150, sticky="w")
    marcap = tk.Entry(master=oother)
    marcap.grid(column=0, row=3, padx=150, sticky="W")
    productop = tk.Entry(master=oother)
    productop.grid(column=0, row=4, padx=150, sticky="W")
    #---Entradas'cantidad'---
    pesop = tk.Entry(master=oother)
    pesop.grid(column=0, row=6, padx=150, sticky="W")    
    tamañop = tk.Entry(master=oother)
    tamañop.grid(column=0, row=7, padx=150, sticky="W")
    #---Entradas 'calorías'---
    caloríasp = tk.Entry(master=oother)
    caloríasp.grid(column=0, row=9, padx=150, sticky="W")
    calgrassp = tk.Entry(master=oother)
    calgrassp.grid(column=0, row=10, padx=150, sticky="W")
    #---Entradas 'Grasa Total'---
    grasasatp = tk.Entry(master=oother)
    grasasatp.grid(column=0, row=12, padx=150, sticky="W")
    grasatransp = tk.Entry(master=oother)
    grasatransp.grid(column=0, row=13, padx=150, sticky="W")
    #---Entrada 'colesterol'---
    colp = tk.Entry(master=oother)
    colp.grid(column=1, row=1, padx=130, pady=10, sticky="W")
    #---Entrada 'sodio'---
    sodiop = tk.Entry(master=oother)
    sodiop.grid(column=1, row=2, padx=130, pady=10, sticky="W")
    #---Entradas 'Carbohidratos'---
    fibrap = tk.Entry(master=oother)
    fibrap.grid(column=1, row=4, padx=130, pady=10, sticky="W")
    azúcarp = tk.Entry(master=oother)
    azúcarp.grid(column=1, row=5, padx=130, pady=10, sticky="W")
    #---Entrada 'Proteína'---
    protp = tk.Entry(master=oother)
    protp.grid(column=1, row=6, padx=130, pady=10, sticky="W")
    #---Entradas 'Vitaminas'---
    VitAp = tk.Entry(master=oother)
    VitAp.grid(column=1, row=8, padx=130, pady=10, sticky="W")
    VitCp = tk.Entry(master=oother)
    VitCp.grid(column=1, row=9, padx=130, pady=10, sticky="W")
    VitDp = tk.Entry(master=oother)
    VitDp.grid(column=1, row=10, padx=130, pady=10, sticky="W")
    VitEp = tk.Entry(master=oother)
    VitEp.grid(column=1, row=11, padx=130, pady=10, sticky="W")
    #---Entradas 'Calcio'---
    Calciop = tk.Entry(master=oother)
    Calciop.grid(column=1, row=12, padx=130, pady=10, sticky="W")
    #---Entradas 'Hierro'---
    hierrop = tk.Entry(master=oother)
    hierrop.grid(column=1, row=13, padx=130, pady=10, sticky="W")

#-----------------------------------------------------------------
    
    #---Botón---
    bot1 = tk.Button(master=oother, text="Guardar Cambios",
                     command= lambda: guardar(lista_entradas))
    bot1.grid(column=1, row=13, sticky="E")
    
    lista_entradas=[tipop, marcap, productop, pesop, tamañop,
                    caloríasp, calgrassp, grasasatp, grasatransp,
                    colp, sodiop, fibrap, azúcarp, protp, VitAp,
                    VitCp, VitDp, VitEp, Calciop, hierrop]
    
    oother.mainloop()
    return oother

def guardar(asx):
    """Función que tiene como argumento la lista creada con
        la función: "entradas()". Esta lista pasa a ser
        el argumento del método write_wb() ser escrita
        en el archivo de Excel
    """
    win = tk.Tk()
    win.title("Aviso")
    win.geometry("200x100")
    listaentras = entradas(asx)
    txt= tk.Text(master=win)
    txt.grid(column=0, row=1)
    txt.insert(tk.END, "Archivo guardado")
    libro = Excel("wb8.xlsx", "Hoja1")
    libro.write_wb(listaentras)
    

def entradas(lista):
    """Función que toma una lista de todas las entradas existentes
        y con ellas crea otra lista con el texto de cada una de
        ellas.
    """
    final=[]
    for i in range(0, len(lista)):
        final.append(str(lista[i].get()))
    return final
    
