#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 11 2018

@author: Sara Palacios
"""
import tkinter as tk
from clase import *
from prueba import *



        
def Analizar_wn():
    """Esta función crea la ventana que permite analizar un producto,
        se activa al dar cick en: 'Analizar Producto' """
    #---Ventana 'Analizar producto'----
    newwn = tk.Tk()
    newwn.title("Analizar Producto")
    newwn.geometry("500x200")
    #---Etiquetas--
    lb1 = tk.Label(master=newwn, text="Aquí podrá encontrar la información de cuaquier producto",
                   font=("Malgun Gothic Semilight", 10))
    lb1.grid(column=0, row=0, padx=70)
    lb2 = tk.Label(master=newwn, text="Por favor ingrese el producto a evaluar",
                   font=("Malgun Gothic Semilight", 10))
    lb2.grid(column=0, row=1, pady=10)

    #---Entrada de texto---
    entry1 = tk.Entry(master=newwn)
    entry1.grid(column=0, row=3, pady=10)
    palabra = entry1.get()

    #--Botón para buscar--
    but1=tk.Button(master=newwn, text="Buscar",
                   command=mostrar_información(newwn, palabra))
    but1.grid(column=0, row=4, pady=10)

    
    
    
    newwn.mainloop()
    return newwn



def mostrar_información(wn, word):
    #no funciona aún
    """Función que muestra en un texto las características del producto
        ingresado"""
    datos = tk.Text(master=wn, height=10, width=30)
    datos.grid(column=0, row=5)
    libro = Excel("wb7.xlsx", "Hoja1")
    información = libro.read_wb(word)
    datos.insert(tk.END, información)
    

    


    
    

    
    
    


    
    




