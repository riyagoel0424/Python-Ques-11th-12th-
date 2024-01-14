# Concatenating two strings (Adding two strings)
a = "I love you "
b ="RIya "
print(a+b)

#  String Slicing
c = "Hello Buddy "
print(c[3])
print(c[4:8])  #Here 8 is excluded
print(c[2:9])  # Here 9 is excluded
print(c[:7])  # If blank space in first place then min value of index will come automatically
print(c[3:])   # If blank space in second place then lengh of string  will come automatically
print(c[-8:-1]) # this is same as[4:11]
print(c[4:11])

# Slicing with skip value
print(c[1:9:3]) # Print letter after skipping every 2 letters 
