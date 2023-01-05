'''duplicates were not allowed in the dictionary and sets'''
d = {}
print(type(d))
d = {10, 20, 30}
print(type(d))
a = {10, 20, 50}
b = {10, 1, 2, 3}
print(a.union(b))  # combining of all elements and extra duplicate values were removed
print(a.intersection(b))  # different values of set were prints out
print(a-b)
print(b-a)

