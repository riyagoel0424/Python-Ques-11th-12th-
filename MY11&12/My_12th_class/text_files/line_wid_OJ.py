#### VO LINE FROM FILE JO O ya J SE START HO

def check():
    file = open('abc.txt')
    data = file.readlines()
    for i in data:
        if i[0] == 'J':
            print(i , end='')
        elif i[0] == 'O':
            print(i , end='')
    
    
check()