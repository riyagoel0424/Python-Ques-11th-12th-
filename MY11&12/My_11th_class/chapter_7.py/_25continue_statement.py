for i in range(5):
    if i == 2:
        continue
    print(i)    
    print("Hello ")        # yha value 2 ke liye na to hello print hoga value of i 
    
    
#OR

for i in range(4,12):
    print("Yes")
    if i == 8:
        continue
    print("No") 
# yha yes to sbke liye print hoga but 8 value ke liye no nhi print hoga bcz continue khta hai iss 
# value ke liye yha tk code chl gya to koi ni but aage nhi vhlega ab next value ke liye chlega 

for i in range (1 , 21 ):
    if i % 2 != 0:
        continue
    print(i , "Its an even no.")
