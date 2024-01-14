
M={}
a=int(input('enter no. of stu'))
for i in range(a):
    d=input('name')
    e=int(input('roll no.'))
    M[d]=e
print(M)
ans='y'
while ans == 'y':
    d=input('name')
    e=int(input('roll no.'))
    M[d]=e
    ans=input('y or n')
print(M)


    
    
  

        

