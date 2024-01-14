a = eval(input('Enter first number '))
b = eval(input('Enter second number '))

def add(a,b):
    c=a+b
    print(c)

def sub(a,b):      # absolute value mile iske liye abs lgaya hai
    m=a-b
    print(abs(m))
    
def multi(a,b):
    n=a*b
    print(n)
    
def div(a,b):     # hmesha bda divide by chota ho iske liye conditional statement bnai hai
    if a>=b:
        print(a/b)
    else:
        print(b/a)
        
        
add(a,b)
sub(a,b)
multi(a,b)
div(a,b)



''' agr hum def mein last mein print(c) ki jgh return(c) likhte then neeche print(add(a,b)) likhna pdta'''
