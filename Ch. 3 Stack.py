## For a call stack, the main function "greet" is at the bottom
## of the stack. Each internal functions (greet2 and bye) are
## stacked on top. Once greet2 and bye are removed from the stack,
## only then can the main function greet can be removed from the 
## stack.

## A stack has two operations: push and pop
## All function calls go onto the call stack
## The call stack can get very large which takes up a lot of memory. 


def greet(name):
    print(f"Hello, {name}")
    greet2(name)
    print("Getting ready to say goodbye")
    bye()

def bye():
    print("Ok. Bye bye!")

def greet2(name):
    print(f"How are you {name}")

greet("Jonathan")

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))