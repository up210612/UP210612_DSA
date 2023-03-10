class Node: 
    def __init__(self, data):
        self.data =data
        self.next= None
    
    def getData(self):
        return self.data

class Stack: #las clases siempre comienzan con MAYUSC 
    def __init__(self):
        self.head=None
        self.size=0
    
    def getSize(self):
        return self.size

    def isEmpty(self):
        
        return True if self.size == 0 else False
        #return True if not self.size else False 
        #return True if not self.head else False 

    def hasDat (self):
        if self.size>=1:
            return True
        else: False

    def push (self, data):
        newNode = Node(data)
        newNode.next= self.head
        self.head= newNode
        self.size+=1
    
    def pop (self):
        dat= None
        if not self.isEmpty():
            dat= self.head.data
            self.head=self.head.next
            self.size-=1
        return dat
    
    def peak (self):
        dat=None
        if not self.isEmpty():
            dat = self.head.data
        return dat
    
    def show(self):
        cad = self.head.data
        self.head= self.head.data
        
        return cad   
        #concatenar datos de los nodos y mostrarlos, SIN borrarlos
        
    

p1 = Stack()
print(p1.peak())
p1.push("jesus")
p1.push("maria")
p1.push("jose")

print(p1.show())

print(p1.peak())
print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())

#los nodos generan objetos
#propiedades: size, head       