##### READ THE DETAILS OF CSV FILE AND DISPLAY THEM

import csv
def add_data():
    File = open('pqr.csv' , 'r' , newline='')
    Data = csv.reader(File)
    for i in Data:
        print(i)          ##### EK SATH READ NI KRA SKTE ... TO CSV MEIN AISE HI BAARI BAARI SE KRATE HAI 
        print(i[0] , i[1])  ##### YE AISE AGR SAARA KUCH NA DIKHAKR JO COLUMN DIKHANA HO  (ROW TO SAARI AAYENGI )
    
add_data()