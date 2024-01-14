# Write a program to print the multiplication table of n using for loop in reversed order.
num = int(input("Enter a number "))
for i in range(10,0,-1):     # REVERSE KRNE KE LIYE BSS YHA PR FRK KIA HAI BAAKI SAME HAI
    print(str(num) , " X " , str(i) , " = " , num*i)
    
    

# To print each indivisual character of string
str1= "Welcome to my blog"
for i in str1:
    print(i,end="")
