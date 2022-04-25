import os
import csv
import tkinter
from tkinter import filedialog, ttk, messagebox
from wsgiref.validate import PartialIteratorWrapper

# --------------------------------------------------------- XML --------------------------------------------------------


def leerCSV():
    with open('entrada.csv', encoding='utf-8') as file:
        global partidos
        partidos = []
        partido = csv.DictReader(file)
        for row in partido:
            partidos.append(row)
        
        print (partidos)
        print("\t")


ventana = tkinter.Tk()
ventana.title("LA LIGA BOT")
ventana.geometry("1100x700")
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Frames ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
frame = tkinter.Frame(ventana)
# Establece la posición del componente
frame.place(x=20, y=10)
# Color de fondo, background
frame.config(bg="lightgrey")
# Podemos establecer un tamaño
frame.config(width=750, height=653)
# Establece el ancho del borde
frame.config(bd=10)
# Establece el tipo de relieve para el borde
frame.config(relief="ridge")


frameIm = tkinter.Frame(frame)
# Establece la posición del componente
frameIm.place(x=10, y=10)
# Color de fondo, background
frameIm.config(bg="white")
# Podemos establecer un tamaño
frameIm.config(width=710, height=550)
# Establece el ancho del borde
frameIm.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm.config(relief="ridge")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Buttons --------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


def hola():
    print("Hola Mundo")
boton1 = tkinter.Button(ventana, text="Reporte de errores", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton1.place(x=790, y=10)
boton1.config(width=20, height=1)
boton1.config(bd=10)
boton1.config(relief="ridge")


boton2 = tkinter.Button(ventana, text="Limpiar Log de errores", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton2.place(x=790, y=70)
boton2.config(width=20, height=1)
boton2.config(bd=10)
boton2.config(relief="ridge")


boton3 = tkinter.Button(ventana, text="Reporte de tokens", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton3.place(x=790, y=130)
boton3.config(width=20, height=1)
boton3.config(bd=10)
boton3.config(relief="ridge")

boton4 = tkinter.Button(ventana, text="Limpiar log de tokens", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton4.place(x=790, y=190)
boton4.config(width=20, height=1)
boton4.config(bd=10)
boton4.config(relief="ridge")

boton5 = tkinter.Button(ventana, text="Manual de usuario", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton5.place(x=790, y=250)
boton5.config(width=20, height=1)
boton5.config(bd=10)
boton5.config(relief="ridge")

boton6 = tkinter.Button(ventana, text="Manual de tecnico", fg="black", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="lightgrey")
boton6.place(x=790, y=310)
boton6.config(width=20, height=1)
boton6.config(bd=10)
boton6.config(relief="ridge")

boton7 = tkinter.Button(ventana, text="Enviar", fg="black", font=(
    "broadway 12 bold"), command=leerCSV, borderwidth=0, bg="lightgrey")
boton7.place(x=790, y=600)
boton7.config(width=20, height=1)
boton7.config(bd=10)
boton7.config(relief="ridge")


busqueda = tkinter.StringVar()
txtA = tkinter.Entry(frame, textvariable=busqueda, font=(
    "broadway 16 bold"), borderwidth=0, bg="white")
txtA.place(x=10,y=580)
txtA.config(width=46)
txtA.config(bd=10)
txtA.config(relief="ridge")
    




# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- Entry ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

ventana.config(cursor="arrow")
ventana.config(bg="grey")
ventana.config(bd=15)
ventana.config(relief="ridge")
ventana.mainloop()
