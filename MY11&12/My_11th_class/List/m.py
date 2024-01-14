t=eval(input('enter'))
key = int(input('enter no.'))
found=False
for i  in range(len(t)):
    if key==t[i]:
        found=True
        print(i)
if found ==True:
    print('found')
else:
    print('not found')
