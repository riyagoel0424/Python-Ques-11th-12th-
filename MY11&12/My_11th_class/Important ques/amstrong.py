n = int(input("Enter a number "))
a1 = n % 10
a2 = n // 100
a3 = n // 10
a4 = a3 % 10
a5 = a2 ** 3 + a4 ** 3 + a1 ** 3
if a5 == n:
    print("It is an amstrong no. ")
else:
    print("Not an amstrong no. ")  
