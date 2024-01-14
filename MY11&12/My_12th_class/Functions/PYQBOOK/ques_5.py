
Scores = [200,456,300,100,234,678]


def ZeroEnding():
    sum = 0
    for i in Scores:
        if i % 10 == 0:
            sum += i
            
    print(sum)
    
ZeroEnding()

            
    