'''
l=[-1,3,4,5,6,-10]
l1=[]
for i in l:
    if (i<0):
        l1.append(i)
        l.remove(i)
print(l)
print(l1)

class Rect:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)
sample=Rect(4,5)
sample.area()
print(id(sample.area()))

l=[4,1,4,3,7,9]
l1=[]
for i in l:
    for j in l:
        if l[i]==l[j]:
            l1.append(i)
            l.remove(i)
print(l)
print(l1)
'''

l=[10,20,30]
s=0
for i in l:
   s+=1
print(s)

l=[10,20,30]
class a:
    def person(self,l):
        print(len(l))
s=a()
s.person([10,20,30])


