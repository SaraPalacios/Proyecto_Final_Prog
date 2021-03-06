#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 11 2018

@author: Sara Palacios
"""
import tkinter as tk
from Analizar_Producto import Analizar_wn
from Agregar_Nuevo_p import Agregar_wn
from Comparar_Producto import Comparar_wn




#---Ventana principal----
main = tk.Tk()
main.title("Nutridata")
main.geometry("510x200")


#---Etiquetas---
mainlb = tk.Label(text="Bienvenido a nutridata", font=("Malgun Gothic Semilight", 10))
mainlb.grid(column=0, row=0)
seclb = tk.Label(text="¿Qué desea hacer?", font=("Malgun Gothic Semilight", 15))
seclb.grid(column=1, row=3)



#---Botones---
bot1 = tk.Button(text="Analizar Producto", command=Analizar_wn)
bot1.grid(column=0, row=5, padx=20, pady=20)


bot2 = tk.Button(text="Comparar Productos", command=Comparar_wn)
bot2.grid(column=1, row=5, padx=40, pady=20)


bot3 = tk.Button(text="Agregar Producto", command=Agregar_wn)
bot3.grid(column=4, row=5, padx=40, pady=10)





main.mainloop()

