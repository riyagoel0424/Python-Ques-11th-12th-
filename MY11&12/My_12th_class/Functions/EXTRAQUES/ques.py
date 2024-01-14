###### EK DICTIONARY INPUT KRAI THEN USME KOI KEY AND VALUE PAIR DELETE KRAYA

def DICTIONARY():
    keys = []
    values = []
    n = int(input('enter no. of elements: ')) # Number of elements in dictionary entered by user
    
    for i in range(n): # one by one values store in dictionary
        name = input('name: ') # Different keys entered by user
        keys.append(name)
        
        phone_no = int(input('phone_no: ')) # Different values entered by user 
        values.append(phone_no) # list marks store
        
        dictionary = dict.fromkeys(keys , values[i])
    print(dictionary)
    
    
    NAME_DELETION = input('ENTER NAME TO BE DELETED ')
    if NAME_DELETION in dictionary:
        del dictionary[NAME_DELETION]
        print(dictionary)
    else:
        print('NAME NOT FOUND ')
    
    
DICTIONARY()


