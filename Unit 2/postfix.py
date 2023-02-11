def prioridad (c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c in ['^']:
        return 3




#p=[5,6,2,'+','*',12,4,'/','-']
op=input ()
p=op.split()
#print(p)
p.append(')')

stack=[]
prior=[]
i=0
while p[i]!= ')':
    
    if p[i] in ['+','-','*','/','^']:
        print('\n')
        print("operador")
        b=float(stack.pop())
        a=float(stack.pop())
        
        if p[i]== '+' :
            c=a+b
        elif p[i]== '-' :
            c=a-b

        elif p[i]== '*' :
            c=a*b

        elif p[i]== '/' :
            c=a/b
        elif p[i]== '^' :
            c=a**b

        stack.append (c)
        print("Prioridad: ",prioridad(p[i]), '\n')

    else: 

        stack.append(p[i])
        print("operando")

    i +=1
value=stack.pop()
print('Resultado: ',value)

'''
p=postfix.split()
p=input("Ingrese posfix")
p=p.split()
for elem in p

'''