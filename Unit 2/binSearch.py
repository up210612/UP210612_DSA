def binSearch(list,value):
    prin=0
    i=0
    fin=int(len(list))
    middle= int((prin+fin)//2)
    while prin<=fin and list[middle]!=value:
        if value< list[middle]:
            fin=middle-1
            i+=1
        else:
            prin=middle+1
            i+=1
        middle=int((prin+fin)//2)
        
    if list[middle]== value:
        return middle, i
    else: 
        return "none"

a=[1,3,4,5,7,8,9,10,11,13,14]
#value = 14
value=int(input("Enter value: "))
back= binSearch(a,value)
print(back)