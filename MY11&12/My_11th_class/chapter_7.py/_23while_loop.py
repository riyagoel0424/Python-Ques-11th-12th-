# Write a program to print the content of a list using while loops.
devices = ['Laptop ' , 'Computer' , 'Phone' , 'ipad']
i = 0
while i<len(devices):
    print(devices[i])    # in list index starts from 0
    i = i + 1
    
#OR

for gadgets in devices :   # HERE WE CAN USE ANY WORD OR LETTER IN PLACE OF GADGETS
    print(gadgets)

