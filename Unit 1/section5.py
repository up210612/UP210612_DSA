

def ordenar(stack):
	return len(stack)== 0 

def double(x):
    y=x*2
    return y 

a=[5, 6, 9, 8, 7]
for i in range(0, len(a)):
	print(a[i])

#bubble

for i in range (0, len(a)+1 -2):
    for j in range (0, len(a)+1 - i-2):
        x= a[j]
        y= a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x
        
print (a)

print("What's your name?")
nombre= input()
print("What's your last name?")
apellido= input()
print("What's your age?")
edad= input()
nomCom=nombre+" "+ apellido #concatenar inputs

print ("Hola ", nomCom, " de ", edad, " años")

#time.sleep(2)
