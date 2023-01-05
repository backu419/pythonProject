'''
def add(x,y):
    return x+y
a=add
print(a(10,20))
print(add)
print(id(add))


def incr(x):
    return x+1
def decr(x):
    return x-1
def operator(func,n):
    r=func(n)
    return r
print(operator(decr,10))
print(operator(incr,10))
'''

def odd(x):
    l = [i for i in range(x)]
    for i in l:
        if (i%2!=0):
            yield i
def even(x):
    l = [i for i in range(x)]
    for i in l:
        if (i%2==0):
            yield i
def oper(func,n):
    r=func(n)
    return r
a=oper(odd,50)
for i in a:
    print(i)
a=oper(even,50)
for i in a:
    print(i)

