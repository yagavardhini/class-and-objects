class node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nxt=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval,'==>',end='')
            printval=printval.nxt
    def atbeginning(self,newdata):
        newnode=node(newdata)
        newnode.nxt=self.headval
        self.headval=newnode
list=slinkedlist()
list.headval=node('mon')
e2=node('tues')
e3=node('wed')
list.headval.nxt=e2
e2.nxt=e3
list.atbeginning('thurs')
list.listprint()
