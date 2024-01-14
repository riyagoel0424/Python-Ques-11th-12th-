##### TO DISPLAY NAMES JINKA NAME aeiou (CHOTE VOWELS) SE START HOTA HAI 

import csv
def DISPLAY_NAME():
    file = open('pqr.csv' , 'r')
    data = csv.reader(file)
    for i in data:
        if i[1][0] in 'aeiou':       ### i hai row list ki terms mein usme 1 hai naam uska 0th letter
            print(i[1])              ### naam print krana hai isliye i ka 1 
      
    
DISPLAY_NAME()



