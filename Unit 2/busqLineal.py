
def listNotsort(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i
        else:
            if i==len(L)-1:
                return 'none'

def listSort(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i
        if L[i]>int(x):
            return 'none'


l1=[-5,2,8,6,1,9,14]
l2=[-3,1,5,9,10,12,15]
value=int(input("Ingrese valor a buscar en ambas listas: "))
#value=6
print("Lista No ordenada")
find= listNotsort(l1, value)
print(find)

print("Lista ordenada")
find= listSort(l2, value)
print (find)




