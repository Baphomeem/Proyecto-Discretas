Saskiel
saskiel_
Invisible

Saskiel — 20/07/2025 16:40
m!p rara bien
Jockie Music (1)
APP
 — 20/07/2025 16:40
Did you know you now get better audio quality with any premium tier https://www.patreon.com/Jockie!
:deezer: ​ Started playing Rara Bien by Rupatrupa
Saskiel — 20/07/2025 16:44
Expansión de Expresiones Algebraicas Usando Python y LaTeX
Jockie Music (1)
APP
 — 20/07/2025 16:46
There are no more tracks
No tracks have been playing for the past 3 minutes, leaving :wave:

This can be disabled by using the premium command 24/7, for more information check out the perks command!
IsabelSepulveda — 20/07/2025 17:18
Tipo de archivo adjunto: document
Proyecto_discretas.docx
29.84 KB
Saskiel — 20/07/2025 17:23
Tipo de archivo adjunto: document
Informe - P4 (1).docx
38.45 KB
Saskiel — ayer a las 21:11
m!p colmillo tainy
Jockie Music (1)
APP
 — ayer a las 21:11
:deezer: ​ Started playing COLMILLO by Tainy
There are no more tracks
:spotify: ​ Started playing Bien Loco by Nova y Jory
Jockie Music (1)
APP
 — ayer a las 21:19
:spotify: ​ Started playing Pa' Que La Pases Bien by Arcángel
Did you know you now get better audio quality with any premium tier https://www.patreon.com/Jockie!
:spotify: ​ Started playing Mírala Bien by Wisin & Yandel
:spotify: ​ Started playing Dile a Tu Amiga by Dalmata
Jockie Music (1)
APP
 — ayer a las 21:29
:spotify: ​ Started playing Regalame Una Noche by J Alvarez
:spotify: ​ Started playing Rakata by Wisin & Yandel
Jockie Music (1)
APP
 — ayer a las 21:36
:spotify: ​ Started playing Hay Algo en Ti by Luny Tunes
:spotify: ​ Started playing Cazador (feat. Ñengo Flow) by Nova y Jory
Saskiel — ayer a las 21:42
Imagen
Jockie Music (1)
APP
 — ayer a las 21:44
:spotify: ​ Started playing Candy by Plan B
IsabelSepulveda — ayer a las 21:47
#Importe de la libreria tkinter para implementacion de la interfaz
import tkinter as tk

#Toma la entrada y reescribe los simbolos ( ) {} $ +- y -
def limpiar_entrada(f):
    f = f.replace(" ", "").replace("-", "+-")
Expandir
Polinomios_interfaz.py
6 KB
Jockie Music (1)
APP
 — ayer a las 21:48
:spotify: ​ Started playing Gata Fiera (feat. Joan) by Trebol Clan
:spotify: ​ Started playing Punto y Aparte by Tego Calderón
:spotify: ​ Started playing Dale Don Dale by Don Omar
Jockie Music (1)
APP
 — ayer a las 21:58
:spotify: ​ Started playing Nadie Como Tu by Wisin & Yandel
esmo — ayer a las 22:00
m!s
Jockie Music (1)
APP
 — ayer a las 22:00
Skipping, 1/4 (3 votes required)
esmo — ayer a las 22:00
tf
Jockie Music (1)
APP
 — ayer a las 22:02
:spotify: ​ Started playing Mi Noche by Reykon
:spotify: ​ Started playing Guatauba by Plan B
:spotify: ​ Started playing Te Imagino by Alberto Stylee
Jockie Music (1)
APP
 — ayer a las 22:12
:spotify: ​ Started playing No Es Culpa Mía by Daddy Yankee
:spotify: ​ Started playing Te la Tiro Pa Que Bailes by Dj Joe
Saskiel — ayer a las 22:15
m!skip
Jockie Music (1)
APP
 — ayer a las 22:15
Te la Tiro Pa Que Bailes by Dj Joe has been skipped by @Saskiel (requester privilege)
Jockie Music (1)
APP
 — ayer a las 22:15
:spotify: ​ Started playing Sólo Pasajero by Luigi 21 Plus
:spotify: ​ Started playing Cuando Me Dirá by Ñengo Flow
:spotify: ​ Started playing Acechándote by Yaga & Mackie
Jockie Music (1)
APP
 — ayer a las 22:25
:spotify: ​ Started playing Shorty by Casa De Leones
:spotify: ​ Started playing Cositas Que Haciamos (feat. Farruko) by Musicologo Y Menes
Jockie Music (1)
APP
 — ayer a las 22:33
:spotify: ​ Started playing Señal De Vida by Ñejo & Dalmata
Xephblade — ayer a las 22:34
@saskiel
@Saskiel
juanes
venga q es jodiendo
Jockie Music (1)
APP
 — ayer a las 22:37
:spotify: ​ Started playing Matador - Official Remix by Nova y Jory
:spotify: ​ Started playing Escápate Conmigo - Remix by Wolfine
Jockie Music (1)
APP
 — ayer a las 22:44
:spotify: ​ Started playing Gata Oficial by Luigi 21 Plus
:spotify: ​ Started playing Salió El Sol by Don Omar
No one has been listening for the past 3 minutes, leaving :wave:

This can be disabled by using the premium command 24/7, for more information check out the perks command!
IsabelSepulveda — 19:55
#Importe de la libreria tkinter para implementacion de la interfaz
import tkinter as tk

#Toma la entrada y reescribe los simbolos ( ) {} $ +- y -
def limpiar_entrada(f):
    while ")^{" in f:
Expandir
Main.py
7 KB
﻿
#Importe de la libreria tkinter para implementacion de la interfaz
import tkinter as tk

#Toma la entrada y reescribe los simbolos ( ) {} $ +- y -
def limpiar_entrada(f):
    while ")^{" in f:
        pos_f = f.find(")^{")
        exp_f = f[pos_f+3:]
        exp_f = exp_f[:exp_f.find("}")]
        factor_f = f[pos_f-1::-1]
        factor_f = "(" + factor_f[:factor_f.find("(")] + ")"
        factor_f = factor_f[::-1]
        f = f[:pos_f+1] + f[pos_f+4+len(exp_f):] + factor_f*(int(exp_f)-1)
        
    f = f.replace(" ", "").replace("-", "+-")
    f = f.replace("{+-", "-").replace("$", "").replace("{", "").replace("}", "")
    f = f.replace("(", " ").replace(")", " ")
    return f.strip().split("  ")

# Separa los factores en cada termino, devolviendo cada factor en un arreglo de 2 elementos (cada termino)
def separar_terminos(factores):
    coeficientes = []
    for factor in factores:
        terminos = factor.split("+")
        coeficientes.append([t for t in terminos if t])
    return coeficientes

#Toma los terminos y determina los coeficientes y exponentes
def extraer_coeficientes_exponentes(terminos):
    coeficientes = []
    exponentes = []
    for factor in terminos:
        c_factor = []
        e_factor = []
        for termino in factor:
            if "x" in termino:
                pos = termino.index("x")
                coef_str = termino[:pos]
                coef = -1 if coef_str == "-" else (1 if coef_str == "" else int(coef_str))
                if "^" in termino:
                    exp = int(termino.split("^")[1])
                else:
                    exp = 1
            else:
                coef = int(termino)
                exp = 0
            c_factor.append(coef)
            e_factor.append(exp)
        coeficientes.append(c_factor)
        exponentes.append(e_factor)
    return coeficientes, exponentes

#determina el valor de lso terminos que componen el polinomio y sus exponentes
def multiplicar_polinomios(coeficientes, exponentes):
    while len(coeficientes) >= 2:
        a, b = coeficientes[0], coeficientes[1]
        c, d = exponentes[0], exponentes[1]
        productoC = [a[i]*b[j] for i in range(len(a)) for j in range(len(b))]
        sumaE = [c[i]+d[j] for i in range(len(c)) for j in range(len(d))]
        coeficientes = [productoC] + coeficientes[2:]
        exponentes = [sumaE] + exponentes[2:]
    return coeficientes[0], exponentes[0]

#suma terminos cuyo grado sea el mismo
def sumar_terminos_semejantes(coeficientes, exponentes):
    i = 0
    while i < len(exponentes):
        j = i + 1
        while j < len(exponentes):
            if coeficientes[i] == 0:
                coeficientes.pop(i)
                exponentes.pop(i)
                j = i + 1
            elif exponentes[i] == exponentes[j]:
                coeficientes[i] += coeficientes[j]
                coeficientes.pop(j)
                exponentes.pop(j)
                j = i + 1
            else:
                j += 1
        i += 1
    return coeficientes, exponentes

#ordena los terminos de mayor a menor grado
def ordenar(coeficientes, exponentes):
    pares = sorted(zip(exponentes, coeficientes), reverse=True)
    exp_ordenado, coef_ordenado = zip(*pares)
    return list(coef_ordenado), list(exp_ordenado)

def formato_LaTex(coef, exp):
    pol = []
    for c, e in zip(coef, exp):
        termino = ""
        if e == 0 or c != 1:
            termino += str(c)
        if e != 0:
            termino += 'x'
        if e > 1:
            termino += f'^{{{e}}}'
        pol.append(termino)
    return '$' + ' + '.join(pol).replace(' + -', ' - ') + '$'

#toma la entrada ingresada por el usuario y determina factores terminos y coeficientes con las otras funciones
def procesar_entrada():
    f = polinomio.get()
    factores = limpiar_entrada(f)
    terminos = separar_terminos(factores)
    coeficientes, exponentes = extraer_coeficientes_exponentes(terminos)
    coef_final, exp_final = multiplicar_polinomios(coeficientes, exponentes)
    coef_final, exp_final = sumar_terminos_semejantes(coef_final, exp_final)
    coef_final, exp_final = ordenar(coef_final, exp_final)
    return formato_LaTex(coef_final, exp_final)

#ejecuta la funcion procesar entrada para obtener el resultado 
def ejecutar():
    procesado = procesar_entrada() 
    salida_resultado.config(state='normal')  # Permite editar temporalmente
    salida_resultado.delete("1.0", tk.END)
    salida_resultado.insert(tk.END, procesado)
    salida_resultado.config(state='disabled')  # Bloquea edición después

def copiar_resultado():
    texto = salida_resultado.get("1.0", tk.END).strip()
    wind.clipboard_clear()
    wind.clipboard_append(texto)
    
#IMPLEMENTACION DE LA INTERFAZ GRAFICA

#Creacion de la ventana principal y especificaciones 
wind = tk.Tk()
wind.geometry('600x300')
wind.configure(background="#f0f0f0")
wind.resizable(False,False)

tk.Wm.wm_title(wind,'Multiplicador de polinomios')

#Creacion de marco dentro de la ventana
frame1=tk.Frame(
    wind,
    bg="#f0f0f0",
)
frame1.pack(expand=True, fill='both')

frame = tk.Frame(frame1, bg="#f0f0f0")
frame.place(relx=0.5, rely=0.5, anchor='center')

#Etiqueta de texto con instruccion para el usuario
tk.Label(
    frame, 
    text="Ingrese el polinomio en LaTeX (Ej: $(x+1)(x+2)$):",
    bg="#f0f0f0",
    font=('times new roman', 18)
    
    ).pack(pady=10)

#creacion de entrada de texto
polinomio=tk.Entry(
    frame,
    width=40,
    font=('times new roman',14)
    )

polinomio.pack(pady=10)

#Boton de ejecucion del programa 
tk.Button(
    frame,
    text='Ejecutar',
    font=('times new roman', 12),
    bg="#81a3b0",
    #command= llamar funcion como objeto
    command=ejecutar).pack(pady=10)

resultado = tk.StringVar()


#Etiqueta de outpout del resultado
salida_resultado = tk.Text(
    frame,
    font=("times new roman", 14),
    bg="#ffffff",
    height=1,
    width=40,
    wrap='word'
)
salida_resultado.pack(pady=10)


tk.Button(
    frame,
    text='Copiar',
    font=('times new roman', 12),
    bg="#81a3b0",
    command=copiar_resultado
).pack(pady=5)


wind.mainloop()
