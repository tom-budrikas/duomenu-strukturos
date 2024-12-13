class LinkedList:
    def __init__(self, data, init_type="insert_start"):
        if not isinstance(data, list):
            raise Exception("Linked List must be passed a list.")
        elif not len(data) > 0:
            raise Exception("Linked List must be passed a list that is not empty.")
        else:
            self.length = 0
            self.head = None
            if init_type == "insert_start":
                for num in data[::-1]:
                    self.insertNodeStart(num)
            if init_type == "insert_end":
                for num in data:
                    self.insertNodeEnd(num)
            self.current = self.head

    def insertNodeStart(self, num):
        new_node = ListNode(num)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insertNodeIndex(self, index, num):
        if index == 0:
            self.insertNodeStart(num)
        else:
            previous = self.getNodeAtIndex(index - 1)
            new_node = ListNode(num)
            if previous.next == None:
                previous.next = new_node
            else:
                current = self.getNodeAtIndex(index)
                previous.next = new_node
                new_node.next = current
        self.length += 1

    def insertNodeEnd(self, num):
        if self.getLength() > 0:
            last_node = self.getLastNode()
            new_node = ListNode(num)
            last_node.next = new_node
        else:
            new_node = ListNode(num)
            self.head = new_node
        self.length += 1

    def getLength(self):
        return self.length

    def getFirstNode(self):
        return self.head
    
    def getLastNode(self):
        current = self.head
        if current is None:
            raise Exception("The Linked List is empty.")
        while current.next != None:
            current = current.next
        return current

    def getNodeAtIndex(self, index):
        count = 0
        current = self.head
        if index < 0:
            raise Exception("Index provided is out of bounds.")
        while count <= index:
            if count == index and current != None:
                return current
            elif current.next != None:
                count += 1
                current = current.next
            else:
                raise Exception("Index provided is out of bounds.")
    def removeLastNode(self):
        previousNode = self.getNodeAtIndex(self.getLength()-2)
        previousNode.next = None
        self.length -= 1

    def removeFirstNode(self):
        first_node = self.getFirstNode()
        if self.getLength() > 1:
            next_node = self.getNodeAtIndex(1)
            self.head = next_node
        if self.getLength() < 1:
            raise Exception("Linked List is already empty.")
        del first_node
        self.length -= 1

    def removeNodeAtIndex(self, index):
        if self.getLength() < 1:
            raise Exception("Linked List is already empty.")
        
        if index == 0:
            self.removeFirstNode()
        elif index == self.getLength() - 1:
            self.removeLastNode()
        else:
            previous_node = self.getNodeAtIndex(index - 1)
            selected_node = self.getNodeAtIndex(index)
            next_node = self.getNodeAtIndex(index + 1)
            previous_node.next = next_node
            del selected_node


    def printList(self):
        current = self.head
        if (current is None):
            print("Linked List is empty.")
        else:
            while current is not None:
                print(current.data)
                current = current.next
            
class ListNode:
    def __init__(self, data):
        self.data = data   
        self.next = None