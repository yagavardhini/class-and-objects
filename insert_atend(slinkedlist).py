class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
            return
        last=self.headval
        #to find the last node
        while(last.nxt):
            last=last.nxt
        last.nxt=newnode
    def listprint(self):
         printval=self.headval
         while printval is not None:
             print(printval.data,'==>',end='')
             printval=printval.nxt
list=slinkedlist()
list.headval=node('mon')
e2=node('tues')
e3=node('wed')
list.headval.nxt=e2
e2.nxt=e3
list.atend('thurs')
list.listprint()
            
