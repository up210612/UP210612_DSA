def moveRight(list, mov):
    for i in range(mov+1):
        last = list.pop()
        list.insert(0, last)
    return list


def checkSyn(list2):
    list2 = list2.split()
    for i in range(len(list2)+1):
        if ')' in list2 and '(' in list2:

            list2.remove(')')
            list2.remove('(')
            continue
        if '(' in list2 or ')' in list2:
            res = "incorrect  syntaxis"
            break
        res="correct syntaxis"
    return res
    



list = [5, 2, 1, 6, 3, 8, 6, 4, 7]
move= int (input("Ingrese la cantidad de veces que quiere recorrerse: "))
list= moveRight(list, (move-1))
print("1)-->", list)

list2= ('( a * + ( ) ) b ( ) ')
response = checkSyn(list2)
print("2)-->", response)

