###### FREQUENCY OF ELEMENTS IN A LIST 

List = []
n = int(input('Enter total elements '))

for i in range(0,n):
        num = int(input('enter element '))
        List.append(num)
print('Original list',List)

def FREQUENCY():
    count =0
    num = int(input('enter number whose frequency is to be calculated'))
    for i in List:
        if i == num:
            count+=1
    print('Frequency is ' , count)
    
FREQUENCY()

        