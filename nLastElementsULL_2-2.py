##Implement an algorithm to find the nth to last element of a singly linked list

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

    def isEmpty(self):
        """to see whether the list is empty. It needs no parameters and returns a boolean value"""
        return self.head == None

    def add(self,item):
        """adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list"""
        temp = Node(item)
        temp.setNext(self.head)
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
            
    def printUnorderedList(self):
        """print all data"""
        current = self.head
        while current != None:
            print(str(current.getData()) + ' ', end="")
            current = current.getNext()
        print()

    def getNlastElement(self, n):
        """return the nth (>0) element since the tail"""
        assert(n > 0)
        position = self.size() - n + 1
        if position <= 0:
            print ("Out of index")
        else:
            count = 1
            current = self.head
            while count < position:
                current = current.getNext()
                count += 1
            print(str(current.getData()) )

if __name__ == "__main__":
    ul = UnorderedList()
    ul.add(0)
    ul.add(1)
    ul.add(0)
    ul.add(2)
    ul.add(0)
    ul.add(3)
    ul.add(4)
    ul.add(1)
    ul.printUnorderedList()
    print()
    ul.getNlastElement(9)
    ul.getNlastElement(8)
    ul.getNlastElement(7)
    ul.getNlastElement(1)
