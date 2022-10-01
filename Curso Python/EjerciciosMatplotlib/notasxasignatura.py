#Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso y
#una cadena con el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.

import matplotlib.pyplot as plt

def ingreso_datos(notasxmateria):

    materia=input("Ingrese la materia: ")
    
    if materia in notasxmateria.keys():
            print("Esa materia ya fue ingresada.")
    else:
            nota=float(input(f"Ingrese la nota de {materia}: "))
            notasxmateria[materia]=nota

    return 






def graficador(notasxmateria,micolor):
    plt.bar(notasxmateria.keys(),notasxmateria.values(),color=micolor)
    plt.show()
#------------------------------------------------------------------     

print("GRAFICO NOTAS POR MATERIA")
notasxmateria={}
corte=1
micolor=input("Ingrese el color del grafico a mostrar: ")

while(corte!=0):
    ingreso_datos(notasxmateria)
    corte=int(input("Presione 1 para seguir ingresando materias / 0 para finalizar: "))

print(notasxmateria)
graficador(notasxmateria,micolor)