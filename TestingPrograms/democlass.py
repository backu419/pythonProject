class Person:
    name=""
    id=0
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(self.name,self.id)
P=Person("SAM",200)
P.show()