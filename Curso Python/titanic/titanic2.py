#funcion control de clase




def es_numero(numero):
    try: 
        int(numero)
        return True
    except ValueError:
        return False

def control_clase(clase):
    contador1=0
    contador2=0
    contador3=0
    cantidades=list()

    for i in clase:
        if i==1:
            contador1=contador1 + 1
        elif i==2:
            contador2=contador2 + 1
        else:
            if i==3:
                contador3=contador3 + 1
    cantidades.append(contador1)
    cantidades.append(contador2)
    cantidades.append(contador3)
    return print(cantidades)

#5;0;3;Allen, Mr. William Henry;male;35;0;0;373450;8.05;;S
#----------------PROGRAMA---------------
import matplotlib.pyplot as plt
import numpy as np

nombre_archivo=input("Ingrese el nombre del archivo:")
archivo=open(nombre_archivo+".csv","rt")

milista=list()

#creo la lista con todas las clases que aparecen en el archivo 
for oracion in archivo:
    if es_numero(oracion.split(';')[2]):
        milista.append(int(oracion.split(';')[2]))
    else:continue



print(milista)

x=np.array(control_clase(milista))
y=["clase 1","clase 2", "clase 3"]
plt.bar(x,y)
plt.show()
archivo.close()
