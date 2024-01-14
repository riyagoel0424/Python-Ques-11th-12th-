##### TOTAL DIGITS IN FILE COUNT

def countdigits():
    file = open('abc.txt')
    data = file.read()
    c=0
    for i in data:
        if i in '1,2,3,4,5,6,7,8,9,0':              #### ORRR  if i.isdigit():
            print(i)
            c+=1
    print('total digits' , c)









countdigits()