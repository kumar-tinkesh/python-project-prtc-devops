class Node:
    def __init__(self, data, next=None):
        self.data= data 
        self.next = next 


class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is not None:
            pass
        else:
            print('Linked list is empty!')



ll = SLL()
ll.display()