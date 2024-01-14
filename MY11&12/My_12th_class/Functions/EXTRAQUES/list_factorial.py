######  FACTORIAL  OF NUMBER

# """fact = 1 
# num = int(input('Enter  num '))

# for i in range(1,num+1):
#     fact = fact*i
# print(fact)"""

#####  FACTORIAL  OF NUMBER IN LIST

L = []
n = int(input('Enter total elements '))

for i in range(0,n):
        num = int(input('enter element '))
        L.append(num)
print('old list',L)  



def change(L):
    l1 = []
    for i in L:
        fact = 1
        for k in range(1,i+1):
            fact = fact * k
        l1.append(fact)
        L = l1
    print(L)

change(L)



    
        