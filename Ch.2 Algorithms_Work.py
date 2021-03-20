## As far as I know, you cannot introduce global variable into a function for Python.
## However, you can pull another FUNCTION into another function. 

## These two functions work together to sort a List from smallest to largest. 
## The findSmallest function first goes through the list and finds the smallest value.
## The selectionSort then creates a new List with the sorted elements.



def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

arr =[34,43,5665,34,22,654,45,8,43,7,2]
print(arr)

print(findSmallest(arr))

def selectionSort(arr):
    newArr =[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort(arr))
