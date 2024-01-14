#### KITNE RECORDS HAI CSV FILE MEIN YE COUNT KRNE KE LIYE code

import csv
def WritCsv():
    File = open('record.csv' , 'r' , newline='')
    Data = csv.reader(File)
    c=0
    for i in Data:
        # print(i)         
        c+=1 
    print(c-1)                #### to eliminate first row jisme codename name roll ye likha hota hai sbse upr
        
WritCsv()

###### CSV PRINT KRANE PR
############## MTLB AISE LIST MEIN RECORDS DIKHTE HAI CSV FILE KO PRINT KRANE PR 
########## TEXT FILE MEIN READ() MEIN PRINT KRAO TO SIMPLE JESA LIKHA HOTA HAI VESA HI AATA HAI
###### TEXT FILE MEIN LIST MEIN PRINT READLINES() FUNCTION SE HOTA HAI 
    