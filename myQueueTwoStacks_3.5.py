##Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    """a queue using two stacks"""
    def __init__(self):
        self.A = []
        self.B = []

    def isEmpty(self):
        """is queue empty?"""
        return self.A == [] and self.B == []

    def enqueue(self, element):
        self.B.append(element)

    def dequeue(self):
        element = None
        if self.A == []:
            while self.B != []:
                self.A.append(self.B.pop())
        if self.A != []:
            element = self.A.pop()
        return element

    def __str__(self):
        return "{0} {1}".format(self.A, self.B)


if __name__  == '__main__':
    myQ = MyQueue()
    myQ.enqueue(1)
    myQ.enqueue(2)
    myQ.enqueue(3)
    print(myQ)

    print("Dequeue :  {}".format(myQ.dequeue()))
    print(myQ)
    myQ.enqueue(4)
    myQ.enqueue(5)
    print(myQ)
    print("Dequeue :  {}".format(myQ.dequeue()))
    print(myQ)
    
    
