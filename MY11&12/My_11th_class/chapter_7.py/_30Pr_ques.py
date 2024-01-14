# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number "))
temp = 1
for i in range(2,num):
    if num % i == 0:
        temp = 0
        break
if temp == 0:
    print("No")
else:
    print("Yes")
   


        