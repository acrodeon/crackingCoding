##Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
##Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity.
##SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
##Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:
    """several stacks, and should create a new stack once the previous one exceeds capacity"""
    def __init__(self, stackSize):
        self.limit = stackSize
        self.stacks = [[]]
        self.tops = [-1]
        self.lastStack = 0

    def isEmpty(self, stackNumber):
        """is stack with index stackNumber in self.stacks empty?"""
        if stackNumber <= self.lastStack:
            return self.tops[stackNumber] == -1 
        return True

    def isFull(self, stackNumber):
        """is stack with index stackNumber in self.stacks full?"""
        if stackNumber <= self.lastStack:
            return self.tops[stackNumber] == self.limit - 1 
        return False

    def push(self, element):
        if self.isFull(self.lastStack):
            self.stacks.append([])
            self.tops.append(-1) 
            self.lastStack += 1
        self.stacks[self.lastStack].append(element)
        self.tops[self.lastStack] += 1

    def pop(self):        
        if self.isEmpty(self.lastStack):
            # could be only the first empty stack
            return None
        element = self.stacks[self.lastStack].pop()
        self.tops[self.lastStack] -= 1
        if self.lastStack > 0 and self.isEmpty(self.lastStack):
            # lastStack is empty and it is not the first stack
            self.lastStack -= 1
            self.stacks.pop()
            self.tops.pop()
        return element
            
    def popAtIndex(self, index):
        """a pop operation on a specific sub-stack"""
        if self.isEmpty(index):
            return None
        element = self.stacks[index].pop()
        self.tops[index] -= 1
        if self.isEmpty(index) and index > 0 and index == self.lastStack:
            # index is an empty stack and it is the last stack different than the first one
            self.lastStack -= 1
            self.stacks.pop()
            self.tops.pop()
        if self.lastStack > 0 and index < self.lastStack:
            # if it is not the last stack we append an element from bottom of nextStack (at least two stacks)
            rolloverElement = self.stacks[index+1][0]
            # we delete bottom element from stack index+1
            del self.stacks[index+1][0]
            self.tops[index+1] -= 1
            if self.isEmpty(index+1):
                # stack index+1 is empty and we delete it
                del self.stacks[index+1]
                self.lastStack -= 1
            # we append bottom element to index stack
            self.stacks[index].append(rolloverElement)
            self.tops[index] += 1
        return element
        
    def printStacks(self):
        for i, st in enumerate(self.stacks):
            print("Stack {0} : {1}".format(i,st))

if __name__  == '__main__':
    setOfSt = SetOfStacks(3)

    setOfSt.push(1)
    setOfSt.push(2)
    setOfSt.push(3)
    setOfSt.printStacks()
    print()
    setOfSt.push(4)
    setOfSt.printStacks()
    setOfSt.push(5)
    setOfSt.push(6)
    setOfSt.push(7)
    setOfSt.push(8)
    setOfSt.printStacks()

    setOfSt.pop()
    print("After on pop")
    setOfSt.printStacks()

    setOfSt.popAtIndex(0)
    print("After on pop on stack 0")
    setOfSt.printStacks()
    
    
    
    
        
        
        
