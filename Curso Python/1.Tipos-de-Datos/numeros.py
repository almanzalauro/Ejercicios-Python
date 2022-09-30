import matplotlib.pyplot as plt
import numpy as np
#plt.title("Mi titulo", loc='right')
#plt.xlabel("ejeX")
#plt.ylabel("ejeY")
#plt.grid( axis='x',c='green',ls="--",lw=3.0)

#para el plot 1
myexplodes=[0.2,0,0]
datos=([10,33,4])
colores=["blue","red","gray"]
mylabels=["Toyota","Fiat","Audi"]
plt.pie(datos, explode=myexplodes, labels=mylabels,colors=colores)
plt.legend(title="Ventas en 2022")
plt.show()
