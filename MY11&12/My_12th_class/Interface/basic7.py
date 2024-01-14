import mysql.connector  
######  TO DELETE VALUES IN TABLE

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor()
NAME = input('enter name jo delete krna hai  ')
#### NAME KE AALAVA KOI ORR FIELD BHI USE KR SKTE HAI WHERE CONDITION KE LIYE 

command = "Delete from classx where Name = '{}' ".format(NAME )
cur.execute(command)
con.commit()


