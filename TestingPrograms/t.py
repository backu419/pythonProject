l=[i for i in range(100)]
def geteven(l):
    for i in l:
        if(i%2==0):
            yield i

a = geteven(l)
for i in a:
    print(i)
