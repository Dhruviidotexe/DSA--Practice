class Node:
    def __init__ (self, info, next=None):
        self.data = info
        self.next= next

class singly_linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp= Node(value)
        if self.head != None:
            T1= self.head
            while T1.next != None:
                T1= T1.next
            T1.next= temp
        else:
            self.head= temp

    def insert_at_beginning(self, value):
        temp= Node(value)
        temp.next= self.head
        self.head= temp

    def insertIn_between(self, value, position):
        temp= Node(value)
        T1= self.head

        while(T1.next != None):
            if T1.data == position:
                temp.next= T1.next
                T1.next= temp
                break
            T1= T1.next

    def print_list(self):
        T1= self.head
        while (T1.next != None):
            print(T1.data)
            T1= T1.next 
        print(T1.data)  


obj = singly_linked_list()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_beginning(5)
obj.insertIn_between(40, 20)
obj.print_list()