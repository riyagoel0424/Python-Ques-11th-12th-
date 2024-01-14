###### EK LIST MEIN JO NUMBERS HAI UNKO USS LIST MEIN REPLACE KRO UNN NUMBERS KE DIGITS KE SUM SE 
######....LIKE 34 IN LIST REPLACE BY 7(3+4)

L = []
n = int(input('Enter total elements '))

for i in range(0,n):
        num = int(input('enter element '))
        L.append(num)
print('Original list',L)


def sum_of_digits(L):
    L2 =[]
    for i in L:
        count=0
        while i !=0:
            count += i%10
            i = i//10
        L2.append(count)
    L = L2
    print('New List', L)
        
sum_of_digits(L)   
     
       
