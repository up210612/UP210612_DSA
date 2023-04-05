from tkinter import *
from math import *
import math
import tkinter.font as font 

def prioridad(c):
    if c in ['+', '-']:
        return 1
    elif c in ['*', '/']:
        return 2
    elif c in ['^', '√']:
        return 3
    elif c in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log']:
        return 4
    elif c in ['(', ')']:
        return 0



def posfix(p):
    p.append('.')

    stack = []
    prior = []
    operator = ['+', '-', '*', '/', '^', '√']
    
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
            elif p[i] == '√':
                c = math.sqrt(a)
                stack.append (b)

            stack.append(c)
            # print("Prioridad: ",prioridad(p[i]), '\n')

        else:

            stack.append(p[i])
            # print("operando")

        i += 1
    value = stack.pop()
    return value


def in2Pos(Q):
    if Q[1] == '-':
        Q.insert(0,'0')
    elif Q[2] == '-':
        Q.insert(1,'0')
        Q.insert(0,'(')
    P = []
    stack = []
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
                    c = math.asin(b)
                    
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


ventana = Tk()
ventana.geometry("448x550")
ventana.title("CALCULADORA")

ventana.geometry("445x433")
ventana.configure(bg='gray14')
al = 3
an = 11

operador=""
a = StringVar()

def bclick(num):
    global operador 
    operador = operador + str(num)
    a.set(operador)

def operacion(operador):
    o = operador.get()
    try:
        infix = o.split()
        infix.insert(0,'(')
        infix.append(')')
        
        postfix = in2Pos(infix)
        result = posfix(postfix)
        a.set(result)
    except:
        clear()
        operacion=("ERROR")
        a.set(operacion) 

def clear(): 
    global operador 
    operador = "" 
    a.set("")
    



botonexpo = Button(ventana, text="EXP", bg=('snow'),width=an, height=al, command=lambda:bclick(" ^ "))
botonexpo.place(x=179, y=375)

botonigual = Button(ventana, text="=", bg=('snow'),width=an, height=al, command=lambda:operacion(salida))
botonigual.place(x=357, y=375)

botonraiz = Button(ventana, text="√", bg=('snow'),width=an, height=al, command=lambda:bclick(" √ "))
botonraiz.place(x=268, y=375)

botonsuma = Button(ventana, text="+", bg=('snow'),width=an, height=al, command=lambda:bclick(" + "))
botonsuma.place(x=268, y=316)

botonresta = Button(ventana, text="-", bg=('snow'),width=an, height=al, command=lambda:bclick(" - "))
botonresta.place(x=357, y=316)

botonrestasig = Button(ventana, text="(-)", bg=('snow'),width=an, height=al, command=lambda:bclick("-"))
botonrestasig.place(x=1, y=375)

botonmul = Button(ventana, text="x", bg=('snow'),width=an, height=al, command=lambda:bclick(" * "))
botonmul.place(x=268, y=258)

botondiv = Button(ventana, text="/", bg=('snow'),width=an, height=al, command=lambda:bclick(" / "))
botondiv.place(x=357, y=258)

botonpar1 = Button(ventana, text="(", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" ( "))
botonpar1.place(x=357, y=84)

botonpar2 = Button(ventana, text=")", bg=('gray9'), fg=('snow'),width=an, height=al, command=lambda:bclick(" ) "))
botonpar2.place(x=357, y=142)

botonsen = Button(ventana, text="sin", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" sin "))
botonsen.place(x=1, y=84)

botoncos = Button(ventana, text="cos", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" cos "))
botoncos.place(x=90, y=84)

botontan = Button(ventana, text="tan", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" tan "))
botontan.place(x=179, y=84)

botonasen = Button(ventana, text="asen", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" asin "))
botonasen.place(x=1, y=142)

botonacos = Button(ventana, text="acos", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" acos "))
botonacos.place(x=90, y=142)

botonatan = Button(ventana, text="atan", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" atan "))
botonatan.place(x=179, y=142)

botonln = Button(ventana, text="ln", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" ln "))
botonln.place(x=268, y=84)

botonlog = Button(ventana, text="log", bg=('gray9'),fg=('snow'),width=an, height=al, command=lambda:bclick(" log "))
botonlog.place(x=268, y=142)

boton7 = Button(ventana, text="7", bg=('snow'),width=an, height=al, command=lambda:bclick("7"))
boton7.place(x=1, y=200)

boton8 = Button(ventana, text="8", bg=('snow'),width=an, height=al, command=lambda:bclick("8"))
boton8.place(x=90, y=200)

boton9 = Button(ventana, text="9", bg=('snow'),width=an, height=al, command=lambda:bclick("9"))
boton9.place(x=179, y=200)

boton4 = Button(ventana, text="4", bg=('snow'),width=an, height=al, command=lambda:bclick("4"))
boton4.place(x=1, y=258)

boton5 = Button(ventana, text="5", bg=('snow'),width=an, height=al, command=lambda:bclick("5"))
boton5.place(x=90, y=258)

boton6 = Button(ventana, text="6", bg=('snow'),width=an, height=al, command=lambda:bclick("6"))
boton6.place(x=179, y=258)

boton1 = Button(ventana, text="1", bg=('snow'),width=an, height=al, command=lambda:bclick("1"))
boton1.place(x=1, y=316)

boton2 = Button(ventana, text="2", bg=('snow'),width=an, height=al, command=lambda:bclick("2"))
boton2.place(x=90, y=316)

boton3 = Button(ventana, text="3", bg=('snow'),width=an, height=al, command=lambda:bclick("3"))
boton3.place(x=179, y=316)

boton0 = Button(ventana, text="0", bg=('snow'),width=an, height=al, command=lambda:bclick("0"))
boton0.place(x=90, y=375)

botonAC = Button(ventana, text="AC", bg=('medium blue'),fg=('snow'),width=an, height=al, command= lambda: clear ())
botonAC.place(x=268, y=200)

botonDEL = Button(ventana, text="DEL", bg=('medium blue'), fg=('snow'),width=an, height=al, command = lambda: clear())
botonDEL.place(x=357, y=200)

salida = Entry(ventana, font=("Consolas",25,"bold"), textvariable=a, width=22,bd=20, insertwidth=5, bg="dark olive green", justify="right")
salida.place(width=380,height=60)
salida.pack()

ventana.mainloop()