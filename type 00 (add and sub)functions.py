class two:
    a=300
    b=200
    c=0
    def add(self):
        c=self.a+self.b
        print(c)
    def sub(self):
        d=self.a-self.b
        print(d)
obj1=two()
obj1.add()
obj1.sub()
print(obj1.a,"||",obj1.b)
