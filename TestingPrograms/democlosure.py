def function1(txt):
    def function2():
        print(txt)
    return function2
msg=function1("hello")
del function1
msg()

