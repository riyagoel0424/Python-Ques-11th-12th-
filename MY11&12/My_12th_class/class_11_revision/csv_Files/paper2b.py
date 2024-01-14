#### TO REMOVE A RECORD FROM CSV FILE

import csv
def removerow():
    file = open('pqr.csv' , 'r')
    data = csv.reader(file)
    s_no = input('ENTER S_NO OF STUDENT U WANT TO REMOVE')
    listt = []   
    for i in data:
        listt.append(i)           ####### ALG ALG LIST KI ROWS KO EK LIST MEIN LANA  bcz remove function list pr lgta hai
    for k in listt:
        if k[0] == s_no:
            listt.remove(k)    ####### AISE REMOVE KR SKTE HAI
    print(listt)
    
    
removerow()
        
    