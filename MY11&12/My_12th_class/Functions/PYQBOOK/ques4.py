####### ID NAAMAK LIST MEIN  KOI EK NO. KITNI BAAR AAYA HAI USKA COUNT PRINT KRANA HAI 

ID = [155 , 122 , 137 , 110 , 122 , 113]
n =  int(input('enter num from list'))

def HowMany():
    count = 0
    for val in ID :
        if val == n:
            count+=1
    print(count)
    
HowMany()
        