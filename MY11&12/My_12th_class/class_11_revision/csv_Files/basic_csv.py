import csv      ##### YE CODE HAI KISI BHI CSV FILE MEIN KOI BHI RECORDS ADD KRANE KA 

# Listt = [ ['Ram  ',' X ',' 50  '] ,  ['Rama  ',' X ',' 56  ']  , ['Raj  ',' XII ',' 81 '] ]
    # Data.writerows(Listt) before while true orr uske neech ka rub

def WrytCsv():
    File = open('pqr.csv' , 'w' , newline='')       ###TEXT FILE AND CSV FILE MEIN EK EXTRA LINE BY DEFAULT CREATE HO JATA HAI USKO HTANE KE LIYE
    Data = csv.writer(File)
    Data.writerow(['Name ',' Class ',' Marks ']  )
    while True :
        Name = input('enter n')
        Class = input('enter c')
        Marks = input('enter m')
        List =[Name , Class , Marks]
        Data.writerow(List)
        Ch = input('enter y to continue')
        if Ch != 'y':
            break
        
WrytCsv()
