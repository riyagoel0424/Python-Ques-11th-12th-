import pickle

def SEARCH():                                               ###### AGR KOI NAME  SEARCH KRNA HAI TO
    File = open('binefile.dat' , 'rb')
    Data = pickle.load(File)
    # print(Data)
    for i in Data:
        if i[0] == 'fgd':
            print('Yes DATA found ')
    
    
SEARCH()

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

def SEARCH():                                                     ###### AGR USER SE NAME LEKR FIR SEARCH KRNA HAI TO
    File = open('binefile.dat' , 'rb')
    Data = pickle.load(File)
    # print(Data)
    WORD = input('Enter name that u want to search')
    found = 0
    for i in Data:
        if i[0] == WORD:
            print('Yes DATA found ')
            found = 1
    if found == 0:
        print('Not found')
    
    
SEARCH()