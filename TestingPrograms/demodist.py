#duplicates were not allowed in the dictionary and sets
data={'name':'steve','num':128,'place':'chennai'}
print(data['name'])
print(data.get('contact'))
print(data.setdefault('contact',65656))     #important one in the dictionary
print(data.get('contact'))
print(data['contact'])
print(data)
for i in data:
    print(i)
for i in data.values():
    print(i)

for k,v in data.items():
    print(k,v,sep="->")     #seperator -> sep means

data.update({'contact':"1434"})
print(data)
data.popitem()
print(data)     #removes last elemenr of dictionary
