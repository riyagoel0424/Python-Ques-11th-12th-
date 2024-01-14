###### DATA ADD KRANA HAI INN CSV FILE

import csv
def add_data():
    File = open('pqr.csv' , 'w')
    Data = csv.writer(File)
    Data.writerow(['customer code' , 'cust name' , 'amount'])
    
    while True:
        customer_code = int(input('enter customer_code'))
        cust_name = input('enter cust name ')
        amount = int(input('enter amount '))
        list = [customer_code , cust_name ,amount]
        Data.writerow(list)
        Ch = input('enter y to continue')
        if Ch != 'y':
            break
    
add_data()