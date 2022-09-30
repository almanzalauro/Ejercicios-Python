n = int(input())
arr = list(map(int, input().split()))    
for i in arr:
    a=i
    b=i
    if i>=a:
        b=a
        a=i
    else:
       continue  
print('El puntaje es: ',b)