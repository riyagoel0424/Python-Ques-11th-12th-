import mysql.connector  
######  EK ROW FETCH KRNE KE LIYE FETCHONE FUNCTION
###### FETCHONE MEIN AGR KOI DATA NHI HAI THEN PRINT HOTA HAI NONE
con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor()
cur = con.cursor()
command = "select * from classx "
cur.execute(command)
DATA = cur.fetchone()
print(DATA)

print(cur.rowcount)



#######  ek baar fetchone kia to first record aayega or rowcount 1 aaaya ...
#### agr abb dobara isi ke neeche firse fetchone   vali line likhkr print kraya to 2nd record milega 
### orr usi ke neeche dobara row count fir se print krayenge to 2 milega and soo on
### agr abb fetchall kraya inn sbke neeche then 3rd record ke aage se saara print hoga and frr row count print
### kraya to total jitni rows hai vo print hoga
