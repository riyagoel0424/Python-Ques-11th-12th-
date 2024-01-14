# Programme to square of all digits from ones place and then write it as a single number

n = int(input("Enter a number of 4 digits "))  # For 4 digit number
a0 = n // 1000    # 4th digit    
a1 = n % 1000     # first three digit
b1 = a1 // 100    # 3rd digit
a2 = a1 % 100     # first two digits
b2 = a2 // 10     # 2nd digit
a3 = a2 % 10      # 1st digit
num = (a3*a3) * 10 ** 6 + (b2*b2) * 10 ** 4 + (b1*b1) * 10 ** 2 + (a0*a0)
print(num)