from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None # Initially, there is nothing in the list.

    def insertionAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            # If there is empty linked list, then make the newNode as the head of our
            # new linked list.
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode
    # DummyNode -> B -> C | Add A
    def insertionAtHead(self, data):
        # b -> c
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node

    def remove(self, target):
        if self.head is None:
            return "List Empty"
        while self.head and self.head.data == target:
            self.head = self.head.next

        prevNode = self.head
        currNode = self.head

        while currNode:
            if currNode.data != target:
                prevNode = currNode
                currNode = currNode.next
            else:
                # 1 -> 2 -> 3 -> 4
                prevNode.next = currNode.next
                currNode = currNode.next

        return self.head

    def removeAtIndex(self, index):

        if index == 0:
            self.head = self.head.next

        currNode = self.head
        prevNode = self.head
        counter = 0
        while currNode:
            if counter != index:
                counter += 1
                prevNode = currNode
                currNode = currNode.next
            else:
                # counter == index
                prevNode.next = currNode.next
                currNode = currNode.next

        return self.head

    def listTraversal(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.data)
            tempNode = tempNode.next

    def getValues(self):
        # Returns an array of all the values in the linked list, ordered from head to tail
        currNode = self.head
        resultArray = []
        while currNode:
            if currNode.data:
                resultArray.append(currNode.data)
            currNode = currNode.next
        return resultArray
