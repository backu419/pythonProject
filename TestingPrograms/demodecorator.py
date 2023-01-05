'''
def function1(func):
    def function2():
        print("Hello from function2")
        func()
    return function2
def demo():
    print("Hi, how are you ?")
f=function1(demo)
f()
'''
def function1(func):
    def function2():
        print("Hello from function2")
        func()
    return function2
@function1
def demo():
    print("Hi, how are you ?")
demo()
#f=function1(demo)
#f()