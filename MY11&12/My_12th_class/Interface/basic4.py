import mysql.connector  
######  TO CREATE STRUCTURE OF TABLE , TO SHOW TABLES IN DATABASE , TO DESC STRUCTURE OF TABLE

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor() 
Command =  '''create table ClassX (
RollNo int Primary key ,
Name varchar(20)
Marks float(4,2))
'''  
cur.execute(Command)
print('yes')


cur.execute('show tables')
for i in cur:
    print(i)
    
    
cur.execute('desc classX')
for i in cur:
    print(i)
    
con.commit()   #### TAAKI JO BHI CHANGES HUM KR RE VO SATH SATH SAVE HOTE RHE 