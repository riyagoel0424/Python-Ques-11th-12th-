import mysql.connector 

##### TO GIVE DATABASE CREATE KRNE KI COMMAND 
 
con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'company')
    
cur = con.cursor()        ##### CURSOR FUNCTION KE THROUGH HI HUM EXECUTE FUNCTION KO CALL KR SKTE HAI
Command = 'Create database Schools '
cur.execute(Command)
print('done')


