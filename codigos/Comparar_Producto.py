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


def compare(selection, ent1, ent2, ent3, ent4, lista):
    """Esta función toma el texto escrito en las dos entradas de la interfaz
    y el elemento seleccionado del OptionMenu, con esta información lee en
    archivo de Exccel las palabras y muestra en un espacio de tecto la información
    para comparar.
    """
    a = selection.get()
    b = ent1.get()
    c = ent2.get()
    book = Excel("wb8.xlsx", "Hoja1")
    window=tk.Tk()
    window.title("Informcación específica y comparación")
    texto = tk.Text(master=window, height=10, width=70)
    texto.grid(column=0, row=1)
    txtb = book.read_wb(b)
    txtc = book.read_wb(c)
    if b!=c:
    
        for i in range(len(lista)):
            if a == lista[i]:
                indicemenu = lista.index(lista[i])
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

    elif b==c:
        d=ent3.get()
        e=ent4.get()
        txtd= book.read2wrds_wb(b, d)
        print(txtd)
        txte= book.read2wrds_wb(b, e)
        print(txte)
        for i in range(len(lista)):
            if a == lista[i]:
                indicemenu = lista.index(lista[i])
                indiceexceld = txtd[indicemenu+3]
                indiceexcele = txte[indicemenu+3]
                numsd=re.sub("\D", "", indiceexceld)
                numse=re.sub("\D", "", indiceexcele)
                comparación = min(numsd, numse)
                if comparación == numsd:
                    msg="El producto {0} de la marca {1}".format(c,d)
                    comp = "es más salubable con respecto a {0}".format(a)
                    comp2= "\n" + "Con: {0}".format(indiceexceld)
                    msg1="El producto {0} de la marca {1}".format(c, e)
                    comp3=" es menos salubable con respecto a {0}".format(a) 
                    comp4="\n" + "Con: {0}".format(indiceexcele)
                    texto.insert(tk.END, ( msg + comp + comp2+"\n" + msg1 + comp3 + comp4))
                elif comparación == numse:
                    msg2="El producto {0} de la marca {1}".format(c, e)
                    comp5= " es más salubable con respecto a {0}".format(a)
                    comp6= "\n" + "Con: {0}".format(indiceexcele)
                    msg3="El producto {0} de la marca {1}".format(c, d)
                    comp7=" es menos salubable con respecto a {0}".format(a)
                    comp8="\n" + "Con: {3}".format(indiceexceld)
                    texto.insert(tk.END, ("\n" + msg2 + comp5 + comp6 +"\n" + msg3+comp7 + comp8))
        
    window.mainloop()
    return window
            
                             
            
            
            
            
            
def Comparar_wn():

    """Esta función crea la ventana que permite comparar productos,
        se activa al dar cick en: 'Comparar Producto' """
    #---Ventana 'Comparar Producto'----
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
    lb5.grid(column=0, row=7, padx=30, sticky="W")

    lb6 = tk.Label(otherwn, text="Si el producto es el mismo, por favor ingrese las marcas a comparar",
                      font=("Malgun Gothic Semilight", 12))
    lb6.grid(column=0, row=5, padx=20,sticky="W")
    lb7 = tk.Label(otherwn, text="Marca 1",
                      font=("Malgun Gothic Semilight", 11))
    lb7.grid(column=0, row=6, padx=30, pady=10, sticky="W")

    lb8 = tk.Label(otherwn, text="Marca 2",
                      font=("Malgun Gothic Semilight", 11))
    lb8.grid(column=0, row=6, padx=250, pady=10,sticky="W")

    #---Entrada de texto---
    entry1 = tk.Entry(master=otherwn)
    entry1.grid(column=0, row=4, padx=110, pady=10, sticky="W")
    
    entry2 = tk.Entry(master=otherwn)
    entry2.grid(column=0, row=4, padx=330, pady=10,sticky="W")
    
    entry3 = tk.Entry(master=otherwn)
    entry3.grid(column=0, row=6, padx=110, pady=10, sticky="W")
   
    entry4 = tk.Entry(master=otherwn)
    entry4.grid(column=0, row=6, padx=330, pady=10,sticky="W")
  


    #--lista de Optionmenu---
    variables =["Peso Neto", "Tamaño por porción", "Calorías", "Calorías de grasa",
                "Grasa Saturada",  "Grasas Trans", "Colesterol", "Sodio", "Fibra",
                "Azúcares", "Vitamina A", "Vitamina C", "Vitamina D", "Vitamina E",
                "Calcio", "Hierro"]
    #---Optionmenu---
    selección = tk.StringVar()
    selección.set("Seleccione una opción")

    om = tk.OptionMenu(otherwn, selección,  *variables)
    om.grid(column=0, row=8, padx=150, sticky="W")

    #---Boton---
    but1=tk.Button(master=otherwn, text="Buscar información",
                   command=lambda:compare(selección, entry1, entry2,
                                          entry3, entry4, variables))
    but1.grid(column=0, row=18, pady= 20,sticky="W")


    otherwn.mainloop()

    return otherwn
