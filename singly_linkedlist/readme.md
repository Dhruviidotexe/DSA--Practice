Singly Linked List

A Singly Linked List is a linear data structure where each element (node) contains:

Data – the value stored in the node
Next – a reference to the next node

The last node points to None.

Head
 ↓
[10 | •] → [20 | •] → [30 | None]
1. Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Creating nodes:

a = Node(10)
b = Node(20)

a.next = b
2. Basic Operations
Traversal

Visit every node from the head.

def traverse(head):
    current = head

    while current:
        print(current.data)
        current = current.next

Time: O(n)
Space: O(1)

Insert at Beginning
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

Time: O(1)