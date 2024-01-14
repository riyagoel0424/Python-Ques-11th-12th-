### COUNT NO. OF VOWELS IN A FILE   

def check():
    file = open('abc.txt')
    data = file.read()
    V = 0
    for i in data:
        if i in 'aeiouAEIOU':      #### not in for consonants
            V+=1
    print(V)
    
    
check()