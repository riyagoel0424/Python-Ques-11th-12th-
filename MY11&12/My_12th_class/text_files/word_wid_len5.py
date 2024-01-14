#####  THOSE WORDS FROM FILE HAVING LENGTH 5    .......
###  SPLIT FUNCTION LIST MEIN ANSWER DETA HAI AND SPACE KO KHA JATA HAI ...USKI JGH COMMA ,

def word():                                   ##JB BHI WORDS KI BAAT KR RKHI HO TO MOSTLY READ() AND THEN SPLIT()                        
    file = open('abc.txt')                    ##JB BHI WORDS KI BAAT KR RKHI HO TO MOSTLY READ() AND THEN SPLIT()
    data = file.read()
    data2 = data.split()
    print(data)
    c = 0                                                    
    for i in data2:                                          
        if len(i) == 5:
            print(i)
            c+=1
    print("Total words with len 5 :" , c)                                                      
        
word()