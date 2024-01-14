import mysql.connector  
######  TO INSERT VALUES IN TABLE

con = mysql.connector.connect(host = 'localhost' ,
                              user = 'root' ,
                              password = '12345',
                              database = 'Schools')
    
cur = con.cursor()

while True:
    RollNo = int(input('enter roll no. '))
    Name = input('enter name ')
    command = "insert into classx values({}, '{}')".format(RollNo , Name)
    #### {} ye ek baar '' inme daala hai bcz string hai
    #### FORMAT FUNCTION {} INKO EK EK KRKE ROLLNO FRR NAME SE REPLACE KREGA
    #### ISI FORMAT SE USER SE TYPE KRAYENGE VALUES AND INSERT KRAYENGE TABLE MEIN 
    cur.execute(command)
    con.commit()
    Ch = input('enter y to continue')
    if Ch != 'y':
        break
    
print('done')