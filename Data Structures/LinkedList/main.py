from LinkedList import LinkedList
from Node import Node

LinkedList = MyLinkedList()


# LinkedList.append("a")
# LinkedList.append("b")
# LinkedList.append("c")
# LinkedList.append("d")
# LinkedList.append("e")
# LinkedList.insert_Beginning("a")
# LinkedList.append("f")
# LinkedList.traverse()
# print()

# # LinkedList.delete_last()
# # LinkedList.delete_first()
# # LinkedList.traverse()

# LinkedList.remove_this("a")
# LinkedList.insert_after("f", "g")
# LinkedList.insert_after("b", "123")

# LinkedList.traverse()
# print(LinkedList.allValues())
# print(f"The length of Linked List is -> {LinkedList.number_of_Node()}")
# print(f"The value of last node is -> {LinkedList.last_Node()}")
# print(LinkedList.find("123"))


# node1 = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# node4 = Node("D")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1

# print(node1.is_circular())
# node1 -> node2 -> node3 -> node1
# print(node1.find_last_node_in_cycle().value)

# node1 = Node(1)
# node2 = Node(1)
# node3 = Node(0)
# node4 = Node(0)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# print(node1.binary_to_int())

# node1 = Node(2)
# node2 = Node(4)
# node3 = Node(2)

# node1.next = node2
# node2.next = node3

# node1a = Node(5)
# node2a = Node(6)
# node3a = Node(2)

# node1a.next = node2a
# node2a.next = node3a

# print(node1.add_two_numbers(node1a))

node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ans = node1.partition(val = 3)
print(ans.node_Traverse())

