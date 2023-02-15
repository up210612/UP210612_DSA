def prioridad (c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c in ['^']:
        return 3
    elif c in ['(', ')']:
        return 0


#p=[5,6,2,'+','*',12,4,'/','-']
#cadenas polacas
Q=['(', '5', '*', '(', '6', '+', '2', ')', '-', '12', '/', '4', ')']
#Q=q.split()

P=[]
stack=[]
Q.insert(0, "(")
Q.insert(-1, ")")
Q.append(".") #Para recorrer Q
i=0
while Q[i]!= '.':
    if Q[i]== "(":
        stack.append(Q[i])
    elif Q[i] in ['+','-','*','/','^']:
        #revisar prioridades
        a= int(prioridad(Q[i]))
        b= prioridad(stack[-1])
        #print(a,b)
        if a<=b:
            P.append(stack[-1])
            stack.pop()
        stack.append(Q[i])

    elif Q[i] == ")":
        while stack[-1]!= "(":
            P.append(stack[-1])
            stack.pop()
        stack.pop()
    else:
        P.append(Q[i])
    
    i+=1

print(P)

