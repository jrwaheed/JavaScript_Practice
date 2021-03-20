## Notice that recursion is used twice here!!

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)  ##<---Recursion use

arr = [44,4,456,546,3456,54,656,6,8,45,3]

print(quickSort(arr))