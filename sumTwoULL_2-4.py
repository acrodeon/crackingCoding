##You have two numbers represented by a linked list, where each node contains a single digit.
##The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
##EXAMPLE
##Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
##Output: 8 -> 0 -> 8

class Node:
    def __init__(self,initdata):
        """First, the node must contain the list item itself. We will call this the data field of the node. In addition, each node must hold a reference to the next node (None by default)"""
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        """list object will maintain a single reference to the head of the list"""
        self.head = None
        self.tail = None

    def isEmpty(self):
        """to see whether the list is empty. It needs no parameters and returns a boolean value"""
        return self.head == None

    def add(self,item):
        """adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list"""
        temp = Node(item)
        temp.setNext(self.head)
        if self.head == None:
           self.tail = temp
        self.head = temp


    def append(self,item):
        """adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list"""
        temp = Node(item)
        if self.tail != None:
            self.tail.setNext(temp)
        self.tail = temp
        if self.head == None:
            self.head = temp

    def size(self):
        """returns the number of items in the list. It needs no parameters and returns an integer"""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        """searches for the item in the list. It needs the item and returns a boolean value"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        """removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # we assume item is present
        if previous == None:
            # the item to be removed happens to be the first item
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            if self.tail == current:
                # the item to be removed happens to be the last item
                self.tail = previous
            
    def printUnorderedList(self):
        """print all data"""
        current = self.head
        while current != None:
            print(str(current.getData()) + ' ', end="")
            current = current.getNext()
        print()

    def getHead(self):
        """return the head of the list"""
        return self.head


def sumTwoULL(u1, u2):
    """adds the two numbers as linked lists and returns the sum as a linked list"""
    resList = UnorderedList()
    currentU1 = u1.getHead()
    currentU2 = u2.getHead()
    sum = 0 
    while currentU1 != None or currentU2 != None:
        if currentU1 != None and currentU2 != None:
            sum += currentU1.getData() + currentU2.getData()
            resList.append(sum%10)
            sum = sum // 10
            currentU1 = currentU1.getNext()
            currentU2 = currentU2.getNext()
        elif currentU2 != None:
            resList.append(currentU2.getData())
            sum = 0
            currentU2 = currentU2.getNext()
        elif currentU1 != None:
            resList.append(currentU1.getData())
            sum = 0
            currentU1 = currentU1.getNext()
    return resList


if __name__ == "__main__":
    u1 = UnorderedList()
    u1.add(5)
    u1.add(1)
    u1.add(3)
    u2 = UnorderedList()
    u2.add(2)
    u2.add(9)
    u2.add(5)
    u1.printUnorderedList()
    u2.printUnorderedList()
    sumTwoULL(u1,u2).printUnorderedList()

    print()
    
    u1 = UnorderedList()
    u1.add(5)
    u1.add(1)
    u1.add(3)
    u2 = UnorderedList()
    u1.printUnorderedList()
    u2.printUnorderedList()
    sumTwoULL(u1,u2).printUnorderedList()
 
