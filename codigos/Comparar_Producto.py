#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on SAT Nov 24 2018
@author: Sara Palacios
"""
import tkinter as tk
from clase import *
from Agregar_Nuevo_p import entradas



"""Esta función crea la ventana que permite comparar productos,
    se activa al dar cick en: 'Comparar Producto' """
#---Ventana 'Analizar producto'----
otherwn = tk.Tk()
otherwn.title("Analizar Producto")
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

#---vars de CheckButtons---
peso=tk.IntVar()
tamaño=tk.IntVar()
cals=tk.IntVar()
calsgras=tk.IntVar()
grassat=tk.IntVar()
grastrans=tk.IntVar()
col=tk.IntVar()
sod=tk.IntVar()
fib=tk.IntVar()
azucar=tk.IntVar()
vita=tk.IntVar()
vitc=tk.IntVar()
vitd=tk.IntVar()
vite=tk.IntVar()
cal=tk.IntVar()
hierro=tk.IntVar()

#---Checkbuttons---
chkp=tk.Checkbutton(otherwn, text="Peso Neto", font=("Malgun Gothic Semilight", 10),
                    variable=peso, onvalue=1, offvalue=0)
chkp.grid(column=0, row=7, padx=50, sticky="W")
chkt=tk.Checkbutton(otherwn, text="Tamaño por porción", font=("Malgun Gothic Semilight", 10),
                    variable=tamaño, onvalue=1, offvalue=0)
chkt.grid(column=0, row=8, padx=50, sticky="W")
chkcals=tk.Checkbutton(otherwn, text="Calorías", font=("Malgun Gothic Semilight", 10),
                    variable=cals, onvalue=1, offvalue=0)
chkcals.grid(column=0, row=9,padx=50, sticky="W")
chkcg=tk.Checkbutton(otherwn, text="Calorías de grasa", font=("Malgun Gothic Semilight", 10),
                    variable=calsgras, onvalue=1, offvalue=0)
chkcg.grid(column=0, row=10, padx=50,sticky="W")
chkgs=tk.Checkbutton(otherwn, text="Grasa Saturada", font=("Malgun Gothic Semilight", 10),
                    variable=grassat, onvalue=1, offvalue=0)
chkgs.grid(column=0, row=11, padx=50,sticky="W")
chkgt=tk.Checkbutton(otherwn, text="Grasas Trans", font=("Malgun Gothic Semilight", 10),
                    variable=grastrans, onvalue=1, offvalue=0)
chkgt.grid(column=0, row=12, padx=50,sticky="W")
chkcol=tk.Checkbutton(otherwn, text="Colesterol", font=("Malgun Gothic Semilight", 10),
                    variable=col, onvalue=1, offvalue=0)
chkcol.grid(column=0, row=13,padx=50, sticky="W")
chksod=tk.Checkbutton(otherwn, text="Sodio", font=("Malgun Gothic Semilight", 10),
                    variable=sod, onvalue=1, offvalue=0)
chksod.grid(column=0, row=14,padx=50, sticky="W")

chkfib=tk.Checkbutton(otherwn, text="Fibra", font=("Malgun Gothic Semilight", 10),
                    variable=fib, onvalue=1, offvalue=0)
chkfib.grid(column=0, row=7, padx=250, sticky="W")
chkazuc=tk.Checkbutton(otherwn, text="Azúcares", font=("Malgun Gothic Semilight", 10),
                    variable=azucar, onvalue=1, offvalue=0)
chkazuc.grid(column=0, row=8, padx=250, sticky="W")
chkvita=tk.Checkbutton(otherwn, text="Vitamina A", font=("Malgun Gothic Semilight", 10),
                    variable=vita, onvalue=1, offvalue=0)
chkvita.grid(column=0, row=9, padx=250, sticky="W")
chkvitc=tk.Checkbutton(otherwn, text="Vitamina C", font=("Malgun Gothic Semilight", 10),
                    variable=vitc, onvalue=1, offvalue=0)
chkvitc.grid(column=0, row=10, padx=250, sticky="W")
chkvitd=tk.Checkbutton(otherwn, text="Vitamina D", font=("Malgun Gothic Semilight", 10),
                    variable=vitd, onvalue=1, offvalue=0)
chkvitd.grid(column=0, row=11, padx=250, sticky="W")
chkvite=tk.Checkbutton(otherwn, text="Vitamina E", font=("Malgun Gothic Semilight", 10),
                    variable=vite, onvalue=1, offvalue=0)
chkvite.grid(column=0, row=12, padx=250, sticky="W")
chkcalcio=tk.Checkbutton(otherwn, text="Calcio", font=("Malgun Gothic Semilight", 10),
                    variable=cal, onvalue=1, offvalue=0)
chkcalcio.grid(column=0, row=13, padx=250, sticky="W")
chkhierro=tk.Checkbutton(otherwn, text="Hierro", font=("Malgun Gothic Semilight", 10),
                    variable=hierro, onvalue=1, offvalue=0)
chkhierro.grid(column=0, row=14, padx=250, sticky="W" )



#--Botón para buscar--
but1=tk.Button(master=otherwn, text="Buscar información",
               command= lambda: asd(lista_checks))
but1.grid(column=0, row=18, padx=300, pady= 20,sticky="W")

lista_checks=[peso,tamaño,cals, calsgras, grassat, grastrans,
              col, sod, fib, azucar, vita, vitc, vitd,
              vite, cal, hierro]



otherwn.mainloop

def asd(lista):
    lst=entradas(lista)
    temp = []
    for i in range(len(lst)):
        c = lst.index(lst[i])
        print(c)
        
            
    


    
