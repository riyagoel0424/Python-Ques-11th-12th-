# dic = {'Nitin': 21 , 'ankit': 15}
# x= dic.items()

# print(x)

# dic={}
# dic[(1,2,4)] = 8
# dic[(4,2,1)] = 10
# dic[(1,2)] = 24
# sum=0
# for i in dic:
#     sum += dic[i]
# print(sum)



########### veryyyyyyyyy zrooori reverse krna list ko
l = [ 2 , 3 , 4]
l1=[]
def reverse(l):
    for i in range(len(l)-1,-1 , -1):
        l1.append(l[i]*2)
    print(l1 )
    
reverse(l)
        
