
'''
user_wotd=input("gimme me a word")
user_wotd=user_wotd.upper()
new_word=" "
for letter in user_wotd:
    if letter not in ("A", "E", "I", "O","U"):
        new_word+= letter
print(new_word)

'''
# Use of in & not in 
i=0
c0=int(input("Ingrese número"))
while c0!=1:
    i+=1
    if c0%2==False:
        
        c0=c0/2
        print(c0)
    else: 
        c0=3*c0+1
        print(c0)
    
print("intentos: ",i)


#end=""- elimina el salto de línea 

#import numpy as np- para importar librerías
#pip install numby(para instalar librerías desde la terminar, esto es para WINDOWS)

number=[10, 5, 7, 9, 2, 8]
#print(number.sort())
for i in range(0, len(number)):
    print(number[i], end="\t")

number[0]=111
number.remove(7)#quita el primer 7 que encuentra
del number[1] #elimina esa posición y recorre las demas posiciones
print(number[-2]) #empieza a contar del final al inicio
number.pop()#muestra y elimina la ultima posición
del number[-1]#solo elimina la ult posicion
#number.append() agrega cosas a la cola
number.insert(3,33)#posición 3, agregar el 33

for i in range(0, len(number)):
    print (number[i])

name="Universidad"
r= name.replace("sida", "vih")
print(r, len(name))

'''
funtion
result=function(arg)

method
resutl=data.method(arg)

list.append(value)]
list.insert(location,value)

my_list=[] --> Empty list

'''

my_list=[]
suma=0
for i in range (5):
    my_list.append((i+1)*10)
    #my_list.insert(o,(i+1)*10)
    suma+= my_list[i]
print(my_list)
print(suma)
#print(np.sum(my_list))

nom= "universidad"
print(nom[6:10])
nombre="universidad politécnica"
x=nombre.split()
print(x[1])

#lambda para funciones anónimas


my_list=[5,9,7,2,6]
my_list.sort()
my_list.reverse()
print(my_list)

squares=[x ** 2 for x  in range(10) if x**2%2==0]
print(squares)

board=[]
for i in range(8):
    row=["A" for i in range(8)]
    board.append(row)
print(board)

#c=[[[2,1,5,4],[5,8,6,3][8,7,2,5]],[[5,8,9,6][7,4,5,6][5,2,0,1]]] #arreglo tridimensional
#print(c.shape) DImensiones del arreglo
#print(np.where(a>3))- te dice la posición de los datos del arreglo que son mayores a 3, o sea que cumplen con la condición

board1 = [[i+j for i in range(3)] for j in range(7)] #arreglo bidimensional
#por default genera una lista
#board2 = np.array(board1) - lo transforma a arreglo
'''
print("days")
for day in board1:
    print(day)
print()
'''

list_1 =[3,5,8,9,3]
list_2=list_1
print(list_2)
#le pasa la direccion de memoria
list_1[0]=10
print(list_2)

list_2=list_1[:] #Aquí se pasan los datos, no la direc de memoria
print(list_1[2:4])

del list_1[1:3] #borra y recorre las posiciones
del list_1[:] #está vacio, borra contenido
del list_1 #elimina la lista

print(12 in my_list) #true/false
#print(np.max(my_list)) - no. maximo de la lista

