
#while el resultado de mi sumatoria, sea menor a mi cant, seguir incrementando el valor del factorial. 

i=0
acum= 0
residuo=0
cant= int(input("Ingrese el efectivo que tiene:"))
while acum<=cant:
    i+=1
    acum=acum+i
else: 
    residuo=cant-(acum-i)  
    i-=1 
print("Le alcanza para ", i, " boletos. Le sobra ", residuo)