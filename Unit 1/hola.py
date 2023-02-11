
#section 1 (5 de enero)

print("Hola\nMundo "); print ("phyton")
print("\\")
print("Hola", "Mundo", end="...")
print("Hola", "Mundo", end="\n", sep="-")
print ('Cruel  '*2) 
#default end="\n" sep=" ""
#primero posición, después por nombre, el combinado "Uso de funciones"

print ('Greg\'s Book')
print("Greg's Book")

'''
sección de comentario
+ se usa para concatenar
'''

import array as arr
a= arr.array('i', [5,2,3]) #Aquí declaras de que tipo es tu arreglo, ENTERO
print (a)
print (a[1])
# import= include de C
b=[55,22, "33"] # Al no haber declarado el tipo de arreglo, acepta todo tipo de datos que agregues
b.append("44") #agregar
print (b)
b.pop() #quita el último elemento si no indicas que posición
print(b)
b.pop(1) #QUita el elemento en las posición indicada
print (b)