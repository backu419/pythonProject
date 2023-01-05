name = "sam"
version="2.1.0"
test_runner="Unittest"
def months(n,year):
    l=[1,3,5,7,8,10,12]
    if n==2:
        if ((year%4==0) or (year%100!=0) and (year%4==0)):
            return 29
        else:
            return 28
    elif n in l:
        return 31
    else:
        return 30
def login(username, password):
    if(username=="Hcluser" and password=="1234"):
        return 1
    else:
        return 0
