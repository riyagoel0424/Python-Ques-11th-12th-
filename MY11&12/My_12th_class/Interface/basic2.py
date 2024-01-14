import mysql.connector  

##### CURSOR FUNCTION KE USE SE EXECUTE FUNCTION MEIN HUM MYSQL KI COMMANDS KO PYTHON MEIN LIKHTE HAIN 

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'company')
if con.is_connected():
    print('yes')
    
cur = con.cursor()        ##### CURSOR FUNCTION KE THROUGH HI HUM EXECUTE FUNCTION KO CALL KR SKTE HAI
cur.execute('show tables')   #### AB EXECUTE FUNCTION MEIN SQL KI SAARI COMMANDS LIKH SKTE HAI
for i in cur:
    print(i)


####### ANSWER ALWAYS IN TERMS OF TUPLES
    
    
    
    
