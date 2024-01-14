##### DATA MEIN SE VO LINE DELETE KRO JISME USER DWARA ENTER KIA GYA WORD HO
##### DELETE KRNE KE BAAD VALE DATA KO EK NYI FILE MEIN WRITE KRO 

def DELETE_LINES():
    file = open('data.txt')
    data = file.readlines()
    word = input('ENTER NAME TO BE DELETED ')
    for i in data:
        if word in i:    
            data.remove(i)       ##### I USS LIST KA ELEMENT(EK LINE) HAI JISME FILE KI SAARI LINES HAI .
    print(data)
    






DELETE_LINES()    