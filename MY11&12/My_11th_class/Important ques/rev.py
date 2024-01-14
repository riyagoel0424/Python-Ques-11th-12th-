n = int(input(" Enter a number "))  #for a 6 digit no.
a1 = n//10000  #for last two digits
r1 = n%10000  #for first four digits
n2 = r1//100   # for last two digits of r1
r2 = r1%100    #for first two digits of r1
rev = r2*10000+n2*100+a1
print(rev)
