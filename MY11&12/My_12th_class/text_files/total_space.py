### COUNT NO. OF SPACES IN A FILE

def check():
    file = open('abc.txt')
    data = file.read()
    V = 0
    for i in data:
        if i in ' ':       # SPACE KE LIYE ' ' 
            V+=1
    print(V)
    
    
check()