# Write a program to store seven fruits in a list entered by the user 

f1 = input("Enter fruit number 1")
f2 = input("Enter fruit number 2")
f3 = input("Enter fruit number 3")
f4 = input("Enter fruit number 4")
f5 = input("Enter fruit number 5")
f6 = input("Enter fruit number 6")
f7 = input("Enter fruit number 7")
print([f1 , f2 , f3 ,f4 ,f5 ,f6 ,f7])

# Write a program to accept the marks of 6 students and display them in a sorted manner.
m1 = int(input(" Enter marks of 1 student"))
m2 = int(input(" Enter marks of 2 student"))
m3 = int(input(" Enter marks of 3 student"))
m4 = int(input(" Enter marks of 4 student"))
m5 = int(input(" Enter marks of 5 student"))
m6 = int(input(" Enter marks of 6 student"))
l1 = [ m1 ,  m2 , m3 , m4 ,m5 , m6 ]
l1.sort()
print(l1)

# Write a program to sum a list with 4 numbers
l = [2 , 7 , 8 ,9 ]
print(l[0] + l[1] + l[2] + l[3])
print(sum(l))