import pickle      ## phle upr vala dekhne ke liye neeche vala sara comment kr and vice versa

def Wrytbinary():
    File = open('binefile.dat' , 'wb')      
    while True :
        Name = input('enter n')
        Class = input('enter c')
        Marks = input('enter m')
        List =[Name , Class , Marks]
        pickle.dump(List , File)
        Ch = input('enter y to continue')
        if Ch != 'y':
            break
        
        
def READ():                                               ########  PTA NHI LOOP KB BND HOGA ISLIYE TRY AND EXCEPT KA USE VRNA ERROR 
    File = open('binefile.dat' , 'rb')
    try:
        while True:
            Data = pickle.load(File)
            print(Data)
    except:
        File.close()
        

Wrytbinary()
READ()


###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################



def Wrytbinary():
    File = open('binefile.dat' , 'wb')                           
    Liste =[]    
    while True :
        Name = input('enter n')
        Class = input('enter c')
        Marks = input('enter m')
        List =[Name , Class , Marks]
        Liste.append(List)
        Ch = input('enter y to continue')                     ##### AGR TRY EXCEPT USE NI KRNA TO PHLE SARA DATA EK LIST MEIN LE LO USS LIST KO]
        if Ch != 'y':                                         #### DUSRI LIST MEIN DAAL KR FRR EK BAAR DUMP KRVAO TO LOAD BHI EK HI BAAR KRNA PDEGA
            break
    pickle.dump(Liste , File)



def READ():                                             
    File = open('binefile.dat' , 'rb')
    Data = pickle.load(File)
    print(Data)
    
     
        
Wrytbinary()
READ()



