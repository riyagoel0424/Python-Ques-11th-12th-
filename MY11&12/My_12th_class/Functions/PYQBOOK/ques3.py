num = int(input("Enter the length of list"))
my_list=[]
for i in range(num):
    number = int(input("Enter number in list"))
    my_list.append(number)
print(my_list)


def AddOddEven():

    for i in my_list:
        Even = 0
        Odd = 0
        if i % 2 ==0:
            Even += i
        else:
            Odd += i
    print('SUM OF EVEN NUM' ,Even) 
    print('SUM OF ODD NUM',Odd)        
            
AddOddEven()
            