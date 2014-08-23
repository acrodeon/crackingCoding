##Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented.
##The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

# from python interactive repo
from stack import Stack

def sortStack(st):
    """sort a stack in ascending order"""
    tempSt = []
    while not st.isEmpty():
        element = st.pop()
        while tempSt != [] and element < tempSt[-1]:
            st.push(tempSt.pop())
        tempSt.append(element)
    return tempSt


if __name__  == '__main__':
    st = Stack()
    for i in range(10,-1,-1):
        st.push(i)
    sortList = sortStack(st)
    print(sortList)

    
    




        
    

