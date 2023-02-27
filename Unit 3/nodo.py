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