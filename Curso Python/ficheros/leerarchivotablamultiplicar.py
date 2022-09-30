#Escribir una función que pida un número entero entre 1 y 10, 
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# done n es el número introducido, y la muestre por pantalla. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
import os
numero=int(input("Ingrese un numero del 1 al 10:"))

if os.path.exists("Tabla-"+str(numero)+".txt"):
    archivo=open("Tabla-"+str(numero)+".txt","rt")
    for i in archivo:
        print(i)
else:
    print("El archivo Tabla-"+str(numero)+".txt no existe." )
