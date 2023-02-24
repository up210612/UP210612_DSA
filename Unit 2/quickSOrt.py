def quicksort (a,primero,ultimo):
    i=primero
    j=ultimo
    central =(primero+ultimo)//2
    pivote=a[central]
    while (i<=j):
        while (a[i]<pivote):
            i=i+1
        while (a[j]>pivote):
            j=j-1
        if (i<=j):
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
            i+=1
            j-=1

    if(primero<j):
        quicksort(a,primero,j)
    if(i<ultimo):
        quicksort(a,i,ultimo)

a=[2,5,12,3,9,25,1]
r=quicksort(a,0,len(a)-1)
print(a)



