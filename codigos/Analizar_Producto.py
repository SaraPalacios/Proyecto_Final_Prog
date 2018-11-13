#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 11 2018

@author: Sara Palacios
"""
import tkinter as tk
from clase import *
import random
#from prueba import *



        
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
                   command= lambda: mostrar_información(newwn, entry1.get()))
    but1.grid(column=0, row=4, pady=10)

    

    
    
    
    newwn.mainloop()
    return newwn


def phrase_generator(wn, entry):
    phrases = ["Hello", "what's up", "aloha", "Hafa Adai"]
    
    
    return phrases[random.randrange(0,3)] + entry


def mostrar_información(wn, word):
    
    """Función que muestra en un texto las características del producto
        ingresado"""
    
    window = tk.Tk()
    window.title("Información de producto")
    texto = tk.Text(master=window, height=10, width=70)
    texto.grid(column=0, row=1)
    libro = Excel("wb7.xlsx", "Hoja1")
    información = libro.read_wb(word)
    texto.insert(tk.END, información)
    
   




    


    
    

    
    
    


    
    




