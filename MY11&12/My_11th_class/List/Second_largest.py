a=eval(input('enter list'))
first=a[0]
sec=a[0]
for i in range(1,len(a)):
    if first<a[i]:
        sec=first
        first=a[i]
    elif first>a[i]and sec<a[i] :
        sec = a[i]
print(sec)
       
        
    
    
