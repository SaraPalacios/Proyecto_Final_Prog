#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 24 2018
@author: Sara Palacios
"""
import tkinter as tk
import re
from clase import *
from Agregar_Nuevo_p import entradas


def compare():
    """Esta función toma el texto escrito en las dos entradas de la interfaz
    y el elemento seleccionado del OptionMenu, con esta información lee en
    archivo de Exccel las palabras y muestra en un espacio de tecto la información
    para comparar.
    """
    a = selección.get()
    b = entry1.get()
    c = entry2.get()
    book = Excel("wb8.xlsx", "Hoja1")
    txtb = book.read_wb(b)
    txtc = book.read_wb(c)
    txtbnums = book.read_numbs(b)
    
    window=tk.Tk()
    window.title("Informcación específica y comparación")
    texto = tk.Text(master=window, height=10, width=70)
    texto.grid(column=0, row=1)
    for i in range(len(variables)):
        if a == variables[i]:
            indicemenu = variables.index(variables[i])
            indiceexcelb = txtb[indicemenu+3]
            indiceexcelc = txtc[indicemenu+3]
            numsb=re.sub("\D", "", indiceexcelb)
            numsc=re.sub("\D", "", indiceexcelc)
            comparación = min(numsb, numsc)
            if comparación == numsb:
                msg="El producto más saludable con respecto a {0} es: {1}".format(a,b) + "\n" + "Con: {0}".format(indiceexcelb)
                msg1="El producto menos saludable con respecto a {0} es: {1}".format(a,c) + "\n" + "Con: {0}".format(indiceexcelc)
                texto.insert(tk.END, ("\n" + msg + "\n" + msg1))
            elif comparación == numsc:
                msg2="El producto más saludable con respecto a {0}, es: {1}".format(a,c) +"\n" + "con: {0}".format(indiceexcelc)
                msg3="El producto menos saludable con respecto a {0} es: {1}".format(a,b) + "\n" + "Con: {0}".format(indiceexcelb)
                texto.insert(tk.END, ("\n" + msg2 + "\n" + msg3))
            
                             
            
            
            
            
            


"""Esta función crea la ventana que permite comparar productos,
    se activa al dar cick en: 'Comparar Producto' """
#---Ventana 'Analizar producto'----
otherwn = tk.Tk()
otherwn.title("Comparar Producto")
otherwn.geometry("500x400")

#---Etiqueta principal---
mainlb = tk.Label(otherwn, text="En esta ventana puede comparar dos productos",
                  font=("Malgun Gothic Semilight", 13))
mainlb.grid(column=0, row=0,sticky="W")

lb2 = tk.Label(otherwn, text="Por favor ingrese los nombres de los productos a comparar",
                  font=("Malgun Gothic Semilight", 13))
lb2.grid(column=0, row=1, padx=30,sticky="W")

lb3 = tk.Label(otherwn, text="Producto 1",
                  font=("Malgun Gothic Semilight", 11))
lb3.grid(column=0, row=4, padx=30, pady=10, sticky="W")

lb4 = tk.Label(otherwn, text="Producto 2",
                  font=("Malgun Gothic Semilight", 11))
lb4.grid(column=0, row=4, padx=250, pady=10,sticky="W")

lb5 = tk.Label(otherwn, text="Por favor indique cuáles datos desea comparar",
                  font=("Malgun Gothic Semilight", 13))
lb5.grid(column=0, row=6, padx=30, sticky="W")

#---Entrada de texto---
entry1 = tk.Entry(master=otherwn)
entry1.grid(column=0, row=4, padx=110, pady=10, sticky="W")
palabra = entry1.get()
entry2 = tk.Entry(master=otherwn)
entry2.grid(column=0, row=4, padx=330, pady=10,sticky="W")
palabra2 = entry1.get()


#--lista de Optionmenu---
variables =["Peso Neto", "Tamaño por porción", "Calorías", "Calorías de grasa",
            "Grasa Saturada",  "Grasas Trans", "Colesterol", "Sodio", "Fibra",
            "Azúcares", "Vitamina A", "Vitamina C", "Vitamina D", "Vitamina E",
            "Calcio", "Hierro"]
#---Optionmenu---
selección = tk.StringVar()
selección.set("Seleccione una opción")

om = tk.OptionMenu(otherwn, selección,  *variables)

om.grid(column=0, row=7, padx=150, sticky="W")

#---Boton---
but1=tk.Button(master=otherwn, text="Buscar información", command=compare)
but1.grid(column=0, row=18, pady= 20,sticky="W")


otherwn.mainloop()

