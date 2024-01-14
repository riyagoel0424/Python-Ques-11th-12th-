# Different methods of list...
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]

''' here we cannot store these function in another variable. 
ye function l1 me hi lgega jaise di ne btaya tha ki hm a + b krke c me store kre ya sidha 
a me b ad krke a print kraye.. ye function pr hai or iss function me hm c me store nhi kra skte ek trh se '''

# Sort function  ----- increasing order
l1.sort() 
print(l1)
# Reverse function ----- reverse order
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]
l1.reverse() 
print(l1)
# Append function ----- add element at the end
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]
l1.append(369)
print(l1) 
# Insert function ----- insert any element in given index no. 
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]
l1.insert(2 , 75)
print(l1) 
# Pop function ----- delete element from given index no.
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]
l1.pop(4)
print(l1) 
# Remove function ----- remove given element
l1 = [1 , 3 , 7 , 9.7 , 63 ,89 ,7.5 ]
l1.remove(7.5)
print(l1)
