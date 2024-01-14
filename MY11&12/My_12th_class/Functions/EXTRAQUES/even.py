# We require list of even numbers in output from given list
n = int(input("Enter the length of list"))
my_list=[]
for i in range(n):
    number = int(input("Enter number in list"))
    my_list.append(number)
    
def print_even(listt):
    list=[]
    for num in listt:
        if num % 2 == 0 :
            list.append(num)
    
    print("list of even numbers is" , list)
    
print_even(my_list)        


            
        




    
            




# def print_even(list):
    
#     new_list = []
#     def find_even(num):
#         if num % 2 == 0:
            
    
    
    
#     for num in list:
#         if find_even(num)
    



# print_even(mylist)
    