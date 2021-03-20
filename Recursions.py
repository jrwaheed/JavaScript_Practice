## Wtih each pass through the function, the "list" is redined by [1:]!!!!!

list =[3,5,6,4,4,456,8,5,6,4]

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])



def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum(list))

def max(list):
    if list == []:
        return 0
    elif list[0] > list[1]
        return list[0]
    return max(list[1:])

print(max(list))