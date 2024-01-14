#  ISS LIST MEIN SE EVEN NUMBER PUSH THEN POP KRANE


list = [12,13,34, 56 ,21 ,79,98 ,22 ,35, 38]

stack = []

def PUSH(S,N):
    S.append(N)
    
def POP(S):
    if S!=[]:
        return S.pop()
    else:
        print('stack is empty')
    
for i in list :
    if i % 2 == 0:
        PUSH(stack , i)
        
    
if(len(stack) == 0):               ######## YE TB JBB STACK MEIN KUCH BHI PUSH NHI HUA HOGA
    POP(stack)
else:
    for k in range(len(stack)):       ##### YE TB JB STACK MEIN KUCH PUSH HO RKHA HOGA TO BAARI BAARI SE POP HOGA
        print(POP(stack) , end=' ')
    
    
      
    
    
    
   
        
    