import demofunctions as df
print(df.fact(7))

def calculateWages(no, wages):
    return no * wages

print(calculateWages(20, 30))

def demo1(n1, n2):
    return n1 + n2

print(demo1(10, 20.30))
print(demo1(10, 5))

def d(*n1):  # single astric mark takes n arguments and returns as tuple
    return (n1)

print(d(10, 20, 20))
print(d(10))

def dd(**n1):  # double astric mark takes n arguments and returns as dictionary
    return (n1)

print(dd(name="sam", id=1234, age="20"))

import os,shutil
files=os.listdir("C:\Users\user665\Desktop\sam")
print(files)
shutil.copytree("C:\Users\user665\Desktop\sam","C:\Users\user665\Desktop\sam1")