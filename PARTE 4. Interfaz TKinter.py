import tkinter as tk
from tkinter import ttk 
import pickle
import pandas as pd
import numpy as np
import random
import math
import pickle

## Nuestra función:
def PriceMyHome(m2,hab,baños,barrio): 
    barrios = pd.read_csv("Barrios.csv", index_col = 0)
    barrios = barrios.groupby("Barrios").first()
    A = np.array(barrios.loc[barrio,:]).tolist()
    B = [m2,hab,baños]+A
    B = np.array(B).reshape(1,45)
    pkl_filename= "Clasificador Random Forest.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
    Ypredict = pickle_model.predict(B)
    Clase = int(Ypredict)
    print("**********")
    print(Clase)
    print("**********")
    
    if Clase == 0:
        pkl_filename= "Gradient Boost_clase0.pkl"
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
        Predict_precio = pickle_model.predict(B)
    else:
        pkl_filename= "Gradient Boost_clase1.pkl"
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
        Predict_precio = pickle_model.predict(B)
    
    Precio_final = int(Predict_precio)
    Precio_baja = int(Precio_final * 0.83)
    Precio_alza = int(Precio_final * 1.17)
    return str(Precio_final)#(Precio_baja,Precio_final,Precio_alza)

col = ['m2', 'habitaciones', 'baños', 'barrios']



def boton_calcular():
	

	prediccion = PriceMyHome(int(m2.get()),int(hab.get()),int(baños.get()),barrio.get())
	resultado.set(prediccion)

## Diseño interfaz:
root = tk.Tk()
root.geometry('{}x{}'.format(620, 620))
root.config()
resultado = tk.StringVar(root)

frame0 = tk.LabelFrame(root, bd = 0, relief = tk.RIDGE)
frame0.pack()

tk.Label(frame0, font=('Calibri', 12,'bold'), text = 'Clasificador ').grid(row = 0, column = 0,sticky=tk.W)


tk.Label(frame0, font=('Calibri', 12), text = col[0], justify=tk.RIGHT).grid(row = 1, column = 0)
m2 = tk.Entry(frame0, font = ('Calibri', 12), width=17)
m2.focus()
m2.grid(row = 1, column = 1)

tk.Label(frame0, font=('Calibri', 12), text = col[1], justify=tk.RIGHT).grid(row = 2, column = 0)
hab = tk.Entry(frame0, font = ('Calibri', 12), width=17)
hab.focus()
hab.grid(row = 2, column = 1)

tk.Label(frame0, font=('Calibri', 12), text = col[2], justify=tk.RIGHT).grid(row = 3, column = 0)
baños = tk.Entry(frame0, font = ('Calibri', 12), width=17)
baños.focus()
baños.grid(row = 3, column = 1)

tk.Label(frame0, font=('Calibri', 12), text = col[3], justify=tk.RIGHT).grid(row = 4, column = 0)
barrio = tk.Entry(frame0, font = ('Calibri', 12), width=17)
barrio.focus()
barrio.grid(row = 4, column = 1)



## BOTON de Calcular 

frame5 = tk.LabelFrame(root, bd = 0, relief = tk.RIDGE)
frame5.pack()

button = tk.Button(frame5,padx = 20, pady=3, fg = "black", font = ('arial', 14, 'bold'), width = 4, text = "Calcular", command = boton_calcular)
button.grid(row = 6, column = 1)
ready = tk.Entry(frame5, font = ('arial', 14), width=17, textvariable= resultado)
ready.grid(row = 7, column = 1)   




root.mainloop()


