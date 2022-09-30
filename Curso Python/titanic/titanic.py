import matplotlib.pyplot as plt

#funcion para ver si es numero o no
def es_numero(cadena):
    try: 
        int(cadena)
        return True
    except ValueError:
        return False
#funcion para ver si la celda esta vacia o no
def es_vacio(cadena):
    try: 
        if cadena != '':
            return True
    except ValueError:
        return False


#abro el archivo
nombre_archivo=input("Ingrese el nombre del archivo: ")
fhand=open(nombre_archivo + ".csv","rt")

cadena=list()
edades=list()

for oracion in fhand:
    """
    if oracion.split(";")[5]!="":
        if(es_numero(oracion.split(";")[5])):
            print(int(float(oracion.split(";")[5])))
    """
    if es_numero(oracion.split(';')[0]):

        if es_vacio(oracion.split(';')[5]):
            edades.append(int(float(oracion.split(';')[5])))
        else:
            continue
    else: continue

fhand.close()
plt.title('Cantidad de muertes por edad')
plt.hist(edades,bins=30,color='red',edgecolor='black')
plt.xlabel("Edad")
plt.ylabel("Cantidad")
plt.grid(ls="dashed",color="#DDDDDD")
plt.show()