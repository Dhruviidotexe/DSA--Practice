class Node:
    def __init__(self, info. next=None):
        self.data = info
        self.next= next

class singly_linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp= Node(30)
        if self.head != None:
            T1= self.head
            while T1.next != None:
                T1= T1.next
            T1.next= temp
        else:
            self.head= temp
    def print_list(self):
        T1= self.head
        while T1 != None:
            print(T1.data)
            T1= T1.next 