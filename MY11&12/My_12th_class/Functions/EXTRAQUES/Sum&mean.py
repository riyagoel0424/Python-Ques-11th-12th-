##### SUM AND MEAN OF NUMBERS IN A LIST 

n = int(input("Enter the length of list"))
my_list=[]
for i in range(n):
    number = int(input("Enter number in list"))
    my_list.append(number)
    
def SumMean():
    sum = 0
    for i in my_list:
        sum+=i
    print('SUM OF ELEMENTS IS ' , sum)
    print('MEAN OF ELEMENTS IS ' , sum/n)
    
SumMean()
    