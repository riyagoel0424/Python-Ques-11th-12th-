'''Write a program to print the following star pattern:
*

**

*** for n times  ''' 
n = int(input("Enter value of n"))
for i in range(0, n+1):           # OR  for i in range(n):
    print("*" * i)             #         print("*" * (i+1))