import pickle     ####### APNA DATA DEKHNE KE LIYE JITNI BAAR DUMP KIA HAI UTNI BAAR LOAD 
### LIKHNA PDEGA SAAARA DEKHNE KE LIYE ....SO USE LOOP

def Write():
    File = open('binfile.dat' , 'wb')
    pickle.dump([1,2,3,4,5,6] , File)
    
def READ():
    File = open('binfile.dat' , 'rb')
    Data = pickle.load(File)
    print(Data)
    
    
    
Write()
READ()
    
