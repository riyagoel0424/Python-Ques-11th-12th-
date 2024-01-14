# Roots of Quadratic Equation
import math
a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

root_1 = (-b + pow(b**2 - 4*a*c,0.5))/2*a
root_2 = (-b - pow(b**2 - 4*a*c,0.5))/2*a

print("Value of first root is " , root_1)
print("Value of second root is " , root_2)
