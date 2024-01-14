def DICTIONARY():
    keys = []
    values = []
    n = int(input('enter: ')) # Number of elements in dictionary entered by user
    
    for i in range(n): # one by one values store in dictionary
        roll_no = int(input('roll: ')) # Different keys entered by user
        keys.append(roll_no)
        
        marks = int(input('marks: ')) # Different values entered by user for each roll number
        values.append(marks) # list marks store
        dictionary = dict.fromkeys(keys , values[i])
    print(dictionary)
    
DICTIONARY()
