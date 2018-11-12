#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 11 2018

@author: Sara Palacios
"""
import tkinter as tk
from Analizar_Producto import Analizar_wn



#---Ventana principal----
main = tk.Tk()
main.title("Nutridata")
main.geometry("510x200")



    
def Comparar_productos():
    """Esta función crea la ventana que permite comparar productos,
        se activa al dar cick en: 'Comparar productos' """
    otherwn = tk.Tk()
    otherwn.title("Comparar Productos")
    otherwn.geometry("500x200")
    
    return otherwn

def Agregar_productos():
    """Esta función crea la ventana que permite agregar un nuevo producto,
        se activa al dar cick en: 'Agregar Producto' """
    oother = tk.Tk()
    oother.title("Agregar Producto")
    oother.geometry("500x200")
    
    return oother


#---Etiquetas---
mainlb = tk.Label(text="Bienvenido a nutridata", font=("Malgun Gothic Semilight", 10))
mainlb.grid(column=0, row=0)
seclb = tk.Label(text="¿Qué desea hacer?", font=("Malgun Gothic Semilight", 15))
seclb.grid(column=1, row=3)



#---Botones---
bot1 = tk.Button(text="Analizar Producto", command=Analizar_wn)
bot1.grid(column=0, row=5, padx=20, pady=20)


bot2 = tk.Button(text="Comparar Productos", command=Comparar_productos)
bot2.grid(column=1, row=5, padx=40, pady=20)


bot3 = tk.Button(text="Agregar Producto", command=Agregar_productos)
bot3.grid(column=4, row=5, padx=40, pady=10)





main.mainloop()

