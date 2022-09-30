import pandas as pd
import matplotlib.pyplot as plt


def checkBarcelona(equipo):
    try: 
        equipo=="FC Barcelona"
        return True
    except ValueError:
        return False

def checkPSG(equipo):
    try: 
        equipo=="Paris Saint-Germain"
        return True
    except ValueError:
        return False

def control_equipo(equipo,goles):
    if checkBarcelona:
        goles=goles+1
        
    elif checkPSG:
        goles=goles+1
    return goles   
    
    

#encabezados:  Season-Competition-Matchday-Date-Venue-Club-Opponent-Result-Playing_Position-Minute-At_score-Type-Goal_assist

nomb_archivo=input("Ingrese el nombre del archivo: ")
with open(nomb_archivo+".csv","r") as archivo:

    equipos=dict()
    
    for linea in archivo:
        lista=linea.split(";")

        if lista[5]=="Club":
            continue

        elif lista[5] not in equipos:
            equipos[lista[5]]=1
        else:
            equipos[lista[5]] = control_equipo(lista[5],equipos[lista[5]])
        

    print(equipos)
    plt.bar(equipos.keys(),equipos.values(), color="#2753C0", edgecolor="#CD0000")
    plt.title("GOLES DE MESSI EN EQUIPOS")
    plt.show()
   