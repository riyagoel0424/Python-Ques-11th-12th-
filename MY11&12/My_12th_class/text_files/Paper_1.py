##### EK FILE MEIN E AND U KITNI BAAR AAYA HAI YE BTAO 

def countEU():
    file = open('abc.txt' , 'r')
    data = file.read()
    countU = 0
    countE = 0
    for i in data:
        if i in 'Ee':
            countE += 1
        if i in  'Uu':
            countU += 1
    print('E: ' , countE)  
    print('U: ' , countU) 
             



countEU()