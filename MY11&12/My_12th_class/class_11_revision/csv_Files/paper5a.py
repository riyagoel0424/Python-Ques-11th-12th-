##### EK FILE KO DUSRI FILE MEIN APPEND KRANA HAI
##### JO DAALNI HAI VO READ MODE MEIN OR JISME DAALNI HAI VO APPEND MODE MEIN 

import csv
def UPDATEFILE():
    file1 = open('record.csv' , 'r')
    file2 = open('pqr.csv' , 'a', newline='')
    data1 = csv.reader(file1)
    data2 = csv.writer(file2)
    for i in data1:
        data2.writerow(i)
    
    
UPDATEFILE()