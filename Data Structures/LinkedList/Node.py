
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def node_Traverse(self):
        currNode = self
        while currNode is not None:
            print(currNode.value)
            currNode = currNode.next

    def binary_to_int(self):
        reference = []
        result = 0
        while self is not None:
            reference.append(self.value)
            self = self.next
        
        for index in range(len(reference)):
            if reference[index] == 1:
                result = result + (2 ** index)
        return result
    
    # def is_circular(self):
    #     if self is None:
    #         return False

    #     slow = self
    #     fast = self

    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
            
    #         if slow == fast:
    #             return True

    #     return False

    def is_circular(self):
        visited = set()
        currNode = self
        
        while currNode is not None:
            if currNode in visited:
                return True
            visited.add(currNode)
            currNode = currNode.next
        return False
    
    def find_last_node_in_cycle(self):
        # num1 -> num2 -> num3 -> num4 -> num2
        # num4 is the last node
        visited = set()
        lastNode, currNode = None, self

        while currNode is not None:
            
            if currNode not in visited:
                lastNode = currNode
                visited.add(currNode)
                currNode = currNode.next
            else:
                return lastNode
            
    def partition(head, val):
        # Create two temporary heads
        less_head = less = Node(0)
        greater_head = greater = Node(0)
        
        # Traverse the original list
        current = head
        while current:
            if current.value < val:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Ensure the last node of the greater list points to None
        greater.next = None
        
        # Combine the two lists
        less.next = greater_head.next
        
        return less_head.next


            
    def toList(self):
        # 2 -> 4 -> 3 = [2, 4, 3]
        res = []
        currNode = self
        while currNode is not None:
            res.append(currNode.value)
            currNode = currNode.next
        return res
    
    def add_two_numbers(x, y):
        xDigit = x.toList() # [1, 2, 3]
        xDigit.reverse()
        yDigit = y.toList() # [4, 5]
        yDigit.reverse()

        lenX_Digit = len(xDigit)
        lenY_Digit = len(yDigit)

        if lenY_Digit < lenX_Digit:
            # [0] * 1 + [4, 5]
            # [0, 4, 5]
            yDigit = [0] * (lenX_Digit - lenY_Digit) + yDigit
            # This creates a new list of the needed padding and concate the original to the list.
        elif lenY_Digit > lenX_Digit:
            xDigit = [0] * (lenY_Digit - lenX_Digit) + xDigit

        carry = 0
        result = [0] * len(xDigit) # len(x)
        # Addition
        for digits in range(len(xDigit) - 1, -1, -1):
            # [1, 2, 3] -> X
            # [0, 4, 5] -> Y

            # [3, 7, 8]
            # [2, 6, 3]
            
            currentSum = xDigit[digits] + yDigit[digits] + carry
            if currentSum >= 10:
                carry = 1
                result[digits] = currentSum - 10
            else:
                carry = 0
                result[digits] = currentSum
        
        if carry > 0:
            result = [carry] + result
        # return result
        return int(''.join(map(str, result)))
