##Describe how you could use a single array to implement three stacks.
##Divide the array in three equal parts and allow the individual stack to grow in that limited space

# each stack should contain at most 300 elements different than None
stackSize = 10 + 1

# list[j] is the index of top element in stack j
# no element in stackSize*i for i=0,1 or 2
top = [i * stackSize for i in range(3)]

array = [None]*3*stackSize

def isEmpty(stackNumber):
    """ is stack 'stackNumber'(=0,1 ou 2) empty?"""
    assert(-1<stackNumber<3)
    return top[stackNumber] == stackSize*stackNumber

def push(stackNumber, element):
    """puch element in top position of stack 'stackNumber'"""
    assert(-1<stackNumber<3)
    if (top[stackNumber] - stackSize*stackNumber) < (stackSize-1):
        top[stackNumber] += 1
        array[top[stackNumber]] = element
    else:
        print("ERROR : stack number {} is full".format(stackNumber))

def pop(stackNumber):
    """pop the top element of stack 'stackNumber'"""
    assert(-1<stackNumber<3)
    if isEmpty(stackNumber):
        return None
    element = array[top[stackNumber]]
    array[top[stackNumber]] = None         
    top[stackNumber] -= 1
    return element
    
def peek(stackNumber):
    """return just the top element of stack 'stackNumber'"""
    assert(-1<stackNumber<3)
    if isEmpty(stackNumber):
        return None
    return array[top[stackNumber]]


if __name__  == '__main__':
    for i in range(10):
        push(0,i)
        push(1,2*i)
        push(2,3*i)

    print("After push of ten elements in each stack")
    print(array)

    pop(0)
    pop(0)
    pop(0)
    pop(1)
    pop(1)
    pop(2)
    print("After 3 pop stack 0, 2 pop stack 1 and 1 pop stack 2")
    print(array)

    print("Top stack 0 : {}".format(peek(0)))
    print("Top stack 1 : {}".format(peek(1)))
    print("Top stack 2 : {}".format(peek(2)))      
    
    
    

    

    
    


