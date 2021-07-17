class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.start = None

    def insertlast(self,dataval):
        newNode = node(dataval)
        if(self.start==None):
            self.start=newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next=newNode


    def insertbegining(self,dataval):
        
        newNode = node(dataval)
        if(self.start == None):
            self.start = newNode
        else:
            
            newNode.next = self.start
            self.start = newNode


    def displaylist(self): 
        if(self.start == None):
            print("List is Empty")
        else:
            temp = self.start
            #print("Temp is  = ",temp.data)
            while temp != None:
                print(temp.data,end= ' ')
                temp=temp.next
                


    def deletefirst(self):
        if self.start == None:
            print("List is empty")
        else:
            #self.start=self.start.next
            temp=self.start
            self.start = temp.next
            temp.next = None

    def deletelast(self):
        '''temp=self.start.next
        prev=self.start
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next= None'''
        
        prev = self.start
        temp = prev.next
        while(temp.next != None):
            prev = prev.next
            temp = temp.next
        prev.next = None

#the length of the linked list
    def length(self):
        if self.start == None:
            return 0
        else:
            count = 1
            temp = self.start
            while(temp.next != None):
                count += 1
                temp = temp.next
            return(count)


    def deleteanyposition(self,pos):
        prev = self.start
        temp = prev.next
        #print("length of the list",self.length())
        if pos < 1:
            print("Enter positive valuue")
        elif pos > self.length():
            print("Out of bound")
        else:
            for i in range(1,pos-1):
                prev = prev.next
                temp = temp.next
            prev.next = temp.next
            temp.next = None

    def deletebeforenode(self,pos):
        prev=self.start
        temp=prev.next
        for i in range(1,pos-2):
            prev = prev.next
            temp = temp.next
        prev.next=temp.next
        temp.next=None


    def deleteafternode(self,pos):
        prev = self.start
        temp = prev.next
        for i in range(1,pos):
            prev=prev.next
            temp=temp.next
        prev.next = temp.next
        temp.next = None
        
         
            
            



mylist = Linkedlist()
print(isinstance(mylist,Linkedlist))

mylist.insertlast(25)
mylist.insertlast(35)
mylist.insertlast(45)
mylist.insertlast(55)
mylist.insertlast(65)
mylist.displaylist()
print()

mylist.insertbegining(88)
#mylist.deleteafternode(4)
mylist.displaylist()
print()
mylist.deletefirst()
mylist.deletelast()
mylist.displaylist()

print()
mylist.deleteanyposition(3)
mylist.displaylist()

print()
mylist.deletebeforenode(3)
mylist.displaylist()

print()
mylist.deleteafternode(1)
mylist.displaylist()

print()
mylist.insertlast(67)
mylist.displaylist()






