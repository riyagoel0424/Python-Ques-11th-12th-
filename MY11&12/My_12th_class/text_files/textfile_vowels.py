### VO LINES JINKA FIRST LETTER VOWEL NHI HAI VO PRINT KRVAO 

def countlines():
    file = open("abc.txt")
    data = file.readlines() 
    # print(data)
    for i in data:
        if i[0] not in  'aeiouAEIOU':
            print(i , end='')
            
            
            
    
    
countlines() 

