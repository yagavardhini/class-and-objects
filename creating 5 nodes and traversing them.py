class node:
    def __init__(self,x):
        self.data=x
        self.addres=None
n1=node(500)
n2=node(100)
n3=node(400)
n4=node(200)
n5=node(300)
n2.addres=n4
n4.addres=n5
n5.addres=n3
n3.addres=n1
temp=n2
while temp!=None:
    print(temp.data,"=>",end='')
    temp=temp.addres
    
