import mysql.connector  
######  TO SHOW ALL VALUES IN TABLE USING FETCHALL  
###### FWTCHALL GIVES LIST OF RECORDS IN TUPLES 
###### FETCHALL MEIN AGR KOI DATA NHI HAI FETCH KRNE KE LIYE THEN KHALI EMPTY LIST 

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor()
command = "select * from classx "
cur.execute(command)
# for i in cur:
#     print(i)          ###### AGR EK CODE MEIN EK BAAR RECORD PRINT KRA LIYE AND THEN DOBARA FETCH KRAYA TO KHALI LIST AAYEGI

######    AGR UPR KI DONO LINES UNCOMMENT KRDO THEN EK TO HUME ALG ALG TUPLES MEIN ALG ALG RECORD MILEGA OR NEECHE FETCHALL LIKHA HAI 
######    TO EK KHALI LIST BHI MILEGI BCZ EK BAAR DATA PRINT HO GYA HAI ORR DATA FETCH KRNE KE LIYE HI NHI HAI

##### AGR I IN CUR PRINT KRAO TO ALG ALG RECORDS TUPLES MEIN AAYENEGE BUT AGR FETCHALL KRKE SEEDHA PRINT KRAO TO 
####  LIST OF TUPLES AAYENGE
    
DATA = cur.fetchall() 
print(DATA)

print(cur.rowcount)   #### YE NO. OF ROWS BTATA HAI 