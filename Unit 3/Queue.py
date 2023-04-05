class Node: 
    def __init__(self, data):
        self.data =data
        self.next= None
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data=data
    
#FIFO=PEPS
class Queue:  
    def __init__(self): 
        
        self.head =None
        self.tail = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if not self.head else False
    
    def inQueue(self, data):
        newNode = Node(data)
        if self.getSize() == 0: 
            self.head = newNode
        else: 
            self.tail.next = newNode
        self.tail = newNode
        self.size +=1
        
    def outQueue(self):
        out= None
        if self.size != 0:
            out= self.head.data
            self.head= self.head.next
            self.size -=1
            if self.size != 0:
                self.tail = None
        return out
        
    def show(self):
        if self.isEmpty() == False:
            chain= str(self.head.data)
            reset = self.head
            for i in range (self.size - 1):
                self.head = self.head.next
                data = str(self.head.data)
                chain = chain + ' ' + data
            self.head = reset
            return chain 
        else: return "Empty"
    
    def search(self, data):
        if self.isEmpty() == False:
            data= str(data)
            a = self.show()
            a= a.split()
            l= len(a)
            if data in a: 
                for i in range (l):
                    if a[i] == data:
                        return (i)
                        break
            else: return None
               
                


q= Queue()


q.inQueue(10)
q.inQueue(20)
q.inQueue(50)
q.inQueue(5)
q.inQueue(7)

print(q.show())
print(q.search(0))

