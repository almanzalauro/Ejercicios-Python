#Escribir una función que pida un número entero entre 1 y 10 y
#guarde en un fichero con el nombre tabla-n.txt la tabla de 
#multiplicar de ese número, donde n es el número introducido.
import os

numero=int(input("Ingrese un numero del 1 al 10: "))
if  os.path.exists("tabla-"+str(numero)+".txt"):
       os.remove("tabla-"+str(numero)+".txt")
       print("El archivo ya existia y fue eliminado con exito.")
       


else:
    archivo=open("Tabla-"+str(numero)+".txt","xt")
    for i in range(1,11):
        archivo.write(str(i)+'x'+str(numero)+'='+str(i*numero)+'\n')
    archivo.close()

