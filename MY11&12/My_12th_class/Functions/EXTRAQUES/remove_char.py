#######   TO REMOVE CHARACTERS OF ODD INDEX VALUES IN STRING 

def remove_char():
    ORIGINAL_STRING = input('ENTER STRING')
    string = ' '
    for i in range( len(ORIGINAL_STRING)):                ####  LEN LIKHTE HAI  JBBB INDEX NUMBER CHAHIYE HO 
        if i % 2 == 0:                                    ##### LEN LIKHTE HAI JBBB INDEX NUMBER CHAHIYE HO
            string = string + ORIGINAL_STRING[i]       
    print(string)                                    ##  string name or [] isme uska index give vo index ka character
                                                     ### string name or [] isme uska index give vo index ka character
    
    
   
    
remove_char()