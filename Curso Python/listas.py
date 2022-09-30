#Numeros en comun en dos listas distintas

def sub_list(list_x,list_y):
    result = list()

    if len(list_x)<=len(list_y):    
       
        for i in list_x:
            if i in list_y:
                result.append(i)
            else:continue
        return result
    else: return result   
    

print(sub_list([1, 2, 7, 4, 5],[0, 2, 4, 6, 8, 10]))
