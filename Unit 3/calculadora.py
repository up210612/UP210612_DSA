import math


def prioridad(c):
    if c in ['+', '-']:
        return 1
    elif c in ['*', '/']:
        return 2
    elif c in ['^']:
        return 3
    elif c in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log']:
        return 4
    elif c in ['(', ')']:
        return 0



def posfix(p):
    p.append('.')

    stack = []
    prior = []
    operator = ['+', '-', '*', '/', '^']
    
    i = 0
    while p[i] != '.':

        if p[i] in operator:
            # print('\n')
            # print("operador")
            b = float(stack.pop())
            a = float(stack.pop())

            if p[i] == '+':
                c = a+b
            elif p[i] == '-':
                c = a-b

            elif p[i] == '*':
                c = a*b

            elif p[i] == '/':
                c = a/b
            elif p[i] == '^':
                c = a**b

            stack.append(c)
            # print("Prioridad: ",prioridad(p[i]), '\n')

        else:

            stack.append(p[i])
            # print("operando")

        i += 1
    value = stack.pop()
    return value


def in2Pos(Q):
    P = []
    stack = []
    Q.insert(0, "(")
    long=len(Q)
    Q.insert(long, ")")
    Q.append('.')  # Para recorrer Q
    i = 0
    while Q[i] != '.':
        if Q[i] == "(":
            stack.append(Q[i])
        elif Q[i] in ['+', '-', '*', '/', '^']:
            # revisar prioridades
            a = int(prioridad(Q[i]))
            b = prioridad(stack[-1])
    
            if a <= b:
                P.append(stack[-1])
                stack.pop()
            stack.append(Q[i])
        elif Q[i] in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log']:
            j=1
            subQ=[]
            while Q[i+j] != ')':
                a= Q[i+j]
                subQ.append(a)
                j+=1
            subQ.append(')')
            if '(' in subQ and ')' in subQ:
                
                subQ.remove('(')
                subQ.remove(')')
                if len(subQ)> 1 :
                    subQ= in2Pos(subQ)
                    c=posfix(subQ)
                    
                else: 
                    c= int( subQ[0])
                
                b= math.radians(c)
                if Q[i] == 'sin':
                    c = math.sin(b)
                elif Q[i] == 'cos':
                    c = math.cos(b)

                elif Q[i] == 'tan':
                    c = math.tan(b)

                elif Q[i] == 'asin':
                    c = c= math.degrees(math.asin(c))
                    
                elif Q[i] == 'acos':
                    c = math.acos(b)
                    
                elif Q[i] == 'atan':
                    c = math.atan(b)
                
                elif Q[i] == 'ln':
                    c = math.log(c)
                    
                elif Q[i] == 'log':
                    c = math.log10(c)

                #stack.append(c)
                #for j in range(len(subQ)+3):
                while Q[i]!=')':   
                    Q.pop(i)
                Q.pop(i)
                Q.insert(i,c)
                continue
        elif Q[i] == ")":
            while stack[-1] != "(":
                P.append(stack[-1])
                stack.pop()
            stack.pop()
        else:
            P.append(Q[i])

        i += 1
    return P



Q = ('2 + asin ( 1.7071 - 1 ) + 3')
Q=Q.split()

Q = in2Pos(Q)
Q = posfix(Q)

print(Q)

#Q=['(', '5', '*', '(', '6', '+', '2', ')', '-', '12', '/', '4', ')']
#Q = ['6', '+', '2']