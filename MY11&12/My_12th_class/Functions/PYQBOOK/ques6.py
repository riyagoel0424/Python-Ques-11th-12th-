#### LIST MEIN NTH NUMBER SE PURI LIST ROTATE KRNI HAI TO 

num = int(input("Enter the length of list "))
my_list=[]
for i in range(num):
    number = int(input("Enter number in list "))
    my_list.append(number)
print(my_list)
    

def LShift():
    n = int(input("Enter the number from which rotate "))
    X = my_list[n:] + my_list[:n]
    print(X)  

LShift()
  