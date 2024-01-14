def display():
    file = open('abc.txt')
    data = file.readlines()
    
    for i in data :
        a = i.split(',')
        mileage = int(a[2])
        if mileage < 150 and mileage >100:
            print()
            
            
display()