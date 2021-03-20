## Recursion is simply a function that calls itself! Kinda weird
## Replaces a while loop. May not be the most efficient method,
## but may be the most practical at the time.
## Every recursion has two cases: base and resursive

def recursion(big,small):
    big = big/small
    print(big)
    if big > 100:
        recursion(big,small)
    else: 
        print("We are done here!")

recursion(10000,2)

def countdown (i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(7)


