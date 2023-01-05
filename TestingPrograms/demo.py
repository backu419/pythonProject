#iterator
'''l=[10, 20, 30, 40]
p=iter(l)
print(next(p))
print(next(p))

a=[i for i in range(10)]
print(a)

#generator
def num():
    m=1
    print("first print")
    yield m
    m+=2
    print("second print")
    yield m
    m+=2
    print("third print")
    yield m
print(num())
for p in num():
    print(p)


import time
start_time=time.time()
a=[i for i in range(10)]
print(a)
end_time=time.time()
print(end_time-start_time)


st=time.time()
for i in range(10):
    print(i,end=',')
et=time.time()

print(et-st)
'''

#list
import time
l=[i for i in range(1000)]
s=time.time()
for x in l:
    print(x) #,end=",")
e=time.time()
print(e-s)

#iterator
l=[i for i in range(1000)]
p=iter(l)
s=time.time()
for x in p:
    print(x) #,end=",")
e=time.time()
print(e-s)