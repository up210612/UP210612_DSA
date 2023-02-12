
def raiz11(x):
    return(x**2 - 11)

def biseccion(f, a, b, tol):
    if f(a)*f(b) > 0:
        
        print("No se encontró la raiz.")
    else:
        iter = 0
        while (b - a)/2.0 > tol:
            mp = (a + b)/2.0

            if f(a)*f(mp) < 0:
                b = mp
            else:
                a = mp

            iter += 1
        return(mp, iter)

result, iterac = biseccion(raiz11, -1, 5, 0.0001)
print("Resultado:", result, "\n encontrado en", iterac, "iteraciones")

import math
result, iterac = biseccion(math.cos, 0, 2, 0.0001)
print("Resultado:", result, "\n encpntrado en", iterac, "iteraciones")

'''
Answer: 3.31671142578125 
found in 15 iterations
Answer: 1.5706787109375 
found in 14 iterations
'''








