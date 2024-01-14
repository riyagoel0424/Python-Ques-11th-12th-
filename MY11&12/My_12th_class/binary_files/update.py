import pickle

def UPDATE():                                                     ###### AGR USER SE NAME LEKR FIR SEARCH KRNA HAI TO
    File = open('binefile.dat' , 'rb+')
    Data = pickle.load(File)
    # print(Data)
    WORD = input('Enter name that u want to update')
    found = 0
    for i in Data:
        if i[0] == WORD:
            i[0] = input('enter n')
            i[1]= input('enter c')
            i[2] = input('enter m')
            found = 1
    if found == 0:
        print('Not found')
    else:
        File.seek(0)
        pickle.dump(Data,File)
    
    print(Data)
    
UPDATE()