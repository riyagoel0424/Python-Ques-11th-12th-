#### E AND T LETTERS KO COUNT KRKE UNKI OCCURRENCE NO. BTANA THA INTOTAL IN TEXT


def ETCount():
    E=T=0
    file = open('abc.txt')
    data = file.read()
    for i in data:
        if i in 'eE':
            E+=1
        elif i in 'tT':
            T+=1
    print(E,T)    
        
    
        
ETCount()