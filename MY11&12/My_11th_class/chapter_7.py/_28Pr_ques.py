# Write a program to greet all the person names stored in a list l1 and which starts with S.
L1 = ["Harry " , " Sonam" , "Soha" , "Popy " , "Sandy" , "Sameer"]
for name in L1:
    if name.startswith("S"):
        print("Hello " , name)
        
# HERE SONAM IS NOT PRINTED BCZ IT SATRTS WITH SPACE BUT NOT WITH S
        