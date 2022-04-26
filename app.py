import csv
import tkinter
from wsgiref.validate import PartialIteratorWrapper
import re

# --------------------------------------------------------- CSV --------------------------------------------------------

with open('LaLigaBot-LFP.csv', encoding='utf-8') as file:
        global partidos,tokn, error
        tokn = []
        error = []
        partidos = []
        partido = csv.DictReader(file)
        for row in partido:
            partidos.append(row)
        

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------- Analizador ----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

#RESULTADO “Real Madrid” VS “Villarreal” TEMPORADA <2019-2020>
#JORNADA 12 TEMPORADA <2019-2020>
#JORNADA 1 TEMPORADA <1996-1997> -f jornada1Reporte
#GOLES TOTAL “Valencia” TEMPORADA <1998-1999>
#TABLA TEMPORADA <2018-2019>
#TABLA TEMPORADA <1996-1997> -f reporteGlobal1
#PARTIDOS “Real Madrid” TEMPORADA <1999-2000> -ji 1 -jf 18
#PARTIDOS “Español” TEMPORADA <1999-2000> -f reporteEspano
#TOP SUPERIOR TEMPORADA <2000-2001>
#TOP INFERIOR TEMPORADA <1999-2000> -n 3

def get_value():
    
    text_user = txtA.get()

    text.configure(state='normal')
    text.insert(tkinter.END, "Usuario:\n"+text_user+"\n\n")
    text.configure(state='disabled')

    global lexema, columna
    lexema = []
    columna = 1
    temp = ""
    temp_min = ""
    equipo = ""
    tempo = ""
    jornada = ""
    chatval = True
    resultadoval = False
    comillaval = False
    jornadaval = False
    golesval = False
    tablaval = False
    partidosval = False
    topval = False
    tempoval = False 
    esp_jornada = False
    esp_temp = False
    for letra in text_user:
        if letra == "\n":
            fila += 1
            columna = 1
        elif letra == "\t":
            fila += 5
        else:
            columna += 1           

        if letra == "\n":
            ""
        elif letra == "\t" :
            ""
        elif chatval == True:
            temp += letra 
            temp_min += letra.upper()
            if temp_min == "RESULTADO":
                resultadoval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp)
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            elif temp_min == "JORNADA":
                jornadaval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp) 
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            elif temp_min == "GOLES":
                golesval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp) 
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            elif temp_min == "TABLA":
                tablaval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp) 
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            elif temp_min == "PARTIDOS":
                partidosval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp) 
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            elif temp_min == "TOP":
                topval = True
                tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp) 
                lexema.append(temp)
                chatval = False 
                temp = ""
                temp_min = ""
            else:
                if letra == "“":
                    errortemp = "Error lexico: ' "+ temp +" ' se esperaria palabra reservada col. "+str(columna)
                    error.append(errortemp) 
                    temp = "" 
                    chatval = False    
                    break   
                elif letra == " ":   
                    tokentemp = "Token separacion encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    temp = ""               
                    chatval = False 
        elif resultadoval == True:      
            if letra == " ":
                if comillaval == False:
                    ""
                else:
                    equipo += letra 
            elif letra == "“": 
                tokentemp = "Token contenedor cadena: ' "+letra+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp)   
                comillaval = True
            elif letra == "”":                
                comillaval = False              
                                
                if not equipo:
                    errortemp = "Error lexico cadena vacia, se esperaria informacion,  col. "+str(columna)
                    error.append(errortemp)  
                else:
                    tokentemp = "Token cadena: ' "+equipo+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    lexema.append(equipo)
                    equipo = ""                 

                tokentemp = "Token contenedor cadena: ' "+letra+" ' encontrado en col. "+str(columna)
                tokn.append(tokentemp)   

            elif comillaval == True:
                equipo += letra 

            elif comillaval == False:
                
                if letra == "<":
                    tokentemp = "Token contenedor temporada: ' "+letra+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    tempoval = True
                elif letra == ">":

                    tokentemp = "Token temporada:' "+tempo+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    lexema.append(tempo)
                    tempo = ""

                    tokentemp = "Token contenedor temporada: ' "+letra+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    tempoval = False

                elif tempoval == False:
                    temp += letra
                    temp_min += letra.upper()
                    if temp_min == "VS":
                        tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                        tokn.append(tokentemp) 
                        lexema.append(temp)
                        temp = ""
                        temp_min = ""
                    elif temp_min == "TEMPORADA":
                        tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                        tokn.append(tokentemp) 
                        lexema.append(temp)
                        temp = ""
                        temp_min = ""
                elif tempoval == True:                       
                    tempo += letra
        elif jornadaval == True:
            if letra == " " and esp_jornada == False and esp_temp == False:
                esp_jornada = True
            
            if esp_jornada == True:
                if letra != " ":
                    jornada += letra
                else:
                    if jornada.isnumeric() == True:
                        tokentemp = "Token jornada: ' "+jornada+" ' encontrado en col. "+str(columna)
                        tokn.append(tokentemp) 
                        lexema.append(jornada) 
                        esp_jornada = False
                        esp_temp = True
                        
                    else:
                        errortemp = "Error lexico se esperarian numeros,  col. "+str(columna)
                        error.append(errortemp)

            elif esp_temp == True:
                if letra == "<":
                    tokentemp = "Token contenedor temporada: ' "+letra+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    tempoval = True

                elif letra == ">":
                    tokentemp = "Token temporada:' "+tempo+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    lexema.append(tempo)
                    tempo = ""

                    tokentemp = "Token contenedor temporada: ' "+letra+" ' encontrado en col. "+str(columna)
                    tokn.append(tokentemp) 
                    tempoval = False

                elif tempoval == False:
                    temp += letra
                    temp_min += letra.upper()
                    if temp_min == "TEMPORADA":
                        tokentemp = "Token palabra reservada: ' "+temp+" ' encontrado en col. "+str(columna)
                        tokn.append(tokentemp) 
                        lexema.append(temp)
                        temp = ""
                        temp_min = ""

                elif tempoval == True:                       
                    tempo += letra

                    

            
            



        elif golesval == True:
            ""
        elif tablaval == True:
            ""
        elif partidosval == True:
            ""
        elif topval == True:
            ""

    resp_txt(lexema)
    sintactico(lexema)



def sintactico(lexema):
    equipo1 = []
    equipo2 = []
    resultado = []
    respuesta = ""
    partidos
    for lista in range(len(lexema)):     
        if lexema[0] == "RESULTADO":
            equipo1 = list(filter(lambda item: item['Equipo1'] == lexema[1], partidos))             
            if bool(equipo1) == False:
                respuesta = "El equipo local especificado no exciste.\n\n"
                resp_txt(respuesta)
                break
            if lexema[2] == "VS":
                equipo2 = list(filter(lambda item: item['Equipo2'] == lexema[3], equipo1))
                if bool(equipo2) == False:
                    respuesta = "El equipo visitante especificado no exciste.\n\n"
                    resp_txt(respuesta)
                    break
                if lexema[4] == "TEMPORADA":
                    resultado = list(filter(lambda item: item['Temporada'] == lexema[5], equipo2))
                    if bool(resultado) == False:
                        respuesta = "La temporada especificada no exciste.\n\n"
                        resp_txt(respuesta)
                        break
                    respuesta = "El Bicho bot:\n El resultado de este partido fue: "+lexema[1]+" "+resultado[0]["Goles1"]+" - "+lexema[3]+" "+resultado[0]["Goles2"]+"\n\n"

                    resp_txt(respuesta)
                    break
                else:
                    errortemp = "Error sintactico: "+ lexema[4]  +" no es reconocido por este lenguaje col. "+str(columna)
                    error.append(errortemp)
                    respuesta = "Error sintactico: "+ lexema[4]  +" no es reconocido por este lenguaje col. "+str(columna)+"\n\n"
                    resp_txt(respuesta)
                    break
            else:
                errortemp = "Error sintactico: "+ lexema[2]  +" no es reconocido por este lenguaje col. "+str(columna)
                error.append(errortemp)
                respuesta = "Error sintactico: "+ lexema[2]  +" no es reconocido por este lenguaje col. "+str(columna)+"\n\n"
                resp_txt(respuesta)
                break
                
        elif lexema[0] == "JORNADA":
            ""
        elif lexema[0] == "GOLES":
            ""
        elif lexema[0] == "TABLA":
            ""
        elif lexema[0] == "PARTIDOS":
            ""
        elif lexema[0] == "TOP":
            ""
        else:
            errortemp = "Error sintactico: "+ lexema[0]  +" no es reconocido por este lenguaje col. "+str(columna)
            error.append(errortemp) 
            respuesta = "Error sintactico: "+ lexema[0]  +" no es reconocido por este lenguaje col. "+str(columna)+"\n\n"
            resp_txt(respuesta)
            break

def resp_txt(R):
    text.configure(state='normal')
    text.insert(tkinter.END, R)
    text.configure(state='disabled')

def carga(artemp):    
    text.insert(tkinter.END, artemp)

def recarga(artemp):
    text.insert(tkinter.END, artemp)


def analizar():
    data = text.get(1.0, "end-1c")           

def log_errores():
    error.clear() 

def log_token():
    tokn.clear()       

            
def lista():
    print(tokn)
    print(lexema)
    text.configure(state='normal')
    text.insert("1.0", lexema)
    text.configure(state='disabled')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- Interfaz Gráfica ----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

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
    "broadway 12 bold"), command=lista, borderwidth=0, bg="lightgrey")
boton1.place(x=790, y=10)
boton1.config(width=20, height=1)
boton1.config(bd=10)
boton1.config(relief="ridge")


boton2 = tkinter.Button(ventana, text="Limpiar Log de errores", fg="black", font=(
    "broadway 12 bold"), command=log_errores, borderwidth=0, bg="lightgrey")
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
    "broadway 12 bold"), command=log_token, borderwidth=0, bg="lightgrey")
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
    "broadway 12 bold"), command=get_value, borderwidth=0, bg="lightgrey")
boton7.place(x=790, y=600)
boton7.config(width=20, height=1)
boton7.config(bd=10)
boton7.config(relief="ridge")


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ TextArea --------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

global text
scroll = tkinter.Scrollbar(frameIm)
text = tkinter.Text(frameIm, height = 35,width =74, font=(
    "broadway 10 bold"))
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
text.config(yscrollcommand=scroll.set)


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- Entry ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

busqueda = tkinter.StringVar()
txtA = tkinter.Entry(frame, textvariable=busqueda, font=(
    "broadway 16 bold"), borderwidth=0, bg="white")
txtA.place(x=10,y=580)
txtA.config(width=46)
txtA.config(bd=10)
txtA.config(relief="ridge")       


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Config Ventana -----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

ventana.config(cursor="arrow")
ventana.config(bg="grey")
ventana.config(bd=15)
ventana.config(relief="ridge")
ventana.mainloop()

