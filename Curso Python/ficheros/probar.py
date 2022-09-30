numlist=list()

while True:
    inp=input('Ingrese un numero: ')
    #si se ingresa 'done' termina el ciclo
    if inp =='done':break
    value = float(inp)
    numlist.append(value)

average=sum(numlist)/len(numlist)
print('average: ',average)