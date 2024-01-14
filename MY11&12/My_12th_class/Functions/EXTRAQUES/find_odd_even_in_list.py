# LIST KE ODD EVEN NUM ALG ALG LIST MEIN DAALNE HAI


L = []

n = int(input('Enter total elements'))

for i in range(0,n):
        num = int(input('enter element '))
        L.append(num)
print(L)

def listein(L):
     
    L_odd = []
    L_even = []

    for i in L:
        if i % 2 == 0:
            L_even.append(i)
        else:
            L_odd.append(i)
            
    print(L_even)
    print(L_odd)
    
listein(L)
    



      
