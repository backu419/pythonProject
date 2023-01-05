l1 = [10, 20, 30]
l2 = l1  # it's called shallow copy what ever you do the things on l1 it will reflect the same on the l2 too
print(l1)
l1.append(200)
print(l2)
print(id(l1))
print(id(l2))

l1 = [10, 20, 30]
l2 = l1.copy()  # it's called deep copy whatever you do the things on l1 it will not  reflect the same on the l2 too
print(l1)
l1.append(200)
print(l2)
print(id(l1))
print(id(l2))


# function is a block of code that performs a specific task

def square(n):
    return n * n


print(square(5))


def getvalues(l):
    return sum(l), max(l)


num = [2, 4, 5, 7]
s, m = getvalues(num)
print(s, m)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))

def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
print(fact(5))