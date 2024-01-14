######## TO COUNT A WORD

def COUNTMY():
    file = open('data.txt')
    data = file.read().split()
    count = 0 
    for i in data :
        if i.lower() == 'my':
            count += 1
    print(count)
    
COUNTMY()