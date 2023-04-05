class Node: 
    def __init__(self, data):
        self.data =data
        self.left= None
        self.right= None
        
    def getSize(self):
        return self.size
    
    def hasDat (self):
        if self.size>=1:
            return True
        else: False
     
class List: 
    def __init__(self): 
        
        self.head =None
        self.last = None
        self.size = 0
        
    def insert (self, data):
        newNode= Node(data)
        if self.size == 0:
            self.head = newNode
            self.last= newNode
            self.size +=1
        elif self.size == 1:
            if data > self.head.data:
                self.last = newNode
                self.last.right =self.head
                self.head.left = newNode
            else:
                self.head = newNode
                self.head.left = self.last
                self.last.right= newNode
            self.size +=1
        else:
            if data >= self.last.data:
                self.last.left = newNode
                newNode.right = self.last
                self.last = newNode
                self.size +=1
            elif data < self.head.data:
                newNode.left = self.head
                self.head.right = newNode
                self.head = newNode
                self.size +=1
            else: 
                if self.size == 2:
                    self.head.left = newNode
                    newNode.right = self.head
                    self.last.right = newNode
                    newNode.left = self.last
                else: 
                    reset1= self.head
                    reset2 = self.head
                    self.head = self.head.left
                    while self.last.data != self.head.data:
                        if data < self.head.data:
                            self.head.right = newNode
                            newNode.left = self.head
                            newNode.right = reset2
                            self.head = reset2
                            self.head.left = newNode
                            break
                        else: 
                            reset2 = self.head
                            self.head = self.head.left
                            if self.last.data == self.head.data:
                                self.head = reset2
                                newNode.right = self.head
                                newNode.left = self.last
                                self.last.right = newNode
                                self.head.left = newNode
                                break
                    self.head = reset1
                    self.size +=1
                    
                
        
    def printR2L (self):
        if self.size != 0:
            chain= str(self.head.data)
            reset = self.head
            for i in range (self.size - 1):
                self.head = self.head.left
                dato = str(self.head.data)
                chain = chain + ' ' + dato
            self.head = reset
            return chain 
        else: return "Empty"
        
    def printL2R (self):
        if self.size != 0:
            chain= str(self.last.data)
            reset = self.last
            for i in range (self.size - 1):
                self.last = self.last.right
                dato = str(self.last.data)
                chain = chain + ' ' + dato
            self.last = reset
            return chain 
        else: return "Empty"
        
    def removeValue (self,data):
        a = self.printR2L()
        a = a.split()
        if data in a:
            reset = self.head
            for i in range (self.size):
                if self.head.data == data:
                    der= self.head.right
                    izq = self.head.left
                    oneBack.left = izq
                    self.head = self.head.left
                    self.head.right = der
                    break
                else:
                    oneBack = self.head
                    self.head = self.head.left
                i+=1
            self.head = reset
            self.size -=1
            return True
        else: return False
        
    def removePositionR2L (self, position):
        if position >= self.size:
            return False
        else:
            reset = self.head
            for i in range (position + 1):
                if i == position:
                    der= self.head.right
                    izq = self.head.left
                    oneBack.left = izq
                    self.head = self.head.left
                    self.head.right = der
                    break
                else:
                    oneBack = self.head
                    self.head = self.head.left
                i+=1
            self.head = reset
            self.size -=1
            return True
        
    def search (self, data):
        data=str(data)
        a = self.printR2L()
        a = a.split()
        i=0
        for i in range (len(a)):
            if a[i] == data:
                break
            else: i+=1
        if i >= len(a): return False
        else: 
            i=str(i)
            return ("True, position " + i)
            
    def seek(self, position):
        if position >= self.size:
            return False
        else:
            reset = self.head
            for i in range (position + 1):
                if i == position:
                    self.head = reset
                    a = str(self.head.data)
                    return ("value " + a)
                else: 
                    self.head = self.head.left
            self.head = reset
                
a = List()


a.insert (1)
a.insert (3)
a.insert (8)
a.insert (5)
a.insert (10)



print(a.printR2L())
print( a.removePositionR2L(2))
print(a.printR2L())
print(a.search(8))
print(a.seek(2))
    