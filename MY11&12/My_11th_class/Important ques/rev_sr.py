n=int(input("enter a 5 digit no"))
a1 = n % 10
a2 = n // 1000
a3 = n % 1000
a4 = a3 // 10
print(a4 * 1000 + a1*100+a2)