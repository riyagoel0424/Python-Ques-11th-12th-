# Program to find semi perimeter and area of triangle
import math
a = int(input("Enter first side "))
b = int(input("Enter second side "))
c = int(input("Enter third side "))
s = (a + b + c)/2
print(s)
ar = s * (s-a) * (s-b) * (s-c)
print(math.sqrt(ar))
print(pow(ar,0.5))
print(ar**0.5)
