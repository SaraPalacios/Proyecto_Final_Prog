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

         
            
def unico(wn):
    """Esta función activa el botón 'Mismo producto con diferente marca'
        para transformar la interfaz apropiadamente con la intención
        de que el usuario ingrese el nombre de un solo producto
        y compare las marcas.
    """
    def compareunic(selection, ent, ent3, ent4, lista):
        """Esta función es utilizada como comando al dar click en el
            botón 'Buscar información'. Esta crea una nueva ventana de texto
            en donde se especifíca cual marca es mejor que otra según
            un producto y su característica seleccionada.
        """
        a = selection.get()
        f = ent.get()
        d=ent3.get()
        e=ent4.get()
        book = Excel("wb8.xlsx", "Hoja1")
        window=tk.Tk()
        window.title("Informcación específica y comparación de un mismo producto")
        texto = tk.Text(master=window, height=10, width=70)
        texto.grid(column=0, row=1)
        txtd= book.read2wrds_wb(f, d)
        txte= book.read2wrds_wb(f, e)
        listanegas = lista[:9]
        listapros = lista[9:]
        
        for h in range(len(listanegas)):
            
            if a == listanegas[h]:
                indicemenu = listanegas.index(listanegas[h])
                indiceexceld = txtd[indicemenu+3]
                indiceexcele = txte[indicemenu+3]
                numsd=re.sub("\D", "", indiceexceld)
                numse=re.sub("\D", "", indiceexcele)
                
                if numsd == numse:
                    mes="El producto {0} de la marca {1}".format(f,d)
                    mes2=" es igual de saludable al "
                    mes3="producto {0} de la marca {1}.".format(f, e)
                    mes4="Con respecto a: {0}".format(a)
                    texto.insert(tk.END,
                                 (mes+mes2+mes3+"\n"+mes4))
                    
                elif min(numsd, numse)== numsd:
                    msg="El producto {0} de la marca {1}".format(f,d)
                    comp = "es más salubable con respecto a {0}".format(a)
                    comp2= "\n" + "Con: {0}".format(indiceexceld)
                    msg1="El producto {0} de la marca {1}".format(f, e)
                    comp3=" es menos salubable con respecto a {0}".format(a)
                    comp4="\n" + "Con: {0}".format(indiceexcele)
                    texto.insert(tk.END,
                                 (msg+comp+comp2+"\n"+msg1+comp3+comp4))
                elif min(numsd, numse)== numse:
                    msg2="El producto {0} de la marca {1}".format(f, e)
                    comp5= " es más salubable con respecto a {0}".format(a)
                    comp6= "\n" + "Con: {0}".format(indiceexcele)
                    msg3="El producto {0} de la marca {1}".format(f, d)
                    comp7=" es menos salubable con respecto a {0}".format(a)
                    comp8="\n" + "Con: {0}".format(indiceexceld)
                    texto.insert(tk.END,
                                 ("\n"+msg2+comp5+comp6+"\n"+msg3+comp7+comp8))
        for s in range(len(listapros)):
            if a==listapros[s]:
                indicemenu = listapros.index(listapros[s])
                indiceexceld = txtd[indicemenu+12]
                indiceexcele = txte[indicemenu+12]
                numsd=re.sub("\D", "", indiceexceld)
                numse=re.sub("\D", "", indiceexcele)
                if numsd == numse:
                    mes="El producto {0} de la marca {1}".format(f,d)
                    mes2=" es igual de saludable al "
                    mes3="producto {0} de la marca {1}.".format(f, e)
                    mes4="Con respecto a: {0}".format(a)
                    texto.insert(tk.END,
                                 (mes+mes2+mes3+"\n"+mes4))
                elif max(numsd, numse)== numsd:
                    msg="El producto {0} de la marca {1}".format(f,d)
                    comp = "es más salubable con respecto a {0}".format(a)
                    comp2= "\n" + "Con: {0}".format(indiceexceld)
                    msg1="El producto {0} de la marca {1}".format(f, e)
                    comp3=" es menos salubable con respecto a {0}".format(a)
                    comp4="\n" + "Con: {0}".format(indiceexcele)
                    texto.insert(tk.END,
                                 (msg+comp+comp2+"\n"+msg1+comp3+comp4))
                elif max(numsd, numse) == numse:
                    msg2="El producto {0} de la marca {1}".format(f, e)
                    comp5= " es más salubable con respecto a {0}".format(a)
                    comp6= "\n" + "Con: {0}".format(indiceexcele)
                    msg3="El producto {0} de la marca {1}".format(f, d)
                    comp7=" es menos salubable con respecto a {0}".format(a)
                    comp8="\n" + "Con: {0}".format(indiceexceld)
                    texto.insert(tk.END,
                                 ("\n"+msg2+comp5+comp6+"\n"+msg3+comp7+comp8))
                    
                
        
        window.mainloop()
        return window
    lb6 = tk.Label(wn, text="Por favor ingrese el nombre del producto",
                      font=("Malgun Gothic Semilight", 13))
    lb6.grid(column=0, row=6, padx=30, sticky="W")
    lb7 = tk.Label(wn, text="Producto: ",
                      font=("Malgun Gothic Semilight", 11))
    lb7.grid(column=0, row=7, padx=30, pady=10, sticky="W")
    lb8 = tk.Label(wn, text="Por favor ingrese las marcas a comparar",
                      font=("Malgun Gothic Semilight", 12))
    lb8.grid(column=0, row=8, padx=20,sticky="W")
    lb9 = tk.Label(wn, text="Marca 1",
                      font=("Malgun Gothic Semilight", 11))
    lb9.grid(column=0, row=9, padx=30, pady=10, sticky="W")

    lb10 = tk.Label(wn, text="Marca 2",
                      font=("Malgun Gothic Semilight", 11))
    lb10.grid(column=0, row=9, padx=250, pady=10,sticky="W")
    lb11 = tk.Label(wn, text="Por favor indique cuáles datos desea comparar",
                      font=("Malgun Gothic Semilight", 13))
    lb11.grid(column=0, row=10, padx=30, sticky="W")
    entry5 = tk.Entry(master=wn)
    entry5.grid(column=0, row=7, padx=110, pady=10, sticky="W")
    entry3 = tk.Entry(master=wn)
    entry3.grid(column=0, row=9, padx=110, pady=10, sticky="W")
    entry4 = tk.Entry(master=wn)
    entry4.grid(column=0, row=9, padx=330, pady=10,sticky="W")
    #---Optionmenu para elegir característica---
    variables =["Peso Neto", "Tamaño por porción", "Calorías", "Calorías de grasa",
                "Grasa Saturada",  "Grasas Trans", "Colesterol", "Sodio", "Azúcares",
                "Fibra","Proteína", "Vitamina A", "Vitamina C", "Vitamina D",
                "Vitamina E", "Calcio", "Hierro"]
    
    selección = tk.StringVar()
    selección.set("Seleccione una opción")

    om = tk.OptionMenu(wn, selección,  *variables)
    om.grid(column=0, row=11, padx=80, sticky="W")

    #---Boton---
    but1=tk.Button(master=wn, text="Buscar información",
                   command=lambda:compareunic(selección, entry5, entry3,
                                          entry4,variables))
    but1.grid(column=0, row=11,padx=270, pady= 20,sticky="W")

def distintos(wn):
    """Esta función activa el botón 'Distintos productos de diferentes marcas'
        para transformar la interfaz apropiadamente con la intención
        de que el usuario ingrese los nombres de los productos y se haga la
        comparación en general.
    """
    def comparedist(selection, ent1, ent2, lista):
        """Esta función es utilizada como comando al dar click en el
            botón 'Buscar información'. Esta crea una nueva ventana de texto
            en donde se especifíca cual producto es mejor según
            la característica seleccionada.
        """
        a = selection.get()
        b = ent1.get()
        c = ent2.get()
        book = Excel("wb8.xlsx", "Hoja1")
        window=tk.Tk()
        window.title("Informcación específica y comparación de dos productos diferentes")
        texto = tk.Text(master=window, height=10, width=70)
        texto.grid(column=0, row=1)
        txtb = book.read_wb(b)
        txtc = book.read_wb(c)
        listanegas = lista[:9]
        listapros = lista[9:]
        for i in range(len(listanegas)):
            if a == listanegas[i]:
                indicemenu = listanegas.index(listanegas[i])
                indiceexcelb = txtb[indicemenu+3]
                indiceexcelc = txtc[indicemenu+3]
                numsb=re.sub("\D", "", indiceexcelb)
                numsc=re.sub("\D", "", indiceexcelc)
                if numsb == numsc:
                    mes="El producto {0} ".format(b)
                    mes2=" es igual de saludable al "
                    mes3="producto {0}.".format(c)
                    mes4="Con respecto a: {0}".format(a)
                    texto.insert(tk.END,
                                 (mes+mes2+mes3+"\n"+mes4))
                
                elif max(numsb, numsc)== numsb:
                    msg="El producto más saludable con respecto a "+a
                    ot=", es: {0}".format(b)
                    ot2="\n" + "Con: {0}".format(indiceexcelb)
                    msg1="El producto menos saludable con respecto a "+a
                    ot3=", es: {0}".format(c)
                    ot4="\n" + "Con: {0}".format(indiceexcelc)
                    texto.insert(tk.END, (msg+ot+ot2+"\n"+msg1+ot3+ot4))
                elif max(numsb, numsc)== numsc:
                    msg2="El producto más saludable con respecto a "+a
                    ot5=", es: {0}".format(c)
                    ot6="\n" + "Con: {0}".format(indiceexcelc)
                    msg3="El producto menos saludable con respecto a "+a
                    ot7=", es: {0}".format(b)
                    ot8="\n" + "Con: {0}".format(indiceexcelb)
                    texto.insert(tk.END, ("\n"+msg2+ot5+ot6+"\n"+msg3+ot7+ot8))
        for t in range(len(listapros)):
            if a == listapros[t]:
                indicemenu = listapros.index(listapros[t])
                indiceexcelb = txtb[indicemenu+12]
                indiceexcelc = txtc[indicemenu+12]
                numsb=re.sub("\D", "", indiceexcelb)
                numsc=re.sub("\D", "", indiceexcelc)
                if numsb == numsc:
                    mes="El producto {0} ".format(b)
                    mes2=" es igual de saludable al "
                    mes3="producto {0}.".format(c)
                    mes4="Con respecto a: {0}".format(a)
                    texto.insert(tk.END,
                                 (mes+mes2+mes3+"\n"+mes4))
                
                elif max(numsb, numsc)== numsb:
                    msg="El producto más saludable con respecto a "+a
                    ot=", es: {0}".format(b)
                    ot2="\n" + "Con: {0}".format(indiceexcelb)
                    msg1="El producto menos saludable con respecto a "+a
                    ot3=", es: {0}".format(c)
                    ot4="\n" + "Con: {0}".format(indiceexcelc)
                    texto.insert(tk.END, (msg+ot+ot2+"\n"+msg1+ot3+ot4))
                elif max(numsb, numsc)== numsc:
                    msg2="El producto más saludable con respecto a "+a
                    ot5=", es: {0}".format(c)
                    ot6="\n" + "Con: {0}".format(indiceexcelc)
                    msg3="El producto menos saludable con respecto a "+a
                    ot7=", es: {0}".format(b)
                    ot8="\n" + "Con: {0}".format(indiceexcelb)
                    texto.insert(tk.END, ("\n"+msg2+ot5+ot6+"\n"+msg3+ot7+ot8))
        window.mainloop()
        return window


    
    #---Entradas de productos---
    
    lb3 = tk.Label(wn, text="Producto 1",
                      font=("Malgun Gothic Semilight", 11))
    lb3.grid(column=0, row=7, padx=30, pady=10, sticky="W")

    lb4 = tk.Label(wn, text="Producto 2",
                      font=("Malgun Gothic Semilight", 11))
    lb4.grid(column=0, row=7, padx=250, pady=10,sticky="W")

    lb5 = tk.Label(wn, text="Por favor indique cuáles datos desea comparar",
                      font=("Malgun Gothic Semilight", 13))
    lb5.grid(column=0, row=8, padx=30, sticky="W")
    lb6 = tk.Label(wn, text="Por favor ingrese los nombres de los productos",
                      font=("Malgun Gothic Semilight", 13))
    lb6.grid(column=0, row=6, padx=30, sticky="W")
    
    
    #---Entrada de texto---
    entry1 = tk.Entry(master=wn)
    entry1.grid(column=0, row=7, padx=110, pady=10, sticky="W")
    
    entry2 = tk.Entry(master=wn)
    entry2.grid(column=0, row=7, padx=330, pady=10,sticky="W")
    #---Optionmenu para elegir característica---
    variables =["Peso Neto", "Tamaño por porción", "Calorías", "Calorías de grasa",
                "Grasa Saturada",  "Grasas Trans", "Colesterol", "Sodio", "Azúcares",
                "Fibra","Proteína", "Vitamina A", "Vitamina C", "Vitamina D",
                "Vitamina E","Calcio", "Hierro"]
    
    selección = tk.StringVar()
    selección.set("Seleccione una opción")

    om = tk.OptionMenu(wn, selección,  *variables)
    om.grid(column=0, row=9, padx=150, sticky="W")

    #---Boton---
    but1=tk.Button(master=wn, text="Buscar información",
                   command=lambda:comparedist(selección, entry1,
                                              entry2,variables))
    but1.grid(column=0, row=18, pady= 20,sticky="W")
            
def Comparar_wn():

    """Esta función crea la ventana que permite comparar productos,
        se activa al dar cick en: 'Comparar Producto' """
    #---Ventana 'Comparar Producto'----
    otherwn = tk.Tk()
    otherwn.title("Comparar Producto")
    otherwn.geometry("500x470")
    #---Etiqueta principal---
    mainlb = tk.Label(otherwn, text="En esta ventana puede comparar dos productos",
                      font=("Malgun Gothic Semilight", 13))
    mainlb.grid(column=0, row=0,sticky="W")

    #---Otras etiquetas---
    lb2 = tk.Label(otherwn, text="Por favor indique qué desea comparar",
                   font=("Malgun Gothic Semilight", 13))
    lb2.grid(column=0, row=1, padx=30,sticky="W")


    #---Boton comparar---
    but2=tk.Button(master=otherwn, text="Mismo producto con diferente marca",
                   font=("Malgun Gothic Semilight", 10),
                   command=lambda:unico(otherwn))
    but2.grid(column=0, row=4, padx= 50, pady= 10, sticky="W")

    but3=tk.Button(master=otherwn, text="Distintos productos de diferentes marcas",
                   font=("Malgun Gothic Semilight", 10),
                   command=lambda:distintos(otherwn))
    but3.grid(column=0, row=5, padx= 50,pady= 10, sticky="W")

    otherwn.mainloop()

    return otherwn
