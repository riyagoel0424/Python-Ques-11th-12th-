limit = 7 #WE LET A LIMIT OF A STACK IS EQUAL TO 7
stack = []
def PUSH(stk ,content):
    if len(stk) >= limit:
        print('ovrflow')
    else:
        stk.append(content)
        

def POP(stk):
    if stk != []:
        print(stk.pop())
    else:
        print('underflow')
        


PUSH(stack ,5)
PUSH(stack ,4)
PUSH(stack ,2)
print(stack)
        
        
        
         