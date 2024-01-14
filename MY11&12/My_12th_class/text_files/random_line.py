####  TO READ A RANDOM LINE FROM FILE

import random 

def check():
    file = open('abc.txt')
    data = file.readlines()
    a= len(data)                     ##### TOTAL LENGTH OF LIST
    b = random.randint(0,a-1)        ##### RANDOM INDEX NUMBER
    print(data[b])
    
    
check()