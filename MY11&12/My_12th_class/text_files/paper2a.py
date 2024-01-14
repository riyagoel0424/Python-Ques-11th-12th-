###### TO DELETE THE 4TH WORD FROM A TEXT FILE 

def DELETE():
    file = open('data.txt')
    data = file.read().split()
    print(data)
    data.remove(data[2])
    print(data)
    
DELETE()