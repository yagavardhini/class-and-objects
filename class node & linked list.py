class node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
class linkedlist:
    def __init__(self):
        self.head=None
obj=linkedlist()
obj.head=node("mon")
n2=node("tue")
n3=node("wed")
n4=node("thur")
n5=node("fri")
obj.head.nxt=n2
n2.nxt=n3
n3.nxt=n4
n4.nxt=n5
temp=obj.head
while temp!=None:
    print(temp.data,"=>",end='')
    temp=temp.nxt
