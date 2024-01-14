# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number "))
a = 1
for i in range(1, num+1):
    a = a * i
print("Factorial of " , str(num) , "=" , a)