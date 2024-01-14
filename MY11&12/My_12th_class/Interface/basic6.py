import mysql.connector  
######  TO UPDATE  VALUES IN TABLE

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor()
# command = "Update classx set Name =  'Minakshi' where RollNo = 101"
#### AGR USER SE LENA HAI ROLL NO. AND NAME JO SET KRANA HAI
ROLL_NO = int(input('enter roll no. jiska name update krna hai  ')) 
NAME = input('enter name jo update krke aaye  ')
command = "Update classx set Name = '{}' where RollNo = {}".format(NAME , ROLL_NO)
cur.execute(command)
con.commit()
