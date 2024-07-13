from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.value)
            currNode = currNode.next
    
    def append(self, data): # Function add node to last.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, set the head as the new node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Set the next attribute of the last node to the new node

    def length(self):
        count = 0
        currNode = self.head
        while currNode is not None:
            count += 1
            currNode = currNode.next
        return count
    
    def insert_Beginning(self, data):
        # b -> c
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node
    
    def insert_after(self, afterValue, insertingValue):
        # afterValue = B
        # insertingValue = C
        # A -> B -> D
        newNode = Node(insertingValue)
        currNode = self.head

        # while currNode:
        #     if currNode.value != afterValue:
        #         prevNode = currNode
        #         currNode = currNode.next
        #     else:
        #         newNode.next = currNode.next
        #         currNode.next = newNode
        while currNode:
            if currNode.value == afterValue:
                newNode.next = currNode.next
                currNode.next = newNode
                return  # Exit after inserting the node
            currNode = currNode.next
        
    def last_Node(self):
        currNode = self.head
        lastNode = None
        while currNode is not None:
            lastNode = currNode.value
            currNode = currNode.next
        return lastNode

    # A -> B -> C -> None
    def delete_last(self):
        if self.head is None: 
            # Handles the edge case where the list is empty
            return None
        
        elif self.head.next is None:
            # Handles the case where there is only one element in the list
            self.head = None
            return
        
        else:
            currNode, prevNode = self.head, None
            while currNode.next is not None:
                prevNode = currNode
                currNode = currNode.next
            prevNode.next = None

    # A -> B -> C -> None | Del A
    def delete_first(self):
        if self.head is None:
            # Handles the edge case where the list is empty
            return None
        
        if self.head.next is None:
            # Handles the case where there is only one element in the list
            self.head = None
            return
        
        # Handles the general case
        self.head = self.head.next

    def find(self, target):
        currNode = self.head
        while currNode:
            if currNode.value == target:
                return True
            currNode = currNode.next
        return False
    
    def remove_this(self, target):
        # A -> B -> C -> D
        if self.head is None:
            return "List Empty"
        while self.head and self.head.value == target:
            self.head = self.head.next
        prevNode, currNode = self.head, self.head
        while currNode:
            if currNode.value != target:
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
        
        currNode, prevNode = self.head, self.head
        counter = 0
        # 1 -> 2 -> 3 -> 4
        while currNode:
            if counter != index:
                counter += 1
                prevNode = currNode
                currNode = currNode.next
            else:
                prevNode.next = currNode.next
                currNode = currNode.next


    def is_empty(self):
        return self.head is None
    
    def allValues(self):
        currNode = self.head
        res = []
        while currNode:
            if currNode.value:
                res.append(currNode.value)
            currNode = currNode.next
        return res
