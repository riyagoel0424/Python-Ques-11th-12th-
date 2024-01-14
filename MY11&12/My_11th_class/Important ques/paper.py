n = int(input("Enter a number "))
print("Table of " , n , "is")
for i in range(1,11):
    print(n ,' X ' , i ,'=' , n*i )



a = int(input("Enter a year "))
if a % 4 == 0 or a % 400 ==0:
    print("Yes it is a leap year")
else:
    print("Naa ji not a leap year ")
    
    
    
num = int(input("Enter anumber "))
temp = num
count = 0
while num > 0:
    count = count + 1
    num = num // 10
sum = 0
while num:
    rem = num % 10
    sum = sum + rem ** 3
    
    
print(sum)
print(count)



num = int(input("Enter a number "))
mn , mx = num , num
for i in range(4):
    n = int(input("Enter numbers"))
    if n > mx:
        mx = n
    if n < mn:
        mn = n 
print(mx, mn)  

    
    
    
    
 