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
        dat2 = self.head.data
        reset=self.head
        long = self.size
        for i in range(long-1):
            self.head= self.head.next
            dat = self.head.data
            dat2 = dat2 + ' ' + dat
        self.head=reset
        
        return dat2  
        #concatenar datos de los nodos y mostrarlos, SIN borrarlos
        
    def exist (self, dato_busca):
        dat = self.show()
        dat = dat.split()
        if dato_busca in dat: return True
        else: return False
        
    

p1 = Stack()

p1.push("jesus")
p1.push("maria")
p1.push("jose")
p1.push("Pau")

print(p1.show())
print(p1.exist('sara'))



#los nodos generan objetos
#propiedades: size, head       