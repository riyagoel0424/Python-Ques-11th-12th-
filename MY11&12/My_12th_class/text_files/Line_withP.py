#### VO LINE FROM FILE JO P SE START HO

def check():
    file = open('abc.txt')
    data = file.readlines()
    for i in data:
        if i[0] == 'P':
            print(i , end='')
    
    
check()

