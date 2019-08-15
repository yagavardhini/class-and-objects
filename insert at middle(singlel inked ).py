class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def  inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("the mentioned node is absent")
            return
        newnode=node(newdata)
        newnode.nxt=middle_node.nxt
        middle_node.nxt=newnode
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
list.inbetween(list.headval.nxt,'thurs')
list.listprint()
            
