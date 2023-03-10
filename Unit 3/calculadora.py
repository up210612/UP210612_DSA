import math


def prioridad(c):
    if c in ['+', '-']:
        return 1
    elif c in ['*', '/']:
        return 2
    elif c in ['^']:
        return 3
    elif c in ['sen', 'cos', 'tan', 'asen', 'acos', 'atan', 'ln', 'log']:
        return 4
    elif c in ['(', ')']:
        return 0


def in2Pos(Q):
    P = []
    stack = []
    Q.insert(0, "(")
    Q.insert(-1, ")")
    Q.append(".")  # Para recorrer Q
    i = 0
    while Q[i] != '.':
        if Q[i] == "(":
            stack.append(Q[i])
        elif Q[i] in ['+', '-', '*', '/', '^']:
            # revisar prioridades
            a = int(prioridad(Q[i]))
            b = prioridad(stack[-1])
            # print(a,b)
            if a <= b:
                P.append(stack[-1])
                stack.pop()
            stack.append(Q[i])
        elif Q[i] in ['sen', 'cos', 'tan', 'asen', 'acos', 'atan', 'ln', 'log']:
            
            a = Q[i], Q[i+1], Q[i+2], Q[i+3]
            P.append(a) 

        elif Q[i] == ")":
            while stack[-1] != "(":
                P.append(stack[-1])
                stack.pop()
            stack.pop()
        else:
            P.append(Q[i])

        i += 1
    return P


def posfix(p):
    p.append('.')

    stack = []
    prior = []
    operator = ['+', '-', '*', '/', '^']
    funcion = ['sen', 'cos', 'tan', 'asen', 'acos', 'atan', 'ln', 'log']
    i = 0
    while p[i] != '.':

        if p[i] in funcion:
            a = p[i+1], p[i+2], p[i+3]
            # a=a.split()
            if '(' in a and ')' in a:
                a = list(a)
                a.remove('(')
                a.remove(')')
                x = int(a[0])
                b= math.radians(x)
                if p[i] == 'sen':
                    c = math.sin(b)
                elif p[i] == 'cos':
                    c = math.cos(b)

                elif p[i] == 'tan':
                    c = math.tan(b)

                elif p[i] == 'asen':
                    c = math.asin(b)
                    
                elif p[i] == 'acos':
                    c = math.acos(b)
                    
                elif p[i] == 'atan':
                    c = math.atan(b)
                
                elif p[i] == 'ln':
                    c = math.log(x)
                    
                elif p[i] == 'log':
                    c = math.log10(x)

                stack.append(c)
                j = 0
                for j in range(4):
                    p.remove(p[i])
                continue

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

Q = ('1 / ( 100 + 1 / ( 100 + 1 / ( 100 + 1 / 100 ) ) )')
Q=Q.split()

Q = in2Pos(Q)
Q = posfix(Q)

print(Q)


#Q=['(', '5', '*', '(', '6', '+', '2', ')', '-', '12', '/', '4', ')']
#Q = ['6', '+', '2']