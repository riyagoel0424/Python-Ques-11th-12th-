def ch():
    for i in range(0,4):
        if L[i] % 2 == 0:
            L[i] = L[i]*2
        if L[i] % 3 == 0:
            L[i] = L[i]*3
        else:
            L[i] = L[i]*5
            
L =[2,6,9,10]
ch()
for i in L:
    print(i)


