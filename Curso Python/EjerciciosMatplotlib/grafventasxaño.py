#Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
#muestre por pantalla un diagrama de líneas con la evolución de las ventas.
import matplotlib.pyplot as plt
import matplotlib.figure as fig

import numpy as np

#defino las funciones a utilizar

def ingreso_datos(yearinitial,yearend):
    ventas={}
    for i in range(yearinitial,yearend+1):
        ventas[i]=(input("Ingrese las ventas en el año " +str(i)+ ': '))
    return grafica_datos(ventas)         

def grafica_datos(ventas):
    #plt.pie(ventas.values(),labels=ventas.keys())
    plt.plot(ventas.keys(),ventas.values())
    plt.title("VENTAS POR AÑO")
    plt.show()


#Defino el programa
print("A continuacion ingrese el año inicial y final a graficar:")

yearinitial=int(input("Año inicial: "))
yearend=int(input("Año final: "))

ingreso_datos(yearinitial,yearend)



