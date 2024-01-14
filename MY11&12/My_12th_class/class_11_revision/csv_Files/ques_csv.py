###### DATA ADD KRNA EK  CSV FILE MEIN THROUGH PYTHON

import csv

def ADD():
    File = open('record.csv', 'w' , newline='')
    Data = csv.writer(File)
    Data.writerow(['empid', 'Name', 'Mobile'])
    while True:
        empid= input('enter n')
        Name = input('enter c')
        Mobile = input('enter m')
        Listt=[empid , Name ,Mobile]
        Data.writerow(Listt)
        Ch = input('enter y to continue')
        if Ch != 'y':
            break
        
        
ADD()    


###### TO DISPLAY THE RECORDS OF EMPLOYEE WHOSE EMPID = 120

def search():
    File=open('record.csv')
    Data= csv.reader(File)
    next(File)
    for i in Data:
        if int(i[0]) == 120:           ########JAANWAR YHAA INT KRNA MT BHOOLIO BCZ SARE RECORD STRING MEIN HAI
            print(i)
            
            
search()
        
    


     
     