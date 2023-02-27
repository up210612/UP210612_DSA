class node: 
    def __init__(self, data):
        self.data =data
        self.next= None
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data=data

nodo1= node("jesus")
print(nodo1.data)
print(nodo1.getData())
print(nodo1.next)

nodo1.setData("Maria")
print(nodo1.getData())
print(nodo1.data)
nodo2= node("Jose")

nodo1.next=nodo2
print(nodo1.next.data)

nodo3= node("jesus")
nodo2.next=nodo3

print("----->")
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)