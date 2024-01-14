n = int(input(" Enter a number "))
x = n
n1 = n//10000
r1 = n%10000
a = r1*10 + n1
n2 = n//100
r2 = n%100
b = r2*1000+n2
print(a)
print (b)
rev = 0
while (x!=0):
    temp = x % 10
    rev = rev*10 + temp
    x//=10
print(rev)



print(25 * "HELLO ")
