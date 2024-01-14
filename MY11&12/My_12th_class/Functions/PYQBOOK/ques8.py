#####  LIST LEKR USKE ELEMENTS KO DOUBLE KRKE REVERSE ORDER MEIN PRINT KRANA THA 

num = int(input("Enter the length of list"))
my_list=[]
for i in range(num):
    number = int(input("Enter number in list"))
    my_list.append(number)
print(my_list)

l = []
def REVERSE():
    for i in my_list:
        l.append(i*2)
    print(l[::-1])
    
REVERSE()


 