# Write a program to print the multiplication table of a given number using for loop.
num = int(input("Enter a number "))
for i in range(1,11):
    print(num , " X " , i , " = " , num*i)   # HERE WE CAN USE + ALSO INSTEAD OF ,
    i = i+1
print("yes")
    
#OR


  
# Write a program to print the multiplication table of a given number using while loop.
num = int(input("Enter a number "))
i = 1
while i<11:
    print(num*i)
    i = i + 1