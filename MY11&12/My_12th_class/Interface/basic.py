import mysql.connector 

##### YE HUMNE CONNECTION STHAPIT KIA HAI HMARI PYTHON AND MYSQL MEIN
 
con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'company')
if con.is_connected():
    print('yes')