### SUM OF ODD NUMBERS IN A LIST 

num = int(input("Enter the length of list"))
my_list=[]
for i in range(num):
    number = int(input("Enter number in list"))
    my_list.append(number)
print(my_list)

def ODDSUM():
    sum = 0 
    for i in my_list:
        if i % 2 != 0:
            sum+= i
    print(sum)
            
ODDSUM()
        