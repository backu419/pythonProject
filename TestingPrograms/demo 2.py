def add_num(n):
    def add(x):
        return x+n
    return add
num1=add_num(10)
num2=add_num(12)
print(num1(5))
print(num2(5))