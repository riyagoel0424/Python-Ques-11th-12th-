### COUNT NO. OF LINES IN A FILE


# def check():
#     file = open('abc.txt')
#     data = file.readlines()
#     print(len(data))
    
    
# check()
##################################################################################################


def check():
    file = open('abc.txt' , 'w')
    listt = ['poo ' , 'sam ' , '123 ']
    file.writelines(listt )
          ####  ORRR
    file.writelines(['poo ' , 'sam ' , '123 '])
    print(file)
    
check()