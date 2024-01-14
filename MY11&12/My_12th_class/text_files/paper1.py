##### LONGEST WORD PRINT KRAO IN A TEXT FILE

def longest_word():
    file = open('abc.txt' , 'r')
    data = file.read().split()
    longest_len = len(max(data , key = len))
    result = [i for i in data if len(i) == longest_len]
    print(result)
    
            
            
            
    
    
    
    
longest_word()