'''

horas=int (input("ingrese las horas\n"))

minutos=int (input("ingrese los minutos\n"))

duration=int (input("ingrese la duración en minutos\n"))
minutos+=duration
horas= horas+(minutos//60)

if horas > 24:
    horas=(horas)%24

minutos = (minutos%60)
print(horas, ":", minutos)  



year= int (input ("enter year: "))

if year < 1582:
    print ("No within the gregorian calendar period")
elif (year%4):
        print("common year")
else: print ("leap year")


number=1
while number!=0:
    print (number+1)
   

a=[10,20,30,40,50]
#j=(len(a)-1)
for i in range (len(a)):
    if a[i]==a[-i]:
        a[i], a[-i]=a[-i],a[i]
        
print(a)

 '''
 