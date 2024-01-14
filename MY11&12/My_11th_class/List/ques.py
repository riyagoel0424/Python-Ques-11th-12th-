l=eval(input('enter'))
l1=[]
for i in range(len(l)):
    if l[i]%2==0:
        l1.append(l[i]/2)
    else:
        l1.append(l[i]*2)
print(l1)