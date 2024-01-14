#75 SE BDI VALUES VALI KEYS POP KRANI 


dictionary = {"OM":75 , "Jai" : 46 , "BOB":80, "ALI":69, "ANU":96 , "TOM": 84}
def PUSH(S,N):
    S.append(N)
       
def POP(S):
    if S != []:
        return S.pop()
    else:
        print("Stack is empty")
    
stack = []
for k in dictionary:
    if dictionary[k] >= 75:
        PUSH(stack, k)
        
if(len(stack) == 0):   
    POP(stack)
else:  
    for i in range(len(stack)):
        print(POP(stack), end =" ")
    

   
    
        
    
    

    