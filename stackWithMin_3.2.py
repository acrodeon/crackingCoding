##How would you design a stack which, in addition to push and pop,
##also has a function min which returns the minimum element?
##Push, pop and min should all operate in O(1) time.

stackSize = 10 + 1
stack = [None]*stackSize
top = 0
# using an additional stack which keeps track of the mins
minStack = [None]*stackSize

def isEmpty():
    """ is stack empty?"""
    return top==0

def push(element):
    """puch element in top position of stack 'stackNumber' keeping min element updated"""
    global top
    if top < stackSize:
        top += 1
        stack[top] = element
        if (top == 1) or (minStack[top-1] < element):
            minStack[top] = element
        else:
            minStack[top] = minStack[top-1]
    else:
        print("ERROR : stack is full")

def pop():
    """pop the top element of stack 'stackNumber'"""
    global top
    if isEmpty():
        return None
    element = stack[top]
    stack[top] = None
    minStack[top] = None
    top -= 1
    return element

def getMinimum():
    """return the minimum element of the stack"""
    return minStack[top]


if __name__  == '__main__':
    for i in range(5):
        push(i)
    push(-100)
    push(8)
    push(6)

    print(stack)
    print("Minimum : {}".format(getMinimum()))

    pop()
    pop()

    print(stack)
    print("Minimum : {}".format(getMinimum()))

    

